# -*- coding: utf-8 -*-
import datetime

from django.views.generic import View
from django.http import HttpResponse

from .models import Task


class TaskComplete(View):

    def get(self, request, task_hash, *args, **kwargs):
        try:
            task = Task.objects.get(hash=task_hash)
            if not task.is_complete:
                task.is_complete = True
                task.date_complete = datetime.datetime.now()
                task.save()
        except Task.DoesNotExist:
            pass
        return HttpResponse()
