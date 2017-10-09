#
# First flask app Dockerfile
#
#
# Pull base image
FROM centos:7

# Build Commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel git
Run easy_install pip
RUN mkdir /opt/flask_app
WORKDIR /opt/flask-app
ADD requirements.txt /opt/flask-app/
RUN pip install -r requirements.txt
ADD . /opt/flask-app

#Define Working Dir
WORKDIR /opt/flask-app

CMD ["python", "app.py", "runserver"]
