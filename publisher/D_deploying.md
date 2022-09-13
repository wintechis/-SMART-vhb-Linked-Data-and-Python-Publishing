# D - Deploying the Webserver with Gunicorn and NGINX

## Step 1: Create factory function

In Section A - C, the Flask instance (with its HTTP test server) was globally initiated and might raise a conflict when another WSGI HTTP Server like [Gunicorn](https://gunicorn.org/) shall be used for the production environment. Thus, we create an application factory for the Flask instance instead in file _\_\_init\_\_.py_.

## Step 2: Package application

To easily move the application to your Linux server, we build a distribution file:
1. Describe your project in file _setup.py_
2. Define included package data in _MANIFEST.in_
3. Build distribution file by running:
```console
python setup.py bdist_wheel
```

You can find the file in dist/publisher-1.0.0-py3-none-any.whl. The file name is in the format of {project name}-{version}-{python tag} -{abi tag}-{platform tag}.

4. (Rename distribution file)
```console
mv dist/publisher-1.0.0-py3-none-any.whl dist/publisher.whl
```

## Step 3: Configure python environment on Linux server
1. Establish SSH connection
2. Create project folder and virtual environment
```console
mkdir ldpy_publish
cd ldpy_publish
python -m venv env
```

3. Activate virtual environment and install packages
```console
source env/bin/activate
(env) pip install flask==2.2.2 rdflib==6.2.0 requests==2.28.1 gunicorn==20.1.0
```

## Step 4: Copy distribution file to Linux server
A simple way to transfer files from one computer to another is using the secure copy protocol (scp) following the command pattern _'scp /dir/file user@host:/dir'_

## Step 5: Install distribution file and run application with Gunicorn
1. Establish SSH connection, move to your project folder, and activate the virtual environment
2. Install the distribution file
```console
(env) pip install publisher.whl
```
3. Start the application with the Gunicorn Webserver on port 5000
```console
gunicorn --bind 0.0.0.0:5000 publisher:create_app
```
You can read more about the arguments and configuration Gunicorn offers in the [official documentation](https://docs.gunicorn.org/en/stable/).

4. Check in your browser, if you can reach the running Web server, before you proceed.

5. If you cannot reach the Web server, you server might block directly access to port 5000. You can disable your firewall for this port with:
```console
sudo ufw allow 5000
```

## Step 6: Create service to run application permanently
1. Create and open a service file for the application
```console
sudo nano /etc/systemd/system/ldpy_publish.service
```
2. Add your service configuration (see _ldpy_publish.service_), save and close the file

3. Start, enable, and check the status of your configured service
```console
sudo systemctl start ldpy_publish
sudo systemctl enable ldpy_publish
sudo systemctl status ldpy_publish
```

If your service is running, the status message should include a line with _'Active: active (running) ...'_

4. Check in your browser, if you can reach the running Web server, before you proceed.

## Step 7: Configure NGINX
1. Install NGINX, if it is not yet installed (for debian-based)
```console
sudo apt install nginx
```
2. Create configuration block (see ldpy_publish.conf)
```console
sudo nano /etc/nginx/sites-available/ldpy_publish.conf
```
3. Enable configuration block
```console
sudo ln -s /etc/nginx/sites-available/ldpy_publish.conf /etc/nginx/sites-enabled
```
4. Check for syntax errors
```console
sudo nginx -t
```
5. Restart Nginx and adjust firewall settings
```console
sudo systemctl restart nginx
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
6. Now you should be able to reach the Web server in your browser by using the domain you added in the Nginx configuration block.
