include ../.env
export

all: build push test-submit

build:
	$(SPARK_HOME)/bin/docker-image-tool.sh -r temp/spark-base -t latest -p $(SPARK_HOME)/kubernetes/dockerfiles/spark/bindings/python/Dockerfile build
	docker tag temp/spark-base/spark-py:latest $(BASE_IMAGE)

push:
	docker push $(BASE_IMAGE)

test-submit:
	spark-submit \
  		--master k8s://$(K8S_API_URL) \
  		--conf spark.kubernetes.container.image=$(BASE_IMAGE) \
  		--conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
  		--conf spark.kubernetes.container.image.pullPolicy=Always \
  		--deploy-mode cluster \
  		local:///opt/spark/examples/src/main/python/pi.py