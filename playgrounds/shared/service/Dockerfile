FROM python:3.9

RUN pip install Flask

WORKDIR /app

COPY service.py service.py

ENV FLASK_APP=service.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
