import boto3
import json

# Read config.json file
with open('python/config.json') as json_file:
    config = json.load(json_file)

primaryRegion = config.get('AWS')['region']['primary']
secondaryRegion = config.get('AWS')['region']['secondary']

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
    for accessPoint in s3Control.list_access_points()['AccessPointList']:
        accessPointList.append(accessPoint['Name'])
    return accessPointList

print("S3 Buckets:")
print(getBucketList(primaryRegion))

print("S3 Multi Region Access Points:")
print(getS3MultiRegionAccessPointList(primaryRegion))