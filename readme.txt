Установка:
    git clone https://github.com/metalhand91/simple_image_server.git
    
    cd simple_image_server
    
    sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk python3-pip
    
    sudo pip3 install -r requirements.txt
    
    python3 manage.py makemigrations
    
    python3 manage.py migrate
    
    python3 manage.py createsuperuser


Запуск:
    python3 manage.py runserver 0.0.0.0:8000


Адреса:
    панель администратора
    http://127.0.0.1:8000/admin/
    
    список всех изображений:
        http://127.0.0.1:8000/get_all/
    
    ответ:
        {"data": [{"1": "/media/4e80-27e710-4be1a1.jpg"}]}
    
    адрес одного изображения:
        http://127.0.0.1:8000/get_image/id/
        id - id изображения
    ответ:
         /media/4e80-27e710-4be1a1.jpg
