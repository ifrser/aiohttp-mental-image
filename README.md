# aiohttp-mental-image
Personal mental image for aiohttp server


#### quickstart
```
sudo docker build -t test-image .
sudo docker run --rm -p 5000:5000 --name test test-image
curl -X POST localhost:5000/healthcheck
```
