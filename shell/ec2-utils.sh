# The script is used to install inital packages for ec2 instance and also to update the packages
# Script Arguments: init/update

# Check input arguments
if [ -z "$1" ]
  then
    echo "No argument supplied"
    echo "Usage: ec2-utils.sh <init/update>"
    exit 1
fi

ARG=$1

#Check if ARG is init
if [ $ARG == "init" ]; then
  sudo yum update -y --exclude=subscription-manager* --exclude=redhat*
  sudo yum install -y docker
  sudo usermod -a -G docker ssm-user
  sudo yum install -y git
  sudo yum install -y yum-utils
  sudo yum install -y jq
  sudo yum install -y wget
  sudo yum install -y unzip
  sudo pip3 install --upgrade pip
  sudo pip3 install gimme-aws-creds
fi

#Check if ARG is update
if [ $ARG == "update" ]; then
  sudo yum update -y --exclude=subscription-manager* --exclude=redhat*
  #Update kernel
  sudo yum update -y kernel
  sudo package-cleanup --oldkernels --count=1
fi
```