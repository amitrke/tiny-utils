#Default VPC
output "default_vpc_id" {
  value = data.aws_vpcs.default.id
}