#!/bin/bash

sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

cd ansible
ansible-playbook -i inventory.yaml playbook.yaml
cd ..