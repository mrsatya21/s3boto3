#!/bin/bash -xe

sleep 60 

# Check python3 version (as AL2023 comes with python 3 preinstalled) :
python3 --version

# Install pip (Reference Link : https://pip.pypa.io/en/stable/installation/#get-pip-py) : 
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

# Check AWS CLI version (as AL2023 comes with AWS CLI preinstalled) :
aws --version

# Install boto3 (Reference Link : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#using-the-aws-common-runtime-crt) : 
pip -q install boto3