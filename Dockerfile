FROM python:3.8-slim
RUN apt-get update && apt-get upgrade -y && apt-get install -y

ENV PYTHONPATH /source

WORKDIR /source

ADD ./requirements.txt .
RUN pip install -r requirements.txt

ADD . .

CMD ["python", "sample_server"]
