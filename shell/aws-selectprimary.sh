#Get primary region from aws-paramstore script

source ./aws-paramstore.sh "/aws/service/global-infrastructure/regions" "us-east-1"
primary_region=$param_value

#If primary region is us-east-1, then set secondary region to us-west-2
if [ $primary_region == "us-east-1" ]; then
    secondary_region="us-west-2"
else
    secondary_region="us-east-1"
fi
