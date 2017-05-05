from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext


conf = SparkConf().setAppName("lucasSpark").setMaster("local")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)

df = sqlCtx.createDataFrame([(0, 0, 4.0), (0, 1, 2.0), (1, 1, 3.0), (1, 2, 4.0), (2, 1, 1.0), (2, 2, 5.0)],["user", "item", "rating"])
als = ALS(rank=10, maxIter=5, seed=0)
model = als.fit(df) # pyspark.ml.recommendation.ALSModel
print model.rank

print model.userFactors.orderBy("id").collect()
test = sqlCtx.createDataFrame([(0, 2), (1, 0), (2, 0)], ["user", "item"])
predictions = sorted(model.transform(test).collect(), key=lambda r: r[0])

for p in predictions :
 print p



