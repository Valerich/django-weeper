# -*- coding: utf-8 -*-
from django import forms

from .models import TaskDelivery, TASK_DELIVERY_CREATE_STATUSES, TASK_DELIVERY_UPDATE_STATUSES


class TaskDeliveryAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskDeliveryAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.id:
            self.fields['status'].choices = TASK_DELIVERY_UPDATE_STATUSES
        else:
            self.fields['status'].choices = TASK_DELIVERY_CREATE_STATUSES

    class Meta:
        model = TaskDelivery
