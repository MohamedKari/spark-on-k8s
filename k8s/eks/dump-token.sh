printf $(kubectl -n kube-system \
    get secrets/$(kubectl -n kube-system get secret |grep eks-admin |awk '{print $1}') \
    --template={{.data.token}} |base64 -D) > aws-k8s-token