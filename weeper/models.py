# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models
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


class Task(models.Model):
    date_add = models.DateTimeField(_('date add'), auto_now_add=True)
    is_complete = models.BooleanField(_('is complete'), default=False)
    date_complete = models.DateTimeField(_('complete date'), blank=True, null=True)
    key = models.CharField(_('key'), max_length=32)
    task_delivery = models.ForeignKey(TaskDelivery, verbose_name=_('task delivery'))
    email = models.TextField(_('email'))
    deadline = models.DateTimeField(_('deadline'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
