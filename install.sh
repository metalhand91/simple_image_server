#! /bin/bash

git clone https://github.com/metalhand91/simple_image_server.git
cd simple_image_server
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk pip3
sudo pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
echo "finished. to start: python3 manage.py runserver 0.0.0.0:8000"
