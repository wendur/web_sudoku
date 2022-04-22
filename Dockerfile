FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP = "app.py"
ENV FLASK_ENV = development
ENV FLASK_DEBUG = 0

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]
