data "aws_caller_identity" "current" {}

data "aws_vpcs" "default" {
    filter {
        name   = "tag:isDefault"
        values = ["true"]
    }
}