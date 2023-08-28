#!/bin/bash

# This script will read the AWS Parameter Store and export the variables
# The script will only export the variables if they are not already set.

param_name=$1
param_default=$2

param_value=$(aws ssm get-parameter --name $1 --with-decryption --query Parameter.Value --output text 2>/dev/null)
if [ $? -ne 0 ]; then
    echo "Parameter $1 not found. Using default value: $2" 
    export AWS_PARAM_VALUE=$2
else
    export AWS_PARAM_VALUE=$param_value
fi
