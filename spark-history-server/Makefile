include ../.env
export

all: install-history-server

history-server-config.yaml: history-server-config.template.yaml ../.env
	export APP_IMAGE_REPO=$(shell echo $(APP_IMAGE) |awk -F":" '{print $$1}') && \
	export APP_IMAGE_TAG=$(shell echo $(APP_IMAGE) |awk -F":" '{print $$2}') && \
	cat history-server-config.template.yaml |envsubst > history-server-config.yaml

install-history-server: history-server-config.yaml
	helm repo add stable https://kubernetes-charts.storage.googleapis.com
	helm install -f history-server-config.yaml spark-history-server stable/spark-history-server
	minikube service spark-history-server