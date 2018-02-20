# Project-Team-17
Use case is below

   -  Data Set used http://jmcauley.ucsd.edu/data/amazon/ (contact the owner for data link..) . The data sets have  below coloumns 
  
     |-- asin: string (nullable = true)
      |-- helpful: array (nullable = true)
      |    |-- element: long (containsNull = true)
       |-- overall: double (nullable = true)
     |-- reviewText: string (nullable = true)
     |-- reviewTime: string (nullable = true)
     |-- reviewerID: string (nullable = true)
      |-- reviewerName: string (nullable = true)
     |-- summary: string (nullable = true)
     |-- unixReviewTime: long (nullable = true)

 We uploaded the books dataset into the Jupyter Notebook. Using spark , we have found the top ten songs using the values in coloumn "overall".
 ![ScreenShot](https://github.com/SJSU272LabSP18/Project-Team-17/blob/master/Screen%20Shot%202018-02-20%20at%202.45.43%20PM.png)
