#!/bin/bash

apt update -y
apt install docker.io -y

systemctl start docker
systemctl enable docker

docker run -d \
  -p 5000:5000 \
  -e APP_ENV=production \
  -e APP_VERSION=1.0.0 \
  cristiancosmin/flask-infra-demo:1.0.0
