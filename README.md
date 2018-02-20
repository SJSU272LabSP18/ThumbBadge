# Project-Team-17
Use case is below

   -  Use Music reviews data http://jmcauley.ucsd.edu/data/amazon/ (contact the owner for data link..) and use spark to find the top ten songs or something

For this one we created the  hadoop cluster , and added the datasets to that cluster using spark

Data is in json format named "reviews_Digital_Music_5.json" which is feeded in hdfs and then python prog musicds.py extract and display the required result i.e  top ten songs  
To run:
   - PYSPARK_PYTHON=/home/common/conda/anaconda2/bin/python spark-submit   --master yarn --deploy-mode cluster  musicds.py

To run locally i.e o/p on console:
   - PYSPARK_PYTHON=/home/common/conda/anaconda2/bin/python spark-submit   --master local   musicds.py
