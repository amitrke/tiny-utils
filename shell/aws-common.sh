# Use AWS CLI and jq to get the DNS of the load balancer whose name starts with "k8s-<cluster-name>-api-<random-string>"

aws elbv2 describe-load-balancers \
  --query "LoadBalancers[?starts_with(LoadBalancerName, 'k8s-$CLUSTER_NAME-api-')].DNSName" \
  --output text \
  | sed 's/.*\(k8s-.*\)/\1/'
```