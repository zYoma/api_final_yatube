# Учебный проект по реализации API на базе Django REST Framework

### Установка: 

Ввыполните команды:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
mkdir /home/code
cd /home/code
virtualenv env
source env/bin/activate
git clone https://github.com/zYoma/api_final_yatube.git
cd api_final_yatube

```
Установите зависимости:
```
pip install -r requirements.txt
```
Выполните миграции:
```
python manage.py migrate
```
Создание суперпользователя:
```
python manage.py createsuperuser
```
Загрузить фикстуры:
```
python manage.py loaddata fixtures.json
```

### Доступные методы:
```
/api/v1/posts/   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments  (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments/<id>  (GET, POST, PUT, PATCH, DELETE)
/api/v1/group/ (GET, POST)
/api/v1/follow/  (GET, POST)
```

### Пример запроса к API:
```
    import requests
    
    api = 'http://127.0.0.1/api/v1/posts/'
    data = {
         'text': 'Новый пост',
     }
     headers = {'Authorization': 'Bearer ваш_токен'}
     r = requests.post(api, data=data,  headers=headers)
```
