import boto3
import json

# Read config.json file
with open('python/config.json') as json_file:
    config = json.load(json_file)

#Get current AWS account ID
sts = boto3.client('sts')
accountId = sts.get_caller_identity()['Account']

primaryRegion = config.get('AWS')['region']['primary']
secondaryRegion = config.get('AWS')['region']['secondary']

# Get List of all VPCs
def getVpcList(region: str):
    ec2 = boto3.client('ec2', region_name=region)
    vpcList = []
    for vpc in ec2.describe_vpcs()['Vpcs']:
        #If tag 'Name' exists, append to list
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if tag['Key'] == 'Name':
                    vpcList.append(
                        {
                            "id": vpc['VpcId'],
                            "name": tag['Value'],
                            "cidrBlockAssociationSet": vpc['CidrBlockAssociationSet']
                        }
                    )
    return vpcList

# Get List of all S3 buckets that start with 'mybucket'
def getBucketList(region: str):
    s3 = boto3.client('s3', region_name=region)
    bucketPrefix = config.get('AWS')['s3']['bucketPrefix']
    bucketList = []
    for bucket in s3.list_buckets()['Buckets']:
        if bucket['Name'].startswith(bucketPrefix):
            bucketList.append(bucket['Name'])
    return bucketList

#Function to get list of all S3 Multi Region Access Points
def getS3MultiRegionAccessPointList(region: str):
    s3Control = boto3.client('s3control', region_name=region)
    accessPointList = []
    for accessPoint in s3Control.list_multi_region_access_points(AccountId=accountId)['AccessPoints']:
        accessPointList.append({
            "name": accessPoint['Name'],
            "alias": accessPoint['Alias']
        })
    return accessPointList

#Function to get list of all SSM Parameters
def getSSMParameterList(region: str):
    ssm = boto3.client('ssm', region_name=region)
    parameterList = []
    for parameter in ssm.describe_parameters()['Parameters']:
        parameterList.append(parameter['Name'])
    return parameterList

#Function to get list of all Secrets Manager Secrets
def getSecretsManagerSecretList(region: str):
    secretsManager = boto3.client('secretsmanager', region_name=region)
    secretList = []
    for secret in secretsManager.list_secrets()['SecretList']:
        secretList.append(secret['Name'])
    return secretList

#Function to get list of all Route53 DNS
def getRoute53DNSList(region: str):
    route53 = boto3.client('route53', region_name=region)
    dnsList = []
    for dns in route53.list_hosted_zones()['HostedZones']:
        dnsList.append(dns['Name'])
    return dnsList

#Function to get a list of all ECR Repositories
def getECRRepositoryList(region: str):
    ecr = boto3.client('ecr', region_name=region)
    ecrPrefix = config.get('AWS')['ecr']['repositoryPrefix']
    repositoryList = []
    for repository in ecr.describe_repositories()['repositories']:
        if repository['repositoryName'].startswith(ecrPrefix):
            repositoryList.append(repository['repositoryName'])
    return repositoryList

print("VPCs:")
print("Primary Region: " + primaryRegion)
print(getVpcList(primaryRegion))
print("Secondary Region: " + secondaryRegion)
print(getVpcList(secondaryRegion))

print("S3 Buckets:")
print(getBucketList(primaryRegion))

print("S3 Multi Region Access Points:")
print(getS3MultiRegionAccessPointList(secondaryRegion))

print("SSM Parameters:")
print(getSSMParameterList(primaryRegion))

print("Secrets Manager Secrets:")
print(getSecretsManagerSecretList(primaryRegion))

print("Route53 DNS:")
print(getRoute53DNSList(primaryRegion))

print("ECR Repositories:")
print(getECRRepositoryList(primaryRegion))