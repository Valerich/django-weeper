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


Закрывать таски можно двумя способами:
1) Если задача таска - просто перейти по ссылке, то при создании рассылки выставляем флаг "Закрывать при редиректе" и в письмо указываем, что человеку надо пройти по ссылке {{ redirect_link }}.

2) Вызовом урла http://example.com/weeper/complete/[task_key]/

Например с помощью такого кода:

<!DOCTYPE html>
<html>
<head>
    <title></title>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script type="text/javascript">
        var weeper_key = '4e3fdbe51ff41b279816d03f83fd9689';
        $(document).ready(function() {
            $.ajax({
                type: 'GET',
                dataType: 'jsonp',
                url: 'http://example.com/weeper/complete/' + weeper_key + '/'
            });
        })
    </script>
</head>
<body>
    Спасибо за выполнение задания
</body>
</html>

task_key можно получить на странице, если мы переходим на нее через редирект.
{{ redirect_link }} в письме будет заменен на url_таска/?task_key=task_key
