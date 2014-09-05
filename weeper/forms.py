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

    def clean(self):
        cleaned_data = super(TaskDeliveryAdminForm, self).clean()
        close_tasks_date = cleaned_data.get('close_tasks_date', None)
        deadline = cleaned_data.get('deadline', None)
        if close_tasks_date and deadline:
            if deadline >= close_tasks_date:
                raise forms.ValidationError("closing date of the tasks must be greater than the deadline")
        return cleaned_data
