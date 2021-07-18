#!bin/bash

# install requirements and create venv
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

# test coverage for make_api
cd make_api
python3 -m pytest --cov=app
cd ..

# test coverage for model_api
cd model_api
python3 -m pytest --cov=app
cd ..

# test coverage for mot_api
cd mot_api
python3 -m pytest --cov=app
cd ..

# test coverage for service-1
cd service-1
python3 -m pytest --cov=application