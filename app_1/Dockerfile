FROM ubuntu:latest
MAINTAINER Nathan Coulson "nathancoulson@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /app_1
WORKDIR /app_1
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app1.py"]