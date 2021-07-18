#!/bin/bash

# copy docker-compose.yaml onto manager node
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@instance-1:/home/workspace/docker-compose.yaml

# docker stack deploy
ssh -i ~/.ssh/ansible_id_rsa jenkins@instance-1 << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file docker-compose.yaml project2
EOF 