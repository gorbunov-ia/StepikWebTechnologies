mysql -uroot -e "create database qa"
sudo python /home/box/web/ask/manage.py makemigrations
sudo python /home/box/web/ask/manage.py migrate
