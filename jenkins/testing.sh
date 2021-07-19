#!bin/bash

# create a venv and install requirements
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

# service-1 pytest coverage
cd service-1
python3 -m pytest --cov=app
cd ..

# make_api pytest coverage
cd make_api
python3 -m pytest --cov=app
cd ..

# model_api pytest coverage
cd model_api
python3 -m pytest --cov=app
cd ..

# mot_api pytest coverage
cd mot_api
python3 -m pytest --cov=app
cd ..