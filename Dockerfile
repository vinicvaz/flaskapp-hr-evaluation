FROM python:3.7.7


WORKDIR usr/src/flask_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE $PORT

CMD gunicorn -w 1 -b 0.0.0.0:$PORT wsgi:server