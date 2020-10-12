include .env
export

spark.conf: spark.template.conf
	cat spark.template.conf |envsubst > spark.conf