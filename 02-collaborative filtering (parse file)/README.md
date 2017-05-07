PySpark for Collaborative Filtering
=========================

### Initial spark
```python
#conf = SparkConf().setAppName("sparkApp").setMaster("mesos://127.0.0.1:5050")
conf = SparkConf().setAppName("lucasSpark").setMaster("local")
self.sc = SparkContext(conf=conf)
self.sqlCtx = SQLContext(self.sc)
```

### Prepare train & test data
```python
trainingLIST =[ [0, 0, 4.0], [0, 1, 2.0], [1, 1, 3.0], [1, 2, 4.0], [2, 1, 1.0], [2, 2, 5.0] ]
testLIST = [ [0, 2], [1, 0], [2, 0] ]
```

### Prepare train & test data

Create dataFrame
```python
df = self.sqlCtx.createDataFrame(traingLIST, ["user", "item", "rating"])
test = self.sqlCtx.createDataFrame( testingLIST , ["user", "item"])
```

### Recommendation algorithms : 
calculate recommendating rating by "Alternating Least Squares"
```python
als = ALS(rank=10, maxIter=5, seed=0)
model = als.fit(df)

predictions = sorted(model.transform(test).collect(), key=lambda r: r[0])
```

### Show predictions
```python
for p in predictions:
  print p

```
```
Row(user=0, item=2, prediction=-0.13807615637779236)
Row(user=1, item=0, prediction=2.6258413791656494)
Row(user=2, item=0, prediction=-1.5018409490585327)
```

