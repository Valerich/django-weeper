# -*- coding: utf-8 -*-
import hashlib

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.template import Template, Context
from django.utils.translation import ugettext_lazy as _


TASK_DELIVERY_STATUSES = (
    (1, _('new')),
    (2, _('ready for distribution')),
    (3, _('sent')),
    (4, _('closed'))
)


class TaskDelivery(models.Model):
    date_add = models.DateTimeField(_('date add'), auto_now_add=True)
    name = models.CharField(_('name'), max_length=255, blank=True, null=True)
    users = models.ManyToManyField(get_user_model(), verbose_name=_('users'))
    status = models.PositiveSmallIntegerField(_('status'),
                                              choices=TASK_DELIVERY_STATUSES,
                                              default=1)
    deadline = models.DateTimeField(_('deadline'))
    date_send = models.DateTimeField(_('date send'), blank=True, null=True)
    task_url = models.URLField(_('task url'))

    first_email_text = models.TextField(
        _('first email text'),
        help_text="use {{ username }}, {{ email }}, {{ deadline }}, {{ link }}, {{ hash }}")
    reminders_text = models.TextField(
        _('reminders text'), blank=True, null=True,
        help_text="use {{ username }}, {{ email }}, {{ deadline }}, {{ link }}, {{ hash }}")
    day_before_deadline_text = models.TextField(
        _('day before deadline text'), blank=True, null=True,
        help_text="use {{ username }}, {{ email }}, {{ deadline }}, {{ link }}, {{ hash }}")
    day_deadline_text = models.TextField(
        _('day deadline text'), blank=True, null=True,
        help_text="use {{ username }}, {{ email }}, {{ deadline }}, {{ link }}, {{ hash }}")
    after_deadline_text = models.TextField(
        _('after deadline text'), blank=True, null=True,
        help_text="use {{ username }}, {{ email }}, {{ deadline }}, {{ link }}, {{ hash }}")

    class Meta:
        verbose_name = _('TaskDelivery')
        verbose_name_plural = _('TaskDeliverys')

    def __unicode__(self):
        return u'{} {}'.format(self.id, self.name if self.name else u'')

    def send(self):
        if self.status == 2:
            for user in self.users.all():
                task = Task(user=user, task_delivery=self, deadline=self.deadline)
                task.save()
            self.status = 3
            self.save()


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

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

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
                    username += getattr(self.user, field)
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

    def generate_hash(self):
        s = u'{}{}{}'.format(self.task_delivery.id, self.get_email(), self.user.id)
        return hashlib.md5(s).hexdigest()

    def set_email_text(self):
        etfs = ('first_email_text',
               'reminders_text',
               'day_before_deadline_text',
               'day_deadline_text',
               'after_deadline_text')
        context = Context({
            'username': self.get_username(),
            'email': self.get_email(),
            'deadline': unicode(self.deadline),
            'link': self.task_delivery.task_url,
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
        super(Task, self).save(*args, **kwargs)
