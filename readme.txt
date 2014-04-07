python manage.py migrate weeper


settings.py

INSTALLED_APPS = (
    ...
    'weeper',
    ...
)

WEEPER_EMAIL_SUBJECT = u'Рассылка'
WEEPER_REMINDER_EMAIL_SUBJECT = u'Напоминание'
WEEPER_DAY_BEFORE_DEADLINE_EMAIL_SUBJECT = u'Напоминание'
WEEPER_DAY_DEADLINE_EMAIL_SUBJECT = u'Напоминание'
WEEPER_AFTER_DEADLINE_EMAIL_SUBJECT = u'Напоминание'
WEEPER_FROM_EMAIL = 'robot@example.com'
WEEPER_USERNAME_FIELDS = ['first_name', 'last_name']
WEEPER_USER_EMAIL_FIELD = 'email'
WEEPER_CLEAR_PERIOD = 60


urls.py

urlpatterns = patterns('',
    ...
    url(r'^weeper/', include('weeper.urls', namespace='weeper')),
    ...
)


cron

55  9 * * * (/path/to/your/python /path/to/your/manage.py weeper_send_tasks)
55 13 * * * (/path/to/your/python /path/to/your/manage.py weeper_send_tasks)
30 17 * * * (/path/to/your/python /path/to/your/manage.py weeper_send_tasks)
0   1 * * * (/path/to/your/python /path/to/your/manage.py weeper_clear)


Рассылка происходит при помощи django-mailer. Так что небоходимо его также настроить
