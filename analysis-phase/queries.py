from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("project2") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

path = "file:/mnt/c/Users/jan94/OneDrive/Desktop/Work/proj2/rev-proj2/analysis-phase/" # MODIFY PATH IF YOU USE THIS ON YOUR MACHINE

team3data_raw = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(path + "p2_Team3_Data_copy.csv")

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

# spark.sql("SELECT ProductCategory, SUM(Qty) AS Sales FROM team3data \
#                     GROUP BY ProductCategory ORDER BY Sales DESC").show()

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

'''
# clothesByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='Clothes' GROUP BY day, ProductID ORDER BY day, ProductID")
# furnitureByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='Furniture' GROUP BY day, ProductID ORDER BY day, ProductID")
# schoolItemsByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='School Items' GROUP BY day, ProductID ORDER BY day, ProductID")
# technologyByDay = spark.sql("SELECT ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='Technology' GROUP BY day, ProductID ORDER BY day, ProductID")

# clothesByDay.show()
# furnitureByDay.show()
# schoolItemsByDay.show()
# technologyByDay.show()

# clothesByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='Clothes' GROUP BY day ORDER BY day")
# furnitureByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='Furniture' GROUP BY day ORDER BY day")
# schoolItemsByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='School Items' GROUP BY day ORDER BY day")
# technologyByDayTotal = spark.sql("SELECT SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
#                     WHERE ProductCategory='Technology' GROUP BY day ORDER BY day")

# clothesByDayTotal.show()
# furnitureByDayTotal.show()
# schoolItemsByDayTotal.show()
# technologyByDayTotal.show()

#####

totalRevenue.write.csv(path + "output/totalRevenue")
totalSales.write.csv(path + "output/totalSales")

country_revenue.write.csv(path + "output/country_revenue")
country_sales.write.csv(path + "output/country_sales")

topRevByCountry.write.csv(path + "output/topRevByCountry")
topSalesByCountry.write.csv(path + "output/topSalesByCountry")

revenueByQuarter.write.csv(path + "output/revenueByQuarter")
salesByQuarter.write.csv(path + "output/salesByQuarter")

clothesByDay.write.csv(path + "output/clothesByDay")
furnitureByDay.write.csv(path + "output/furnitureByDay")
schoolItemsByDay.write.csv(path + "output/schoolItemsByDay")
technologyByDay.write.csv(path + "output/technologyByDay")

clothesByDayTotal.write.csv(path + "output/clothesByDayTotal")
furnitureByDayTotal.write.csv(path + "output/furnitureByDayTotal")
schoolItemsByDayTotal.write.csv(path + "output/schoolItemsByDayTotal")
technologyByDayTotal.write.csv(path + "output/technologyByDayTotal")
'''

# TODO: - --DONE-- QUERY sales by day per country --DONE--
#       - query sales traffic per country
#       - query sales traffic per city
#       - query sales traffic by time
#       - query sales traffic by time per country

'''
clothesByDayPerCountry = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Clothes' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country")
furnitureByDayPerCountry = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Furniture' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country")
schoolItemsByDayPerCountry = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='School Items' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country")
technologyByDayPerCountry = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Technology' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country")

# clothesByDayPerCountry.show(100)
# furnitureByDayPerCountry.show(100)
# schoolItemsByDayPerCountry.show(100)
# technologyByDayPerCountry.show(100)

clothesByDayTotalPerCountry = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Clothes' GROUP BY Country, day ORDER BY day, Country")
furnitureByDayTotalPerCountry = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Furniture' GROUP BY Country, day ORDER BY day, Country")
schoolItemsByDayTotalPerCountry = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='School Items' GROUP BY Country, day ORDER BY day, Country")
technologyByDayTotalPerCountry = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Technology' GROUP BY Country, day ORDER BY day, Country")

# clothesByDayTotalPerCountry.show(100)
# furnitureByDayTotalPerCountry.show(100)
# schoolItemsByDayTotalPerCountry.show(100)
# technologyByDayTotalPerCountry.show(100)


clothesByDayPerCountry.write.csv(path + "output/clothesByDayPerCountry")
furnitureByDayPerCountry.write.csv(path + "output/furnitureByDayPerCountry")
schoolItemsByDayPerCountry.write.csv(path + "output/schoolItemsByDayPerCountry")
technologyByDayPerCountry.write.csv(path + "output/technologyByDayPerCountry")

clothesByDayTotalPerCountry.write.csv(path + "output/clothesByDayTotalPerCountry")
furnitureByDayTotalPerCountry.write.csv(path + "output/furnitureByDayTotalPerCountry")
schoolItemsByDayTotalPerCountry.write.csv(path + "output/schoolItemsByDayTotalPerCountry")
technologyByDayTotalPerCountry.write.csv(path + "output/technologyByDayTotalPerCountry")

'''

df1 = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Clothes' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country") # sales traffic per country
df2 = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Furniture' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country") # sales traffic per city 
df3 = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='School Items' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country") # sales traffic by time
df4 = spark.sql("SELECT Country, ProductID, First(ProductName), SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Technology' GROUP BY Country, day, ProductID ORDER BY day, ProductID, Country") # sales traffic by time per country

# df1.show(100)
# df2.show(100)
# df3.show(100)
# df4.show(100)

df5 = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Clothes' GROUP BY Country, day ORDER BY day, Country") # ItemRevenuePerQuarter
df6 = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Furniture' GROUP BY Country, day ORDER BY day, Country") # ItemSalesPerQuarter
df7 = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='School Items' GROUP BY Country, day ORDER BY day, Country") #ItemPopularityPerQuarter
df8 = spark.sql("SELECT Country, SUM(Qty) AS Sales, dayofyear(Datetime) AS day FROM team3data \
                    WHERE ProductCategory='Technology' GROUP BY Country, day ORDER BY day, Country") # ?????

# df5.show(100)
# df6.show(100)
# df7.show(100)
# df8.show(100)

'''
df1.write.csv(path + "output/df1")
df2.write.csv(path + "output/df2")
df3.write.csv(path + "output/df3")
df4.write.csv(path + "output/df4")

df5.write.csv(path + "output/df5")
df6.write.csv(path + "output/df6")
df7.write.csv(path + "output/df7")
df8.write.csv(path + "output/df8")
'''
# spark.sql("SELECT ProductID, ProductName, Qty, Price FROM team3data ORDER BY ProductID").show(250)

# spark.sql("SELECT ProductID, ProductName, Qty, Price FROM team3data ORDER BY ProductID").show(250)

spark.stop()

print("Complete!")