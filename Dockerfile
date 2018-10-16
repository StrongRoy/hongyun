FROM python:3.6-alpine

ENV FLASK_APP manager.py
ENV HONGYUN_CONFIG production

RUN adduser -D
USER hongyun

WORKDIR /home/hongyun

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY manager.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
