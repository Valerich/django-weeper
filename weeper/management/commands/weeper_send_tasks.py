# -*- coding: utf-8 -*-
import datetime

from django.core.management.base import BaseCommand

from ...models import TaskDelivery, Task


class Command(BaseCommand):

    def handle(self, *args, **options):
        d_tasks = TaskDelivery.objects.filter(status=2)
        for d_task in d_tasks:
            d_task.send()

        # Напоминание
        for task in Task.objects.filter(is_complete=False,
                                        send_reminders=False,
                                        reminders_date__lte=datetime.datetime.now()):
            task.send(email_type='reminder')

        # За день до дедлайна
        for task in Task.objects.filter(is_complete=False,
                                        send_day_before_deadline=False,
                                        deadline__lte=datetime.datetime.now() + datetime.timedelta(days=1)):
            task.send(email_type='day_before_deadline')

        # В день дедлайна
        for task in Task.objects.filter(is_complete=False,
                                        send_day_deadline=False,
                                        deadline__lte=datetime.datetime.now()):
            task.send(email_type='day_deadline')

        # После дедлайна
        for task in Task.objects.filter(is_complete=False,
                                        deadline__lt=datetime.datetime.now()):
            task.send(email_type='after_deadline')
