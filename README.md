PySpark
==============================


## Install Apache Spark

### Download Apache Spark™


http://spark.apache.org/downloads.html

[http://spark.apache.org/downloads.html](http://spark.apache.org/downloads.html)

```
Choose a Spark release:  2.1.1 (May 02 2017)

Choose a package type:   Pre-built for Hadoop 2.7 and later 

Choose a download type:  Direct Download

Download Spark: spark-2.1.1-bin-hadoop2.7.tgz
```
	
### Settings of Spark

Extract all files from .tar 

```sh
tar zxvf spark-2.1.1-bin-hadoop2.7.tgz 
sudo mv ~/Downloads/spark-2.1.1-bin-hadoop2.7 /usr/local/spark-2.1.1
```

Set environment variable
```sh
vim ~/.bashrc
```

Add following into ~/.bashrc
```sh
export SPARK_HOME="/usr/local/spark-2.1.1"
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
```

reload environment variable
```sh
source ~/.bashrc
```


Details
========================
### Run Pyspark
Method-1 : run by python
```sh
python SparkEgine.py
```

Method-2 : submit code to mesos
(Please check mesos has been ran.)
```sh
./spark-submit --master mesos://127.0.0.1:5050 ~/Desktop/SparkEgine.py
```

