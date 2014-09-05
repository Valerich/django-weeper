# -*- coding: utf-8 -*-
from django.contrib import admin

from .forms import TaskDeliveryAdminForm
from .models import TaskDelivery, Task


class TaskDeliveryAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'status',
                    'deadline',
                    'complete_by_redirect',
                    'send_tag']
    list_filter = ['status', 'date_add', 'deadline']
    filter_horizontal = ('users',)
    form = TaskDeliveryAdminForm
    readonly_fields = ['date_send']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_delivery',
                    'user',
                    'is_active',
                    'is_complete',
                    'date_complete',
                    'send_first_email',
                    'send_reminders',
                    'send_day_before_deadline',
                    'send_day_deadline',
                    'send_last_email',
                    'hash', ]
    list_filter = ['task_delivery', 'date_add', 'date_complete']
    raw_id_fields = ['user', 'task_delivery', 'mails', ]
    readonly_fields = ['date_complete', 'hash']


MODELS = {
    TaskDelivery: TaskDeliveryAdmin,
    Task: TaskAdmin,
}

for model_or_iterable, admin_class in MODELS.items():
    admin.site.register(model_or_iterable, admin_class)
