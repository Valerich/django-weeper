# -*- coding: utf-8 -*-
import datetime
import hashlib

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models, IntegrityError
from django.template import Template, Context
from django.utils.translation import ugettext_lazy as _

from mailer.models import Message

from .utils import send_mail


email_text_help_text = _("use {{ username }}, {{ email }}, {{ deadline }}, {{ redirect_link }}, {{ link }}, {{ hash }}")


TASK_DELIVERY_CREATE_STATUSES = (
    (1, _('new')),
    (2, _('ready for distribution'))
)

TASK_DELIVERY_UPDATE_STATUSES = TASK_DELIVERY_CREATE_STATUSES + (
    (3, _('sent')),
    (4, _('closed')),
)

TASK_DELIVERY_STATUSES = TASK_DELIVERY_UPDATE_STATUSES + (
    (100, _('lock')),
)


class TaskDelivery(models.Model):
    date_add = models.DateTimeField(_('date add'), auto_now_add=True)
    name = models.CharField(_('name'), max_length=255, blank=True, null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('users'))
    status = models.PositiveSmallIntegerField(_('status'),
                                              choices=TASK_DELIVERY_STATUSES,
                                              default=1)
    deadline = models.DateTimeField(_('deadline'))
    date_send = models.DateTimeField(_('date send'), blank=True, null=True)
    task_url = models.CharField(_('task url'), max_length=200)
    complete_by_redirect = models.BooleanField(_('complete by redirect'), default=False)

    first_email_text = models.TextField(
        _('first email text'),
        help_text=email_text_help_text)
    reminders_text = models.TextField(
        _('reminders text'), blank=True, null=True,
        help_text=email_text_help_text)
    day_before_deadline_text = models.TextField(
        _('day before deadline text'), blank=True, null=True,
        help_text=email_text_help_text)
    day_deadline_text = models.TextField(
        _('day deadline text'), blank=True, null=True,
        help_text=email_text_help_text)
    after_deadline_text = models.TextField(
        _('after deadline text'), blank=True, null=True,
        help_text=email_text_help_text)
    last_email_text = models.TextField(
        _('last email text'), blank=True, null=True,
        help_text=email_text_help_text)

    class Meta:
        verbose_name = _('TaskDelivery')
        verbose_name_plural = _('TaskDeliverys')

    def __unicode__(self):
        return u'{} {}'.format(self.id, self.name if self.name else u'')

    def send_tag(self):
        if self.status == 2:
            return u'''<a href="{}">{}</a>'''.format(
                reverse("weeper:task_delivery_send", kwargs={'pk': self.pk}),
                _('Send'))
        else:
            return u''
    send_tag.short_description = _('Actions')
    send_tag.allow_tags = True

    def send(self):
        if self.status == 2:
            self.status = 100
            self.save()
            for user in self.users.all():
                self.create_task(user)
            self.status = 3
            self.save()

    def check_tasks(self):
        """Проверяем для всех ли пользователей созданы таски

        Работает только для статуса 3 ("Отправлен")

        Метод нужен для того, чтобы добавить таск для пользователя, которого добавили к рассылке уже
        после рассылки. И удалить таски пользователей, которые исключены из рассылки
        """

        if self.status == 3:
            task_users = {t.user: t for t in self.task_set.all().select_related("user")}
            for user in self.users.all():
                task = task_users.pop(user, None)
                if not task:
                    self.create_task(user)
            self.task_set.filter(user__in=task_users.keys()).delete()

    def create_task(self, user, send=True):
        try:
            task = Task(user=user, task_delivery=self, deadline=self.deadline)
            task.save()
            if send:
                task.send()
        except IntegrityError:
            # Обрабатываем ситуацию, когда таск для пользователя данной task_delivery уже существует
            pass


class Task(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_('user'))
    date_add = models.DateTimeField(_('date add'), auto_now_add=True)
    is_complete = models.BooleanField(_('is complete'), default=False)
    date_complete = models.DateTimeField(_('complete date'), blank=True, null=True)
    hash = models.CharField(_('hash'), max_length=32, unique=True)
    task_delivery = models.ForeignKey(TaskDelivery, verbose_name=_('task delivery'))
    deadline = models.DateTimeField(_('deadline'))

    first_email_text = models.TextField(_('first email text'))
    reminders_text = models.TextField(_('reminders text'))
    day_before_deadline_text = models.TextField(_('day before deadline text'))
    day_deadline_text = models.TextField(_('day deadline text'))
    after_deadline_text = models.TextField(_('after deadline text'))
    last_email_text = models.TextField(_('last email text'))

    mails = models.ManyToManyField(Message, verbose_name=_('mails'), blank=True, null=True)
    reminders_date = models.DateTimeField(_('reminders_date'), blank=True, null=True)

    send_first_email = models.BooleanField(_('send first email'), default=False)
    send_reminders = models.BooleanField(_('send reminders'), default=False)
    send_day_before_deadline = models.BooleanField(_('send day before deadline'), default=False)
    send_day_deadline = models.BooleanField(_('send day deadline'), default=False)
    send_last_email = models.BooleanField(_('send last email'), default=False)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        unique_together = ('task_delivery', 'user')

    def send(self, email_type='first'):
        types = {
            'first': (
                getattr(settings, 'WEEPER_EMAIL_SUBJECT', u'Задача'),
                self.first_email_text,
                'send_first_email'),
            'reminder': (
                getattr(settings, 'WEEPER_REMINDER_EMAIL_SUBJECT', u'Напоминание'),
                self.reminders_text,
                'send_reminders'),
            'day_before_deadline': (
                getattr(settings, 'WEEPER_DAY_BEFORE_DEADLINE_EMAIL_SUBJECT', u'Напоминание'),
                self.day_before_deadline_text,
                'send_day_before_deadline'),
            'day_deadline': (
                getattr(settings, 'WEEPER_DAY_DEADLINE_EMAIL_SUBJECT', u'Напоминание'),
                self.day_deadline_text,
                'send_day_deadline'),
            'after_deadline': (
                getattr(settings, 'WEEPER_AFTER_DEADLINE_EMAIL_SUBJECT', u'Напоминание'),
                self.after_deadline_text),
            'last': (
                getattr(settings, 'WEEPER_LAST_EMAIL_SUBJECT', u'Задача не выполнена'),
                self.last_email_text,
                'send_last_email'),
        }
        try:
            email_data = types[email_type]
            mails = send_mail(
                email_data[0],
                email_data[1],
                getattr(settings, 'WEEPER_FROM_EMAIL',
                        u'robot@{}'.format(Site.objects.get_current().domain)),
                [self.get_email(), ])
            for mail in mails:
                self.mails.add(mail)
            try:
                setattr(self, email_data[2], True)
                if email_data[2] == 'send_last_email':
                    self.is_complete = True
                self.save()
            except IndexError:
                pass
        except KeyError:
            pass

    def get_username(self):
        username = u''
        username_fields = getattr(settings, 'WEEPER_USERNAME_FIELDS', None)
        if username_fields:
            error = False
            for field in username_fields:
                if not hasattr(self.user, field):
                    error = True
                    username = u''
                    break
                else:
                    if username:
                        username += u' '
                    field = getattr(self.user, field)
                    if hasattr(field, '__call__'):
                        username += field()
                    else:
                        username += field
            if not error:
                return username
        if hasattr(self.user, 'get_full_name'):
            return self.user.get_full_name()
        elif hasattr(self.user, 'first_name'):
            return self.user.first_name
        else:
            return unicode(self.user)

    def get_email(self):
        email_field = getattr(settings, 'WEEPER_USER_EMAIL_FIELD', None)
        if email_field:
            return getattr(self.user, email_field)
        else:
            return getattr(self.user, 'email', None)

    def get_redirect_link(self):
        return u'http://{}{}'.format(
            Site.objects.get_current().domain,
            reverse("weeper:go_to_task_url", kwargs={'task_hash': self.hash}))

    def generate_hash(self):
        s = u'{}{}{}'.format(self.task_delivery.id, self.get_email(), self.user.id)
        return hashlib.md5(s).hexdigest()

    def set_email_text(self):
        etfs = ('first_email_text',
                'reminders_text',
                'day_before_deadline_text',
                'day_deadline_text',
                'after_deadline_text',
                'last_email_text')
        context = Context({
            'username': self.get_username(),
            'email': self.get_email(),
            'deadline': self.deadline,
            'link': u'{}{}'.format(
                self.task_delivery.task_url,
                u'?task_key={}'.format(self.hash) if not self.task_delivery.complete_by_redirect else u''),
            'redirect_link': self.get_redirect_link(),
            'hash': self.hash})
        first_email_text = None
        for etf in etfs:
            s = getattr(self.task_delivery, etf, None)
            if not s:
                setattr(self, etf, first_email_text)
            else:
                template = Template(s)
                email_text = template.render(context)
                setattr(self, etf, email_text)
                if etf == 'first_email_text':
                    first_email_text = email_text

    def save(self, *args, **kwargs):
        if not self.id:
            self.hash = self.generate_hash()
            self.set_email_text()
        date_add = self.date_add if self.date_add else datetime.datetime.now()
        period = self.deadline - date_add
        if period > datetime.timedelta(days=4):
            self.reminders_date = self.deadline - datetime.timedelta(days=period.days/2)
        else:
            self.reminders_date = None
        super(Task, self).save(*args, **kwargs)


def task_delivery_users_changed(instance, action, pk_set, *args, **kwargs):
    if getattr(settings, 'WEEPER_ALLOW_ADDING_USER_TO_SENT_TASK_DELIVERY', True):
        if action == 'post_add' or action == 'post_remove':
            instance.check_tasks()

models.signals.m2m_changed.connect(task_delivery_users_changed, sender=TaskDelivery.users.through)
