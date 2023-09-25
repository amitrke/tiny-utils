# Filename using date and time
filename=$(date '+%Y-%m-%d_%H-%M-%S').tar.gz

# PG Dump
pg_dump -U $POSTGRES_USER -h $POSTGRES_HOST -p $POSTGRES_PORT $POSTGRES_DB > $filename

# Compress file
tar -zcvf $filename $filename

# Upload file to S3, Year/Month/Day

aws s3 cp $filename s3://$S3_BUCKET_NAME/$(date '+%Y')/$(date '+%m')/$(date '+%d')/$filename
