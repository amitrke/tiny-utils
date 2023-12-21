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

print(getBucketList(primaryRegion))
print(getBucketList(secondaryRegion))