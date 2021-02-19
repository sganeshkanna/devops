#!/bin/bash

##################################################################
##### USE THIS FILE IF YOU LAUNCHED AMAZON LINUX 2 ###############
##################################################################


# get admin privelages
sudo su

# install httpd (Linux 2 version)
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
echo "Hello world from $(hostname -f)" > /var/www/html/index.html
