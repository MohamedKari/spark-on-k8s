include ../.env
export

all: ../spark.conf spark-notebook

../spark.conf: 
	cd .. && make spark.conf

spark-notebook: ../spark.conf
	cp ../spark.conf ./spark-notebook.conf
	
	@echo "Appling CONFIGMAP: \n ---"
	kubectl kustomize ./
	kubectl apply -k .
	@echo "---"

	rm ./spark-notebook.conf

	bash ./wait-for-pod.sh spark-notebook
	kubectl port-forward service/spark-notebook-service 8888:8888
	