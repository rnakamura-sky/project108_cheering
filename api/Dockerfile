FROM python

WORKDIR /home/project/
COPY ./requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY ./project108 ./project108

WORKDIR /home/project/project108

