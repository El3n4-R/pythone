import json
import pandas as pd


infile = open("meteo.json", "r")
data = json.load(infile)
#print(dir(data)) 
print(data.keys())

print(type(data))
print(data["day1"])

#'date': '2019-11-6', 
# 'temperature_max': 14, 
# 'temperature_min': 8, 
# 'humidity': 56, 
giorni = [f"day{elem}" for elem in range(1, 8)]
print(giorni)
date_meteo = []
t_max = []
t_min = []
humi = []
for giorno in giorni:
    date_meteo.append(data[giorno]["date"])
    t_max.append(data[giorno]["temperature_max"])
    t_min.append(data[giorno]["temperature_min"])   
    humi.append(data[giorno]["humidity"])

import matplotlib.pyplot as plt

plt.fill_between(date_meteo, t_min, t_max, facecolor="green")
plt.title("escursione termica", fontsize=20)
plt.xlabel("date", fontsize=18)
plt.ylabel("temperature", fontsize=18)
plt.tick_params(axis="both", which="major", labelsize=12)
#plt.axis([0, 55, 0, 3600])
plt.show()
