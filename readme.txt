python manage.py migrate weeper


settings.py

INSTALLED_APPS = (
    ...
    'weeper',
    ...
)

WEEPER_EMAIL_SUBJECT - Заголовок письма
по умолчанию WEEPER_EMAIL_SUBJECT = u'Рассылка'

WEEPER_REMINDER_EMAIL_SUBJECT - Заголовок письма с напоминанием
по умолчанию WEEPER_REMINDER_EMAIL_SUBJECT = u'Напоминание'

WEEPER_DAY_BEFORE_DEADLINE_EMAIL_SUBJECT - Заголовок письма с напоминанием за день до дедлайна
по умолчанию WEEPER_DAY_BEFORE_DEADLINE_EMAIL_SUBJECT = u'Напоминание'

WEEPER_DAY_DEADLINE_EMAIL_SUBJECT - Заголовок письма с напоминанием в день дедлайна
по умолчанию WEEPER_DAY_DEADLINE_EMAIL_SUBJECT = u'Напоминание'

WEEPER_AFTER_DEADLINE_EMAIL_SUBJECT - Заголовок письма с напоминанием после дедлайна
по умолчанию WEEPER_AFTER_DEADLINE_EMAIL_SUBJECT = u'Напоминание'

WEEPER_FROM_EMAIL - от кого рассылается письмо
по умолчанию WEEPER_FROM_EMAIL = 'robot@' + Site.name

WEEPER_USERNAME_FIELDS - поля из которых складывается имя получателя, для добавления в письмо (тег {{ username }})
по умолчанию WEEPER_USERNAME_FIELDS = None
если параметр не указан, то:
1) если в модели User есть метод get_full_name - берем данные оттуда
2) иначе из User.first_name
3) иначе unicode(User)
в WEEPER_USERNAME_FIELDS можно указывать как атрибуты модели так и методы
например WEEPER_USERNAME_FIELDS = ['first_name', 'get_weeper_name']
в этом случае:
 class User(models.Model):
     first_name = models.CharField(...)
     ...
     def get_weeper_name(self):
         return u'а тут имя взятое из метода'

 для u = User(first_name='Олег') в письме {{ username }} будет заменен на u'Олег а тут имя взятое из метода'

WEEPER_USER_EMAIL_FIELD - поле модели user, в котором хранится email
по умолчанию WEEPER_USER_EMAIL_FIELD = 'email'

WEEPER_CLEAR_PERIOD - За какое время очищать данные випера
по умолчанию WEEPER_CLEAR_PERIOD = 60
Это означает, что записи будут удаляться через 60 дней после дедлайна

# Разрешать добавлять пользователей к отправленной рассылке (и удалять)
# если True, то при изменении TaskDelivery.users будут удалены/созданы дополнительные Task,
# если False, то при изменение набора TaskDelivery.users отправленной рассылки ни на что не повлияет
WEEPER_ALLOW_ADDING_USER_TO_SENT_TASK_DELIVERY = True


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
