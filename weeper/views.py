# -*- coding: utf-8 -*-
import datetime

from django.views.generic import View, RedirectView
from django.http import HttpResponse, Http404

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


class TaskRedirect(RedirectView):

    def dispatch(self, request, task_hash, *args, **kwargs):
        try:
            self.task = Task.objects.get(hash=task_hash)
            if self.task.task_delivery.complete_by_redirect and not self.task.is_complete:
                self.task.is_complete = True
                self.task.date_complete = datetime.datetime.now()
                self.task.save()
        except Task.DoesNotExist:
            raise Http404
        return super(TaskRedirect, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return self.task.task_delivery.task_url
