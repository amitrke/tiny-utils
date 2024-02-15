#Usage: k8-cron.sh <namespace> <enable/disable>
#Description: Enable/Disable cronjob in k8s

#!/bin/bash

#Check input arguments
if [ -z "$1" ] || [ -z "$2" ]
  then
    echo "No argument supplied"
    exit 1
fi

#Check if logged into AWS
aws sts get-caller-identity > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Please login to AWS"
  exit 1
fi

CLUSTER_NAME="k8s-cluster"
REGION="us-west-2"

#Set the context
aws eks --region $REGION update-kubeconfig --name $CLUSTER_NAME

#Enable/Disable all cronjobs in the namespace
kubectl get cronjobs -n $1 | awk '{print $1}' | grep -v NAME | xargs -I {} kubectl patch cronjob {} -n $1 -p '{"spec":{"suspend":'$2'}}'
```