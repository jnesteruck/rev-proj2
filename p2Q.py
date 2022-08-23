import findspark
findspark.init()
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .master("local") \
    .appName("project2") \
    .getOrCreate()
    
sc = spark.sparkContext
sc.setLogLevel("WARN")

path = "file:/mnt/c/Users/keyno/Desktop/rev-proj2/analysis-phase/"
team3data_raw = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(path + "p2_Team3_Data_copy.csv")
    
team3data_raw.createOrReplaceTempView("team3data_raw")
team3data = spark.sql("SELECT * FROM team3data_raw WHERE TransactionSuccess='Y' OR TransactionSuccess='N'")
team3data.createOrReplaceTempView("team3data")

trafficbyhour = spark.sql("SELECT SUM(Qty) AS Sales, hour(Datetime) AS Hour FROM team3data \
    WHERE TransactionSuccess = 'Y' GROUP BY Hour ORDER BY Sales desc, Hour")
trafficbycountry = spark.sql("SELECT SUM(Qty) AS Sales, Country, hour(Datetime) as Hour FROM team3data \
    WHERE TransactionSuccess = 'Y' GROUP BY Country, Hour ORDER BY Sales desc, Country")



trafficbyhour.show()
trafficbycountry.show()
# WRITES QUERIES TO CSV 
trafficbyhour.write.csv(path + "/output/TrafficByHour")
trafficbycountry.write.csv(path + "/output/TrafficByCountry")

spark.stop()
print("Complete!")