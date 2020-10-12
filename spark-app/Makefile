include ../.env
export

all: build push submit

build:
	docker build -t $(APP_IMAGE) .

push:
	docker push $(APP_IMAGE)

../spark.conf: 
	cd .. && make spark.conf

submit: ../spark.conf
	spark-submit \
		--master k8s://$(K8S_API_URL) \
		--properties-file ../spark.conf \
		--deploy-mode cluster \
		local:///opt/spark/work-dir/app.py

conda-env:
	conda env update -f env.yml
	source activate python3.7-spark && \
	python -m ipykernel install --user --name python3.7-spark


AWS_ACCESS_KEY_ID:=$(shell cat ../aws-access-key)
AWS_SECRET_ACCESS_KEY:=$(shell cat ../aws-secret-key)
pyspark-notebook:
	source activate python3.7-spark && \
	export AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) && \
	export AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY) && \
	PYSPARK_PYTHON=python3 PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS="notebook ." pyspark \
    	--master k8s://$(K8S_API_URL) \
		--properties-file ../spark.conf \