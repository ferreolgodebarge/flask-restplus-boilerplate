#!/bin/bash

# This script is just a way to test locally without any
# integration server. This script logic can be adapted to
# Jenkins, for example.

# Get the previous version stored statically in acc file
# This version corresponds to actual deployed application
number=$(cat ${PWD}/integration/acc)

# Identify next version to deploy when deployment will be
# triggered
next=$(($number+1))

# Ensure the folder faking the artifact repository is created
mkdir -p ${PWD}/integration/artifacts/app

# Compress the next version package
tar -czf ${PWD}/integration/artifacts/app/$next.tar.gz app/

# Increase the version to store which one will be deployed
echo $next > ${PWD}/integration/acc

# Set environment variables mandatory to the CD
export SSH_USERNAME=$SSH_USER
export SSH_PASSWORD=$SSH_PASS
export REPOSITORY_APP_PATH=${PWD}/integration/artifacts/app/$next.tar.gz
export APP_PATH=~/application/source/deploys/$next
export ENV_PATH=~/temp/server/source/environments/$next
export SYMLINK_PATH=~/application/run

# Trigger the CD
ansible-playbook -i ${PWD}/deployment/inventories/local/hosts ${PWD}/deployment/deployment.yml
