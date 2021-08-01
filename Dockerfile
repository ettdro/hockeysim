# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code
ENV FLASK_APP=hockeysim
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]