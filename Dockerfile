FROM python:3.8-slim

WORKDIR /source

ADD . .

CMD ["python", "server"]
