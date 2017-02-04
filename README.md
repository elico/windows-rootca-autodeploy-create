The first thing to do is enable apache\httpd cgi support.

On ubuntu system you will need to run:
```
sudo a2enmod cgi
sudo systemctl restart apache2
```
On CentOS 7 system follow the next tutorial to enable cgi support: https://www.server-world.info/en/note?os=CentOS_7&p=httpd&f=2

In other systems take a look at the documentation of apache 2.4 at: https://httpd.apache.org/docs/2.4/howto/cgi.html#configuring

