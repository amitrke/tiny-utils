import boto3
import json

# Read config.json file
with open('config.json') as json_file:
    config = json.load(json_file)

primaryRegion = config.get('AWS').get('region').get('primary')
secondaryRegion = config.get('secondaryRegion')

# Get List of all S3 buckets that start with 'mybucket'
def getBucketList(region: str):
    s3 = boto3.client('s3', region_name=region)
    bucketList = []
    for bucket in s3.list_buckets()['Buckets']:
        bucketList.append(bucket['Name'])
    return bucketList

print(getBucketList(primaryRegion))
print(getBucketList(secondaryRegion))