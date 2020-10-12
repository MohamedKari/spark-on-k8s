This repo accompanies my blog post under https://blog.mkari.de/posts/spark-on-k8s.

```sh
git clone https://github.com/MohamedKari/spark-on-k8s && cd spark-on-k8s

echo $AWS_ACCESS_KEY_ID > aws-access-key
echo $AWS_SECRET_ACCESS_KEY > aws-secret-key

# Spin up a Minikube cluster
cd k8s && make

# Open a new terminal window to build and push the Spark Base image
# This will include a submit of th built-in PySpark Pi demo.
cd spark-base && make && cd ..

# Build and push a Spark app with custom dependencies that accesses AWS S3 and submit it to the cluster
cd spark-app && make && cd ..

# Spin up the Spark History server
cd spark-history-server && make

# Open a new new terminal window and run a notebook server on the cluster
cd spark-notebook && make 

# Once the notebook container is up and port-forwarding is established get the notebook URL
kubectl logs -f spark-notebook
```



conf = sc.getConf().getAll()
conf_dict = dict(conf)
conf_dict["spark.executor.instances"] = 12
conf_pairs = list(conf_dict.items())
conf_pairs
new_conf = SparkConf().setAll(conf_pairs)