# Use AWS CLI and jq to get the DNS of the load balancer whose name starts with "k8s-<cluster-name>-api-<random-string>"

nlbDNS=$(aws elbv2 describe-load-balancers \
  --query "LoadBalancers[?starts_with(LoadBalancerName, 'k8s-$CLUSTER_NAME-api-')].DNSName" \
  --output text)

nlbZoneID=$(aws elbv2 describe-load-balancers \
  --query "LoadBalancers[?DNSName=='$nlbDNS'].CanonicalHostedZoneId" \
  --output text)

#Route 53
hostedZoneName="test.helloworld.com"

#Get hosted zone ID
HOSTED_ZONE_ID=$(aws route53 list-hosted-zones-by-name \
  --dns-name $hostedZoneName \
  --query "HostedZones[0].Id" \
  --output text \
  | sed 's/.*\(Z.*\)/\1/')

route53Record="nlb.$CLUSTER_NAME.$DOMAIN_NAME"

#Update route53 DNS record with NLB DNS and region

aws 



# aws route53 change-resource-record-sets \
#   --hosted-zone-id $HOSTED_ZONE_ID \
#   --change-batch "{
#     \"Comment\": \"Update NLB DNS record\",
#       \"Changes\": [{
#         \"Action\": \"UPSERT\",
#         \"ResourceRecordSet\": {
#           \"Name\": \"$route53Record\",
#           \"Type\": \"A\",
#           \"TTL\": 300,
#           \"ResourceRecords\": [{\"Value\": \"$nlbDNS\"}]
#         }
#       }]
#     }",