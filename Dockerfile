FROM python:3.6
RUN echo 'Creating image'
 
RUN apt-get update  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y \  
   gcc \
   python-dev python-distribute \ 
   python-pip \
   python-dev \ 
   python-distribute python-pip
 
RUN mkdir /opt/my-app/  
WORKDIR /opt/my-app

ADD requirements.txt /opt/my-app/  
RUN pip install -r requirements.txt
RUN pwd
COPY . .
 
CMD ["gunicorn", "--workers=4", "-b 0.0.0.0:8000","wsgi:app"]
 
EXPOSE 8000 