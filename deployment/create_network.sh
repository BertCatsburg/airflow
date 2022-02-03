#! /bin/bash

docker network create \
    --driver=bridge \
    --subnet=172.33.0.0/16 \
    --attachable \
    --gateway=172.33.0.1 \
    --label com.bert.project.test=my-docker-network \
    my-net
