from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

class SparkEgine():
 sc = None
 sqlCtx = None
 def __init__(self) :

  #conf = SparkConf().setAppName("sparkApp").setMaster("mesos://127.0.0.1:5050")
  conf = SparkConf().setAppName("lucasSpark").setMaster("local")
  self.sc = SparkContext(conf=conf)
  self.sqlCtx = SQLContext(self.sc)

 def CF(self , path ):

  # Load and parse the data
  data = self.sc.textFile( path )
  ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

  #df = self.sqlCtx.createDataFrame(traingLIST, ["user", "item", "rating"])
  als = ALS(rank=10, maxIter=5, seed=0)
  model = als.fit(traingLIST)  # pyspark.ml.recommendation.ALSModel
  #print model.rank
  #print model.userFactors.orderBy("id").collect()

  test = self.sqlCtx.createDataFrame( testingLIST , ["user", "item"])
  predictions = sorted(model.transform(test).collect(), key=lambda r: r[0])

  self.sqlCtx.stop()

  return predictions


if __name__ == '__main__':
  spark = SparkEgine()

  # userid
  # movieid
  # rating

  path = "./test.data"
  resultLIST = spark.CF( path )
  
  for p in predictions:
   print p














