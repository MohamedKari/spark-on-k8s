import sys
from operator import add

import os

from pyspark.sql import SparkSession
import numpy as np

spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()

partitions = 5
n = 1000 * partitions

print("Doing n iterations: ", n)

def f(_):
    x = np.random.rand() * 2 - 1
    y = np.random.rand() * 2 - 1
    return 1 if x ** 2 + y ** 2 <= 1 else 0

count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)

pi_approx = 4.0 * count / n

print("Pi is roughly %f" % pi_approx)

print("Writing file to S3...")
spark \
    .createDataFrame([
        pi_approx
    ],
    "float") \
    .write \
    .mode("overwrite") \
    .csv(os.getenv("S3A_DATA_PATH"))

print("Wrote file to S3...")

print("Reading file from S3...")
lines = spark \
    .read \
    .text(os.getenv("S3A_DATA_PATH")) \
    .show()

print("Read file from S3!")

spark.stop()