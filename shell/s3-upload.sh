#Check if an argument was passed
if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit 1
fi

# Filename using date and time
filename=$(date '+%Y-%m-%d_%H-%M-%S').tar.gz

# PG Dump
pg_dump -U $POSTGRES_USER -h $POSTGRES_HOST -p $POSTGRES_PORT $POSTGRES_DB > $filename

# Replace the string "prd." with "uat." in the dump file
sed -i 's/prd./uat./g' $filename

# Compress file
tar -zcvf $filename $filename

# Upload file to S3, Year/Month/Day

aws s3 cp $filename s3://$S3_BUCKET_NAME/$(date '+%Y')/$(date '+%m')/$(date '+%d')/$filename


# Download file from S3
aws s3 cp s3://$S3_BUCKET_NAME/$(date '+%Y')/$(date '+%m')/$(date '+%d')/$filename $filename