#sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/conf.d/test.conf
sudo /etc/init.d/nginx restart
