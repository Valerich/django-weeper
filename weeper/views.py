# -*- coding: utf-8 -*-
import datetime

from django.core.urlresolvers import reverse
from django.views.generic import View, RedirectView
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Task, TaskDelivery


class TaskDeliverySend(View):

    def get(self, request, pk, *args, **kwargs):
        if request.user.is_superuser:
            try:
                td = TaskDelivery.objects.get(pk=pk)
                td.send()
                return HttpResponseRedirect(reverse('admin:weeper_taskdelivery_changelist'))
            except TaskDelivery.DoesNotExist:
                raise Http404
        else:
            return HttpResponse(status_code=500)


class TaskComplete(View):

    def get(self, request, task_hash, *args, **kwargs):
        try:
            task = Task.objects.get(hash=task_hash)
            if not task.is_complete and task.is_active:
                task.is_complete = True
                task.is_active = False
                task.date_complete = datetime.datetime.now()
                task.save()
        except Task.DoesNotExist:
            pass
        return HttpResponse()


class TaskRedirect(RedirectView):
    permanent = False

    def dispatch(self, request, task_hash, *args, **kwargs):
        try:
            self.task = Task.objects.get(hash=task_hash)
            if self.task.task_delivery.complete_by_redirect and not self.task.is_complete and self.task.is_active:
                self.task.is_complete = True
                self.task.is_active = False
                self.task.date_complete = datetime.datetime.now()
                self.task.save()
        except Task.DoesNotExist:
            raise Http404
        return super(TaskRedirect, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        url = u'{}{}'.format(
            self.task.task_delivery.task_url,
            u'?task_key={}'.format(self.task.hash) if not self.task.task_delivery.complete_by_redirect else u'')
        return url
