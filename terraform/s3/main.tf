# Create bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-tf-test-bucket"
  acl    = "private"
  count  = var.create_bucket ? 1 : 0

  lifecycle_rule {
    id      = "delete-objects-after-30-days"
    status  = "Enabled"

    expiration {
      days = 30
    }
  }
}

# Create bucket policy

resource "aws_s3_bucket_policy" "my_bucket_policy" {
  bucket = aws_s3_bucket.my_bucket.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "MYBUCKETPOLICY",
  "Statement": [
    {
      "Sid": "IPAllow",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::my-tf-test-bucket/*",
      "Condition": {
         "NotIpAddress": {"aws:SourceIp": "
        }
    }
    ]
}
POLICY
}




