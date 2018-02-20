''' Spark use-case22 Music dataset
Use Music reviews data http://jmcauley.ucsd.edu/data/amazon/ and use spark to find the top ten songs
For this one we created the  hadoop cluster , and added the datasets to that cluster using spark
The data is loaded into HDFS using hadoop fs -mkdir and hdfs cp comamnds 
resides under dir named IN under hdfs i.e IN/reviews_Digital_Music_5.json.
This program reads the Data in json format ,  create RDD,datasets out of it 
Data is in json format named "reviews_Digital_Music_5.json" which is feeded in hdfs 
python prog musicds.py extract and display the required result i.e  top ten songs

To run:
   - PYSPARK_PYTHON=/home/common/conda/anaconda2/bin/python \ 
     spark-submit \   
     --master yarn \
     --deploy-mode cluster \
      musicds.py

To run locally i.e o/p on console:
   - PYSPARK_PYTHON=/home/common/conda/anaconda2/bin/python \ 
     spark-submit \
     --master local \ 
      musicds.py'''


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
