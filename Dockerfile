FROM python:3
ENV PYTHONUNBUFFERED=1

RUN pip install psycopg2
RUN pip install PyDrive3
RUN pip install oauth2client==3.0.0
RUN pip install google-api-python-client
RUN pip install google-auth-httplib2
RUN pip install google-auth-oauthlib

COPY /Devops-App /

RUN apt update
RUN apt install -y gnupg
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN apt-get install apt-transport-https
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN apt-get update && apt-get install -y logstash
COPY /jenkins/logfile_pipeline.conf /etc/logstash/conf.d/

ENTRYPOINT service logstash start && python GoogleDrive.py
