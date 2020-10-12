all: minikube-cluster apply-spark-rbac secrets dashboard

minikube-cluster:
	minikube --memory 8192 --cpus 4 start
	echo "Please run 'kubectl cluster-info' and put the master URL to the .env"

../spark-rbac.yaml:
	cd .. & wget https://raw.githubusercontent.com/GoogleCloudPlatform/spark-on-k8s-operator/master/manifest/spark-rbac.yaml

apply-spark-rbac: ../spark-rbac.yaml
	kubectl apply -f ../spark-rbac.yaml

secrets:
	bash ../populate-secrets.sh

dashboard:
	minikube dashboard