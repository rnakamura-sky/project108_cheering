FROM python

RUN pip install django


COPY ./worker /home/worker
WORKDIR /home/worker

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
