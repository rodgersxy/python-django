## Blog website in Django

```
python3 -m venv django
source django/bin/activate
pip install Django
mkdir mysite
cd mysite
django-admin startproject mysite
```

*This will generate a project structure with several directories and python scripts.
```
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```
```
cd mysite
python manage.py startapp blog
```
* These will create an app named blog in our project.
```
├── db.sqlite3
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
└── blog
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```
