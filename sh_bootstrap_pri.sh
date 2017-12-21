#!/bin/bash
apt-get update -y

# install PHP and MySQL
apt-get install git apache2 ifstat inetutils-traceroute traceroute telnet curl python python-pip python3 python3-pip libapache2-mod-python libapache2-mod-php php-mysql -y
apt-get install mysql-client -y
pip install requests flask ConfigParser mysql-connector-python flask-restful ast 
pip3 install requests
apt-get install php php-fpm php-mysql php-curl php-gd php-pear php-imagick php-imap php-mcrypt php-recode php-tidy php-xmlrpc php-curl php-gd php-intl php-json php-mbstring php-mcrypt php-xml php-zip -y

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893
apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893
apt-get install apt-transport-https
apt-get update && apt-get install azure-cli

a2enmod cgi


export DB_NAME=customersDB
export DB_USER=root
export DB_PWD=password


#Fetch  website
rm -rf /var/www/html/*
mkdir /tmp/temp-website/
cd /tmp/temp-website/
rm -rf /tmp/temp-website/*

git clone  https://github.com/MourIdri/front-end-mou-private.git
cp -R /tmp/temp-website/front-end-mou-cust/* /var/www/html/

mkdir /var/www/html/cgi-bin/sessions_log
chown -R www-data:www-data /var/www/html/
mv /var/www/html/index.html /var/www/html/oldindex.htmlbkp
chmod -R 755 /var/www/html/
chmod a+rwx /var/www/html/cgi-bin/sessions_log
chmod a+rwx /var/www/html/cgi-bin/

cd /etc/apache2/
rm /etc/apache2/apache2.conf
wget https://rgcloudmouradgeneralpurp.blob.core.windows.net/exchangecontainermourad/etcapache2apache2.conf
mv etcapache2apache2.conf apache2.conf

cd /etc/apache2/conf-enabled/
rm /etc/apache2/conf-enabled/serve-cgi-bin.conf
wget https://rgcloudmouradgeneralpurp.blob.core.windows.net/exchangecontainermourad/etcapache2conf-enabledserve-cgi-bin.conf
mv etcapache2conf-enabledserve-cgi-bin.conf serve-cgi-bin.conf