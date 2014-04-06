# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from ...models import TaskDelivery


class Command(BaseCommand):

    def handle(self, *args, **options):
        tasks = TaskDelivery.objects.filter(status=2)
        for task in tasks:
            task.send()
