# D - Deploying application with a Web Server Gateway Interface (WSGI) server

## Step 1: Create factory function

In Section A - C, the Flask instance (with its HTTP test server) was globally initiated. Now, we want to use a factory function instead (see file _\_\_init\_\_.py_).

## Step 2: Package application

To easily move the application to your Linux server, we build a distribution file:
1. Describe your project in file _setup.py_
2. Define included package data in _MANIFEST.in_
3. Build distribution file by running:
```console
(env) python setup.py bdist_wheel
```

You can find the file in dist/publisher-1.0.0-py3-none-any.whl. The file name is in the format of {project name}-{version}-{python tag} -{abi tag}-{platform tag}.

## Step 3: Configure python environment on Linux server (here: Raspberry Pi 3B+ / RaspberryPi OS Bullseye)
1. Establish SSH connection
```console
ssh pi@raspberrypi.local
```

2. Create project folder and virtual environment
```console
pi@raspberrypi:~ $ mkdir ldpy_publish
pi@raspberrypi:~ $ cd ldpy_publish
pi@raspberrypi:~/ldpy_publish $ python -m venv env
```

## Step 4: Copy distribution file to Linux server
A simple way to transfer files from one computer to another is using the secure copy protocol (scp) following the command pattern _'scp /dir/file user@host:/dir'_

_Remark: We recommend to use in the following two terminals. One for establishing a SSH connection with the Linux server and another for transferring files to the Linux server via SCP._

```console
cd dist
scp publisher-1.0.0-py3-none-any.whl pi@raspberrypi.local:~/ldpy_publish/
```

## Step 5: Install distribution file and run application with WSGI server (Waitress / Gunicorn)
1. Establish SSH connection, move to your project folder, and activate the virtual environment
2. Install the distribution file
```console
pi@raspberrypi:~ $ cd ldpy_publish
pi@raspberrypi:~/ldpy_publish $ source env/bin/activate
(env) pi@raspberrypi:~/ldpy_publish $  pip install publisher-1.0.0-py3-none-any.whl
```

3. Start the WSGI server via shell
3a. Install and start the application with the Waitress Webserver on port 5000
```console
(env) pi@raspberrypi:~/ldpy_publish $  pip install waitress
(env) pi@raspberrypi:~/ldpy_publish $ waitress-serve --listen 0.0.0.0:5000 --call publisher:create_app
```
You can read more about the arguments and configuration Waitress offers in the [official documentation](https://docs.pylonsproject.org/projects/waitress/en/latest/index.html).

3b. Install and start the application with the Gunicorn Webserver on port 5000
```console
(env) pi@raspberrypi:~/ldpy_publish $ pip install gunicorn
(env) pi@raspberrypi:~/ldpy_publish $ gunicorn --bind 0.0.0.0:5000 "publisher:create_app()"
```
You can read more about the arguments and configuration Gunicorn offers in the [official documentation](https://docs.gunicorn.org/en/stable/).

4. Check in your browser (here the url is: _raspberrypi.local:5000_), if you can reach the running Web server, before you proceed.


## Step 6: Create service to run application permanently
1. At the moment, the WSGI server is started via shell and will stop when you close the SSH connection. Thus, we must create a service that the server runs permanently. It is easier to work with an explicit Flask instance, when working with services. For that we create a simple Python file _wsgi.py_.
```console
(env) pi@raspberrypi:~/ldpy_publish $ nano wsgi.py
```console

with the content:
```python
from publisher import create_app

app = create_app()

# add app config here or in separate config file
# e.g., assign secret key
```
   
2. Check, if you can correctly run your WSGI server: 
```console
(env) pi@raspberrypi:~/ldpy_publish $ waitress-serve --listen 0.0.0.0:5000 wsgi:app
```
OR
```console
(env) pi@raspberrypi:~/ldpy_publish $ gunicorn --bind 0.0.0.0:5000 wsgi:app
```

3. Next, we must create the service configuration. The required configuration can be found in file _ldpy\_publish.service_.

Transfer the file _ldpy\_publish.service_ via scp to the Linux server:
```console
scp ldpy_publish.service pi@raspberrypi.local:~/
```

Then, open a SSH connection, move the service file to the correct location, and edit the service configuration to your settings. This includes changing the user, the path and uncommenting the execution command that starts your service:

```console
pi@raspberrypi:~ $ sudo mv ldpy_publish.service /etc/systemd/system/
pi@raspberrypi:~ $ sudo nano /etc/systemd/system/ldpy_publish.service
```

1. Start, enable, and check the status of your configured service
```console
pi@raspberrypi:~ $ sudo systemctl start ldpy_publish
pi@raspberrypi:~ $ sudo systemctl enable ldpy_publish
pi@raspberrypi:~ $ sudo systemctl status ldpy_publish
```
If your service is running, the status message should include a line with _'Active: active (running) ...'_

4. Check in your browser, if you can reach the running Web server, before you proceed.

## Step 7: Configure NGINX
1. Install NGINX, if it is not yet installed (for debian-based)
```console
pi@raspberrypi:~ $ sudo apt install nginx
```
2. Transfer configuration file _ldpy\_publish.conf_ to your Linux server via scp
```console
scp ldpy_publish.conf pi@raspberrypi.local:~/
```

3. Move configuration file _ldpy\_publish.conf_ to its right location and add your local ip address.
```console
pi@raspberrypi:~ $ sudo mv ldpy_publish.conf /etc/nginx/sites-available/
pi@raspberrypi:~ $ sudo nano /etc/nginx/sites-available/ldpy_publish.conf
```

4. Make your configuration available with via soft link
```console
pi@raspberrypi:~ $ sudo ln -s /etc/nginx/sites-available/ldpy_publish.conf /etc/nginx/sites-enabled
```
4. Check for syntax errors
```console
pi@raspberrypi:~ $ sudo nginx -t
```
5. Restart Nginx
```console
pi@raspberrypi:~ $ sudo systemctl restart nginx
```
6. Now you should be able to reach the Web server in your browser with your local IP address. Note that your Web server can be only reached in the same network. 

If you want to reach the Web server from other networks and your Linux server does not have a static IP address, there are some workarounds that are not discussed in this course with DynDNS providern (e.g., [no-ip](noip.com)).
