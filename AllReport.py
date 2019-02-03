#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
#import matplotlib.pyplot as plt
import re
import numpy as np
import json

date_today = "03"
month_today = "01"
year_today = "2019"


# In[2]:


#temp
temp_df = pd.read_excel('./data/weather_historic.xls',  encoding = "utf-8")
temp_df = temp_df[["Local time in Pune","T", "U"]]
temp_df = temp_df.rename(columns = {"T": "Temp(deg Centigrade)", "U": "% Humidity"})
temp_df["Date"], temp_df["Daytime"] = temp_df["Local time in Pune"].str.split(' ', 1).str
tempGroupedDF = temp_df.groupby(['Date']).mean().reset_index()
tempGroupedDF["Day"], tempGroupedDF["Month"], tempGroupedDF["Year"] = tempGroupedDF["Date"].str.split('.').str
tempTodayDF = tempGroupedDF[(tempGroupedDF["Month"] == month_today) & (tempGroupedDF["Day"] == date_today)]
tempTodayDF = tempTodayDF.set_index("Year").drop('Day', 1).drop('Month', 1).drop('Date', 1)
if not tempTodayDF.empty:
    print("tempTodayDF available")
else:
    print("No tempTodayDF data available")
    
masterDF = tempTodayDF


# In[3]:


#pm2.5pm10
pmDF = pd.read_excel('./data/pm25pm10-parse.xlsx',  encoding = "utf-8")
pmDF["Date"], pmDF["Time"] = pmDF["Date"].str.split(' ', 1).str
pmDF = pmDF.replace('None', "NaN")
pmDF["PM2.5"] = pmDF["PM2.5"].astype(float)
pmDF["PM10"] = pmDF["PM10"].astype(float)
pmDF["Day"], pmDF["Month"], pmDF["Year"] = pmDF["Date"].str.split('.').str
pmTodayDF = pmDF[(pmDF["Month"] == month_today) & (pmDF["Day"] == date_today)]
pmTodayDF = pmTodayDF.set_index("Year").drop('Day', 1).drop('Month', 1).drop('Date', 1)
if not pmTodayDF.empty:
    print("pmTodayDF.plot()")
    masterDF = pd.merge(masterDF, pmTodayDF, how = "left", left_on = "Year", right_on = "Year")
else:
    print("No pm data available")
    


# In[4]:


#ozoneNoxSo2
ozoneDF = pd.read_excel('./data/ozone-nox-so2-parsed.xlsx',  encoding = "utf-8")
ozoneDF["Date"], ozoneDF["Time"] = ozoneDF["Date"].str.split(' ', 1).str
ozoneDF["Day"], ozoneDF["Month"], ozoneDF["Year"] = ozoneDF["Date"].str.split('-').str
ozoneDF = ozoneDF.replace('None', "NaN")
ozoneDF["Ozone"] = ozoneDF["Ozone"].astype(float)
ozoneDF["NOx"] = ozoneDF["NOx"].astype(float)
ozoneDF["SO2"] = ozoneDF["SO2"].astype(float)
ozoneTodayDF = ozoneDF[(ozoneDF["Month"] == month_today) & (ozoneDF["Day"] == date_today)]
ozoneTodayDF = ozoneTodayDF.set_index('Year').drop('Day', 1).drop('Month', 1).drop('Date', 1).drop('Time', 1)
if not ozoneTodayDF.empty:
    print("ozoneTodayDF.plot()")
    masterDF = pd.merge(masterDF, ozoneTodayDF, how = "left", left_on = "Year", right_on = "Year")
else:
    print("No ozone, so2, nox data available")



# In[5]:


#vehicle
vehicleDF = pd.read_excel('./data/Vehicle2006-2016.xls',  encoding = "utf-8")
vehicleDF = vehicleDF.rename(columns = lambda x: re.sub('-','',x))
vehicleDF = vehicleDF.tail(1)
vehicleDF = vehicleDF.drop('Vehicles', 1)
vehicleDF = vehicleDF.T
vehicleDF = vehicleDF.reset_index()
vehicleDF.columns = ["Year", "Total Vehicles"]
vehicleDF.set_index("Year")
if not vehicleDF.empty:
    print(" vehicleDF.plot()")
    masterDF = pd.merge(masterDF, vehicleDF, how = "left", left_on = "Year", right_on = "Year")
else:
    print("No vehicle data available")




# In[6]:


#tree cover
treeDF = pd.read_excel('./data/tree_cover/TreeCoverPune2009-2017.xls',  encoding = "utf-8")
treeDF["Year"] = treeDF["Year"].astype(str)
treeDF = treeDF.set_index("Year")

if not treeDF.empty:
    print(" treeDF.plot()")
    masterDF = pd.merge(masterDF, treeDF, how = "left", left_on = "Year", right_on = "Year")
else:
    print("No tree cover data available")



# In[7]:


#water table
watertableDF = pd.read_csv('./data/ground_water/PuneWaterTable2009-2018.csv',  encoding = "utf-8")
watertableDF = watertableDF[["WLCODE", "YEAR_OBS", "August(MONSOON)"]]
watertableDF["YEAR_OBS"] = watertableDF["YEAR_OBS"].astype(str)
watertableDF = watertableDF.groupby(['YEAR_OBS']).max().drop("WLCODE", 1)

if not watertableDF.empty:
    print(" watertableDF.plot()")
    masterDF = pd.merge(masterDF, watertableDF, how = "left", left_on = "Year", right_on = "YEAR_OBS")
else:
    print("No water table data available")



# In[8]:


#population
populationDF = pd.read_excel('./data/population_data.xls',  encoding = "utf-8")
populationDF["Date"] = populationDF["Date"].astype(str)
populationDF = populationDF.set_index("Date")

if not populationDF.empty:
    print(" populationDF.plot()")
    masterDF = pd.merge(masterDF, populationDF, how = "left", left_on = "Year", right_on = "Date")
else:
    print("No population data available")



# In[47]:


# dataframe to map conversion

def get_populated_map():
    temp_map = dict()
    for i in range(0, len(masterDF.columns)):
        colname = masterDF.columns[i]
        arr = masterDF[colname].values.tolist()
        temp_map[colname] = arr
        
    return temp_map


# In[ ]:




