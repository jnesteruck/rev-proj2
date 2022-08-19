from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("project2") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

path = "file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/p2_Team3_Data_copy.csv"

team3data_raw = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(path)

# team3data.show(10)
# team3data.printSchema()

team3data_raw.createOrReplaceTempView("team3data_raw")
team3data = spark.sql("SELECT * FROM team3data_raw WHERE TransactionSuccess='Y' OR TransactionSuccess='N'")
team3data.createOrReplaceTempView("team3data")

# team3data.printSchema()

# spark.sql("SELECT * FROM team3data").show(10)

totalRevenue = spark.sql("SELECT ProductCategory, SUM(Price * Qty) AS Revenue FROM team3data \
                    WHERE TransactionSuccess='Y' GROUP BY ProductCategory ORDER BY Revenue DESC")
totalSales = spark.sql("SELECT ProductCategory, SUM(Qty) AS Sales FROM team3data \
                    WHERE TransactionSuccess='Y' GROUP BY ProductCategory ORDER BY Sales DESC")

totalSales.show()

spark.sql("SELECT ProductCategory, SUM(Qty) AS Sales FROM team3data \
                    GROUP BY ProductCategory ORDER BY Sales DESC").show()

country_revenue = spark.sql("SELECT Country, ProductCategory, SUM(Price * Qty) AS Revenue FROM team3data \
                    WHERE TransactionSuccess='Y' GROUP BY Country, ProductCategory ORDER BY Country, Revenue DESC")
country_sales = spark.sql("SELECT Country, ProductCategory, SUM(Qty) AS Sales FROM team3data \
                    WHERE TransactionSuccess='Y' GROUP BY Country, ProductCategory ORDER BY Country, Sales DESC")

totalRevenue.createOrReplaceTempView("totalRevenue")
totalSales.createOrReplaceTempView("totalSales")

country_revenue.createOrReplaceTempView("country_revenue")
country_sales.createOrReplaceTempView("country_sales")

topRevByCountry = spark.sql("SELECT Country, First(ProductCategory), MAX(Revenue) FROM country_revenue GROUP BY Country")
topSalesByCountry = spark.sql("SELECT Country, First(ProductCategory), MAX(Sales) FROM country_sales GROUP BY Country")

# totalRevenue.show()

revenueByQuarter = spark.sql("SELECT quarter(Datetime) AS Quarter, ProductCategory, SUM(Price * Qty) AS Revenue FROM team3data \
                    GROUP BY Quarter, ProductCategory ORDER BY Quarter, Revenue DESC")
revenueByQuarter.createOrReplaceTempView("revenueByQuarter")

# spark.sql("SELECT quarter(Datetime) AS Quarter, ProductCategory, SUM(Price * Qty) AS Revenue FROM team3data GROUP BY Quarter, ProductCategory ORDER BY Quarter, Revenue DESC").show()

# totalSales.show()

salesByQuarter = spark.sql("SELECT quarter(Datetime) AS Quarter, ProductCategory, SUM(Qty) AS Sales FROM team3data \
                    GROUP BY Quarter, ProductCategory ORDER BY Quarter, Sales DESC")
salesByQuarter.createOrReplaceTempView("salesByQuarter")

# spark.sql("SELECT quarter(Datetime) AS Quarter, ProductCategory, SUM(Qty) AS Sales FROM team3data GROUP BY Quarter, ProductCategory ORDER BY Quarter, Sales DESC").show()

clothesByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Clothes' GROUP BY day, ProductID ORDER BY day, ProductID")
furnitureByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Furniture' GROUP BY day, ProductID ORDER BY day, ProductID")
schoolItemsByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='School Items' GROUP BY day, ProductID ORDER BY day, ProductID")
technologyByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Technology' GROUP BY day, ProductID ORDER BY day, ProductID")

# clothesByDay.show()
# furnitureByDay.show()
# schoolItemsByDay.show()
# technologyByDay.show()

clothesByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Clothes' GROUP BY day ORDER BY day")
furnitureByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Furniture' GROUP BY day ORDER BY day")
schoolItemsByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='School Items' GROUP BY day ORDER BY day")
technologyByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Technology' GROUP BY day ORDER BY day")

# clothesByDayTotal.show()
# furnitureByDayTotal.show()
# schoolItemsByDayTotal.show()
# technologyByDayTotal.show()

'''
totalRevenue.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/totalRevenue")
totalSales.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/totalSales")

country_revenue.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/country_revenue")
country_sales.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/country_sales")

topRevByCountry.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/topRevByCountry")
topSalesByCountry.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/topSalesByCountry")

revenueByQuarter.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/revenueByQuarter")
salesByQuarter.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/salesByQuarter")

clothesByDay.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/clothesByDay")
furnitureByDay.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/furnitureByDay")
schoolItemsByDay.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/schoolItemsByDay")
technologyByDay.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/technologyByDay")

clothesByDayTotal.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/clothesByDayTotal")
furnitureByDayTotal.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/furnitureByDayTotal")
schoolItemsByDayTotal.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/schoolItemsByDayTotal")
technologyByDayTotal.write.csv("file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/output/technologyByDayTotal")
'''

# TODO: - QUERY sales by day per country
#       - query sales traffic per country
#       - query sales traffic per city
#       - query sales traffic by time
#       - query sales traffic by time per country

# spark.sql("SELECT ProductID, ProductName, Qty, Price FROM team3data ORDER BY ProductID").show(250)

# spark.sql("SELECT ProductID, ProductName, Qty, Price FROM team3data ORDER BY ProductID").show(250)

spark.stop()

print("Complete!")