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
                                        reminders_date__contains=datetime.date.today()):
            task.send(email_type='reminder')

        # За день до дедлайна
        day_before_deadline = datetime.date.today() + datetime.timedelta(days=1)
        for task in Task.objects.filter(is_complete=False,
                                        send_day_before_deadline=False,
                                        deadline__contains=day_before_deadline):
            task.send(email_type='day_before_deadline')

        # В день дедлайна
        for task in Task.objects.filter(is_complete=False,
                                        send_day_deadline=False,
                                        deadline__contains=datetime.date.today()):
            task.send(email_type='day_deadline')

        # После дедлайна
        for task in Task.objects.filter(is_complete=False,
                                        deadline__lt=datetime.date.today()):
            task.send(email_type='after_deadline')
