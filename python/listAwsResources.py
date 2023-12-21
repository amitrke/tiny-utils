primaryRegion = 'us-east-1'
secondaryRegion = 'us-west-2'

# Get List of all S3 buckets that start with 'mybucket'
def getBucketList(region: str):
    s3 = boto3.client('s3', region_name=region)
    bucketList = []
    for bucket in s3.list_buckets()['Buckets']:
        bucketList.append(bucket['Name'])
    return bucketList

print(getBucketList(primaryRegion))
print(getBucketList(secondaryRegion))