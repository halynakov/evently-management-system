1. install python
2. pip install poetry
3. poetry install
4. poetry shell
5. python manage.py runserver

python manage.py startapp myapp

 1. Провір чи встановлений в тебе python

  python --version



 2. Якщо ти побачив версію типу 3.15.2. Чудово в тебе він вже встановлений, якщо ні, то встанови його

  [Download](https://www.python.org/downloads/)



 3. Тепер провір чи встановлений в тебе django фреймвор. Командою

  python -m django --version



 4. Якщо ти побачий версію, тоді він в тебе встановлений, якшо ні тоді викоримтай наступну команду

  python -m pip install Django



 5. Встанови Django REST Framework (DRF) - це бібліотека, яка додає підтримку API в Django-проєкти. Використовується для створення бекенду, який може взаємодіяти з фронтендом або мобільними застосунками через HTTP-запити.

  pip install djangorestframework



 6. Ця команда запускає вбудований у Django сервер для тестування сайту. 
Сервер працює локально (типово на http://127.0.0.1:8000/)

  manage.py runserver



 7. Якщо ти хочеш створити новий окремий проек для реєстрації, або відображення контенту, або чогось ще використай наступну команду. Замість myapp пропиши назву проекту

  python manage.py startapp myapp 
