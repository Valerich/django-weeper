# -*- coding: utf-8 -*-
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import TaskDelivery


class Command(BaseCommand):

    def handle(self, *args, **options):
        clear_period = getattr(settings, 'WEEPER_CLEAR_PERIOD', 60)
        clear_from = datetime.datetime.now() - datetime.timedelta(days=clear_period)
        delivery_tasks = TaskDelivery.objects.filter(deadline__lte=clear_from)
        for d_task in delivery_tasks:
            for task in d_task.task_set.all():
                task.mails.all().delete()
                task.delete()
            d_task.delete()
