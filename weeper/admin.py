# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import TaskDelivery, Task


class TaskDeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'deadline']
    list_filter = ['status', 'date_add', 'deadline']
    filter_horizontal = ('users',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['key', 'is_complete', 'task_delivery']
    list_filter = ['task_delivery', 'date_add', 'date_complete']


MODELS = {
    TaskDelivery: TaskDeliveryAdmin,
    Task: TaskAdmin,
}

for model_or_iterable, admin_class in MODELS.items():
    admin.site.register(model_or_iterable, admin_class)
