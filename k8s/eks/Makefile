all: eks-cluster apply-spark-rbac secrets dashboard

eks-cluster:
	eksctl create cluster -f eks.yml 

../spark-rbac.yaml:
	cd .. && wget https://raw.githubusercontent.com/GoogleCloudPlatform/spark-on-k8s-operator/master/manifest/spark-rbac.yaml

apply-spark-rbac: ../spark-rbac.yaml
	kubectl apply -f ../spark-rbac.yaml

secrets:
	cd .. && bash populate-secrets.sh

../../aws-k8s-token:
	cd ../.. && bash k8s/eks/dump-token.sh

dashboard: ../../aws-k8s-token
	kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml
	kubectl apply -f dashboard-rbac.yml
	echo http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login
	kubectl proxy

dashboard-token:
	kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')



