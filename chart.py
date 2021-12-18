import pandas as pd
import csv 
import matplotlib.pyplot as plt

df = pd.read_csv("star_with_gravity.csv")
df.head()
df.drop(["Unnamed: 0"],axis = 1,inplace = True)
name = df["Star_name"].to_list()
distance = df["Distance"].to_list()
Mass = df["Mass"].to_list()
Radius = df["Radius"].to_list()
Gravity = df["Gravity"].to_list()
barWidth = 0.25
plt.figure(figsize=(10,5))
plt.title("Gravity Data")
plt.bar(name[0:9],Mass[0:9] ,width=barWidth)
plt.bar(distance[0:9],Radius[0:9] ,width=barWidth)
plt.show()