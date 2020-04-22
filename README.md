#Учебный проект по реализации API на базе Django REST Framework#

Установка:

-склонируйте репозиторий
-выполните миграции


Доступные методы:

/api/v1/posts/   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/coments  (GET, POST, PUT, PATCH, DELETE)
/api/v1/group/ (GET, POST)
/api/v1/follow/  (GET, POST)

Пример запроса к API:

import requests

 api = 'http://127.0.0.1/api/v1/posts/'
    data = {
        'text': 'Новый пост',
    }
    headers = {'Authorization': 'Bearer ваш_токен'}
    r = requests.post(api, data=data,  headers=headers)
