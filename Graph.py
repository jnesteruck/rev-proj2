import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(columns=["Sales","Hour(Military Time)"])
df2 = pd.DataFrame([[4978, 11],[4948, 18],[4928, 18],[4928, 15], [4895, 17], [4842, 8],[4767, 19], [4753, 10], [4730, 16], [4615, 13], [4605, 20], [4602, 14], [4525, 12], [4303, 9]], columns=["Sales", "Hour(Military Time)"])
df.append(df2)
df2.head()

df2.sort_index(axis=0, ascending=True, inplace=True)
graph = df2.plot(x= "Hour(Military Time)", y="Sales", kind="bar")

graph.figure.savefig("SalesTrafficByHour")

