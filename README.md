PySpark
==============================

### Download Apache Spark™

	Choose a Spark release:  2.1.1 (May 02 2017)

	Choose a package type:   Pre-built for Hadoop 2.7 and later 

	Choose a download type:  Direct Download

	Download Spark: spark-2.1.1-bin-hadoop2.7.tgz
	
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
add following into ~/.bashrc
```sh
	export SPARK_HOME="/usr/local/spark-2.1.1"
	export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
```
reload environment variable

```sh
	source ~/.bashrc
```
