namespace="dev"

# Map of cluster names to their respective namespaces

declare -A newmap
newmap[name]="Irfan Zulfiqar"
newmap[designation]=SSE
newmap[company]="My Own Company"

echo ${newmap[company]}
echo ${newmap[name]}


declare -A clusters
clusters["dev"]="dev-cluster"
clusters["prod"]="prod-cluster"

# Print cluster name for namespace
echo ${clusters[$namespace]}
