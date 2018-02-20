#Spark use-case22 Music dataset
# The data is loaded into HDFS using hadoop fs -mkdir and hdfs put comamnds##.
#This program reads the Data in json format ,  create RDD,datasets out of it and run SQL queries
from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Music datasets") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df = spark.read.json("In/reviews_Digital_Music_5.json")
df.printSchema()
df.createOrReplaceTempView("music")
sqlDF = spark.sql("SELECT summary,overall  FROM music WHERE overall = 5.0 LIMIT 10")
sqlDF.show()
