# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import *


urlpatterns = patterns(
    '',
    url(r'^complete/(?P<task_hash>[a-z\_0-9\-]+)/$',
        TaskComplete.as_view(), name="task_complete"),
    url(r'^taskdelivery/(?P<pk>\d+)/send/$',
        TaskDeliverySend.as_view(), name="task_delivery_send"),
    url(r'^(?P<task_hash>[a-z\_0-9\-]+)/$',
        TaskRedirect.as_view(), name="go_to_task_url"),
)
