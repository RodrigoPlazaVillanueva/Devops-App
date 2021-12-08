FROM python:3-slim
ENV PYTHONUNBUFFERED=1

RUN pip install psycopg

COPY /Devops-App /

ENTRYPOINT python GoogleDrive.py
