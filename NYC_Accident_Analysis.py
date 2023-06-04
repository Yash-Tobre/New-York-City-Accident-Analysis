# -*- coding: utf-8 -*-
"""Final Project 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AWhxv42UQlyYs3CY6pZ9AryzYjHAHwFk
"""

from google.colab import drive
drive.mount('/content/drive')
#importing the data

import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import seaborn

def Name_Cleaner(vehicle_name):
  if re.search('-/*', vehicle_name): #this confirms that re.search returns something, meaning it will only proceed if the given symbols are encountered in the string.
    pos = re.search('-/*', vehicle_name).start() #the start method here returns the index position at which the pattern or symnol in this case is encountered.
    return vehicle_name[:pos] #this will RETURN the vehicle name by the remaining strings except this pattern.
  else:
    return vehicle_name #this will return the original name if the pattern is not encountered.

path= "/content/drive/MyDrive/Motor_Vehicle_Collisions_-_Vehicles (1).csv"
org_data = pd.read_csv(path)

org_data_copy= org_data

org_data_copy

org_data['CRASH_DATE']=pd.to_datetime(org_data['CRASH_DATE'])

start_date= '2019-09-01'
end_date='2021-08-31'

daterange=org_data.query('CRASH_DATE>= @start_date and CRASH_DATE<=@end_date')
daterange.to_csv('/content/drive/MyDrive/daterange.csv')

data_to_use=pd.read_csv('/content/drive/MyDrive/daterange.csv')
#to read

data_to_use['CRASH_DATE']=pd.to_datetime(data_to_use['CRASH_DATE'])
data_to_use['YEAR'],data_to_use['MONTH']=data_to_use['CRASH_DATE'].dt.year,data_to_use['CRASH_DATE'].dt.month
#this would create two additional columns of date and month

data_to_use

data1=data_to_use
data1=data1.dropna(subset=['VEHICLE_MAKE'])

data1

data1.isna().sum()

data1['VEHICLE_MAKE']= data1['VEHICLE_MAKE'].apply(Name_Cleaner)

data1

print(data1.columns.get_loc('VEHICLE_MAKE'))
print(data1.columns.get_loc('YEAR'))
print(data1.columns.get_loc('MONTH'))

cols=[8,26,27]
Data=data1[data1.columns[cols]]

Data

"""Query-1 Bar Chart"""

Data['VEHICLE_MAKE']=Data['VEHICLE_MAKE'].str.replace(' ','')
Data['YEAR']=Data['YEAR'].replace(' ','')

mydata=Data[(Data['VEHICLE_MAKE'] == 'NISS') | (Data['VEHICLE_MAKE'] == 'SUBA')|(Data['VEHICLE_MAKE'] == 'BMW')|(Data['VEHICLE_MAKE'] == 'AUDI')]

mydata

mydata.insert(1,'counter','1')

mydata

mydata.groupby(['VEHICLE_MAKE','YEAR'])[['counter']].count()

X = ['BMW','NISS','SUBA','AUDI']
y_2019=[4096,12599,1883,1440]
y_2020=[7630,20339,2875,2345]
y_2021=[5312,12264,1784,1590]

X_axis=np.arange(len(X))

plt.bar(X_axis - 0.2,  y_2019, 0.2, 
	label = '2019')
plt.bar(X_axis ,  y_2020, 0.2, 
	label = '2020')
plt.bar(X_axis+0.2,y_2021,0.2,
        label='2021')
  
plt.xticks(X_axis, X)
plt.xlabel("Vehicle Make")
plt.ylabel("count")
plt.title("Query 1")
plt.legend()
plt.show()

"""Query-2 Line Chart"""

data_to_use=pd.read_csv('/content/drive/MyDrive/daterange.csv')

print(data_to_use)

data_to_use=data_to_use.dropna(subset=['VEHICLE_MAKE'])

data_to_use['VEHICLE_MAKE']= data_to_use['VEHICLE_MAKE'].apply(Name_Cleaner)

data_to_use

data_to_use['CRASH_DATE']=pd.to_datetime(data_to_use['CRASH_DATE'])
data_to_use['YEAR'],data_to_use['MONTH']=data_to_use['CRASH_DATE'].dt.year,data_to_use['CRASH_DATE'].dt.month
#this would create two additional columns of date and month

print(data_to_use.columns.get_loc('VEHICLE_MAKE'))
print(data_to_use.columns.get_loc('MONTH'))
print(data_to_use.columns.get_loc('YEAR'))

cols2=[8,27,26]
q_2=data_to_use[data_to_use.columns[cols2]]

q_2

q_2['VEHICLE_MAKE']=q_2['VEHICLE_MAKE'].str.replace(' ','')
q_2['YEAR']=q_2['YEAR'].replace(' ','')
q_2['MONTH']=q_2['MONTH'].replace(' ','')

q_2['MONTH']=q_2['MONTH'].replace(1,'Jan')
q_2['MONTH']=q_2['MONTH'].replace(2,'Feb')
q_2['MONTH']=q_2['MONTH'].replace(3,'Mar')
q_2['MONTH']=q_2['MONTH'].replace(4,'Apr')
q_2['MONTH']=q_2['MONTH'].replace(5,'May')
q_2['MONTH']=q_2['MONTH'].replace(6,'Jun')
q_2['MONTH']=q_2['MONTH'].replace(7,'Jul')
q_2['MONTH']=q_2['MONTH'].replace(8,'Aug')
q_2['MONTH']=q_2['MONTH'].replace(9,'Sept')
q_2['MONTH']=q_2['MONTH'].replace(10,'Oct')
q_2['MONTH']=q_2['MONTH'].replace(11,'Nov')
q_2['MONTH']=q_2['MONTH'].replace(12,'Dec')

q_2

q_2=q_2[(q_2['VEHICLE_MAKE'] == 'NISS') | (q_2['VEHICLE_MAKE'] == 'SUBA')|(q_2['VEHICLE_MAKE'] == 'BMW')|(q_2['VEHICLE_MAKE'] == 'AUDI')]

n = len(pd.unique(q_2['MONTH']))
print(n)

q_2_2019_BMW=q_2[(q_2['YEAR']== 2019) & (q_2['VEHICLE_MAKE']=='BMW')]
q_2_2019_NISS=q_2[(q_2['YEAR']==2019)&(q_2['VEHICLE_MAKE']=='NISS')]
q_2_2019_AUDI=q_2[(q_2['YEAR']==2019)&(q_2['VEHICLE_MAKE']=='AUDI')]
q_2_2019_SUBA=q_2[(q_2['YEAR']==2019)&(q_2['VEHICLE_MAKE']=='SUBA')]

q_2_2020_BMW=q_2[(q_2['YEAR']== 2020) & (q_2['VEHICLE_MAKE']=='BMW')]
q_2_2020_NISS=q_2[(q_2['YEAR']== 2020) & (q_2['VEHICLE_MAKE']=='NISS')]
q_2_2020_AUDI=q_2[(q_2['YEAR']== 2020) & (q_2['VEHICLE_MAKE']=='AUDI')]
q_2_2020_SUBA=q_2[(q_2['YEAR']== 2020) & (q_2['VEHICLE_MAKE']=='SUBA')]

q_2_2021_BMW=q_2[(q_2['YEAR']== 2021) & (q_2['VEHICLE_MAKE']=='BMW')]
q_2_2021_NISS=q_2[(q_2['YEAR']== 2021) & (q_2['VEHICLE_MAKE']=='NISS')]
q_2_2021_AUDI=q_2[(q_2['YEAR']== 2021) & (q_2['VEHICLE_MAKE']=='AUDI')]
q_2_2021_SUBA=q_2[(q_2['YEAR']== 2021) & (q_2['VEHICLE_MAKE']=='SUBA')]

q_2_2020_BMW.insert(3,'count',1)
q_2_2020_NISS.insert(3,'count',1)
q_2_2020_AUDI.insert(3,'count',1)
q_2_2020_SUBA.insert(3,'count',1)

q_2_2021_BMW.insert(3,'count',1)
q_2_2021_NISS.insert(3,'count',1)
q_2_2021_AUDI.insert(3,'count',1)
q_2_2021_SUBA.insert(3,'count',1)

q_2_2019_BMW.insert(3,'count',1)
q_2_2019_NISS.insert(3,'count',1)
q_2_2019_AUDI.insert(3,'count',1)
q_2_2019_SUBA.insert(3,'count',1)

print(q_2_2020_BMW,q_2_2020_NISS,q_2_2020_AUDI,q_2_2020_SUBA)

print(q_2_2021_BMW,q_2_2021_NISS,q_2_2021_AUDI,q_2_2021_SUBA)

n1 = len(pd.unique(q_2_2019_BMW['MONTH']))
n2= len(pd.unique(q_2_2019_NISS['MONTH']))
n3= len(pd.unique(q_2_2019_AUDI['MONTH']))
n4= len(pd.unique(q_2_2019_SUBA['MONTH']))
print(n1,n2,n3,n4)

m1 = len(pd.unique(q_2_2020_BMW['MONTH']))
m2= len(pd.unique(q_2_2020_NISS['MONTH']))
m3= len(pd.unique(q_2_2020_AUDI['MONTH']))
m4= len(pd.unique(q_2_2020_SUBA['MONTH']))
print(m1,m2,m3,m4)

l1 = len(pd.unique(q_2_2021_BMW['MONTH']))
l2= len(pd.unique(q_2_2021_NISS['MONTH']))
l3= len(pd.unique(q_2_2021_AUDI['MONTH']))
l4= len(pd.unique(q_2_2021_SUBA['MONTH']))
print(l1,l2,l3,l4)

q21=q_2_2019_BMW.groupby(['MONTH'])[['count']].count()

q31=q_2_2020_BMW.groupby(['MONTH'])[['count']].count()
q32=q_2_2020_NISS.groupby(['MONTH'])[['count']].count()
q33=q_2_2020_AUDI.groupby(['MONTH'])[['count']].count()
q34=q_2_2020_SUBA.groupby(['MONTH'])[['count']].count()

q41=q_2_2021_BMW.groupby(['MONTH'])[['count']].count()
q42=q_2_2021_NISS.groupby(['MONTH'])[['count']].count()
q43=q_2_2021_AUDI.groupby(['MONTH'])[['count']].count()
q44=q_2_2021_SUBA.groupby(['MONTH'])[['count']].count()

q22=q_2_2019_NISS.groupby(['MONTH'])[['count']].count()
q23=q_2_2019_AUDI.groupby(['MONTH'])[['count']].count()
q24=q_2_2019_SUBA.groupby(['MONTH'])[['count']].count()

print(q21)
print(q22)
print(q23)
print(q24)

print(q31)
print(q32)
print(q33)
print(q34)

print(q41)
print(q42)
print(q43)
print(q44)

q21.insert(1,'CountNiss',q22['count'])
q21.insert(2,'CountAudi',q23['count'])
q21.insert(3,'CountSuba',q24['count'])

q31.insert(1,'CountNiss',q32['count'])
q31.insert(2,'CountAudi',q33['count'])
q31.insert(3,'CountSuba',q34['count'])

q41.insert(1,'CountNiss',q42['count'])
q41.insert(2,'CountAudi',q43['count'])
q41.insert(3,'CountSuba',q44['count'])

month_dict = {'Jan':1,'Feb':2,'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sept':9, 'Oct':10, 'Nov':11, 'Dec':12}

q21.rename(columns={'count':'CountBMW'}, inplace=True)
q21=q21.sort_values('MONTH', key = lambda x : x.apply (lambda x : month_dict[x]))

q31.rename(columns={'count':'CountBMW'},inplace=True)

q31=q31.sort_values('MONTH', key = lambda x : x.apply (lambda x : month_dict[x]))

q41.rename(columns={'count':'CountBMW'},inplace=True)

q41=q41.sort_values('MONTH', key = lambda x : x.apply (lambda x : month_dict[x]))

q41

from matplotlib import rcParams
rcParams['figure.figsize']=8,8
q21.plot(kind='line')

q31.plot()

q41.plot()

"""Query 3: PIECHART"""

path= "/content/drive/MyDrive/Motor_Vehicle_Collisions_-_Vehicles (1).csv"
org_data = pd.read_csv(path)

data_dt= org_data

org_data

data_dt['CRASH_DATE']=pd.to_datetime(data_dt['CRASH_DATE'])

start_date= '2019-09-01'
end_date='2021-08-31'

mvc_data=data_dt.query('CRASH_DATE>= @start_date and CRASH_DATE<=@end_date')
mvc_data.to_csv('/content/drive/MyDrive/MVC_3.csv')

new_data=pd.read_csv('/content/drive/MyDrive/MVC_3.csv')

new_data

new_data['VEHICLE_TYPE']=new_data['VEHICLE_TYPE'].str.replace(' ','')

new_data

new_data = pd.read_csv('/content/drive/MyDrive/MVC_3.csv')
print(new_data)

# Create new pandas DataFrame.
new_data = new_data[['VEHICLE_TYPE']]

XYZ=list(new_data['VEHICLE_TYPE'].unique())

for i in XYZ:
  print(i)

new_data.value_counts()

new_data=new_data.dropna(subset=['VEHICLE_TYPE'])

new_data['VEHICLE_TYPE'] = new_data['VEHICLE_TYPE'].str.upper()

print(new_data)

new_data = new_data[new_data['VEHICLE_TYPE'].str.contains('(SEDAN|PASSENGER|SPORT|STATION|TAXI|VAN|BUS|BIKE|TRUCK|MOTORCYCLE|BICYCLE)', regex=True)]

print(new_data)

print(new_data['VEHICLE_TYPE'].unique())

new_data["VEHICLE_TYPE"].replace({"4 DR SEDAN": "SEDANS", "2 DR SEDAN": "SEDANS", "SEDAN": "SEDANS", "SPORT UTILITY / STATION WAGON": "SPORT UTILITY VEHICLE", "PASSENGER":"PASSENGER VEHICLE","STATION WAGON/SPORT UTILITY VEHICLE": "SPORT UTILITY VEHICLE", "PICK-UP TRUCK": "TRUCK", "BOX TRUCK": "TRUCK"}, inplace=True)

print(new_data['VEHICLE_TYPE'].unique())

def Clean_names(VEHICLE_TYPE):
  if VEHICLE_TYPE in ['SEDANS','VAN','BIKE','BUS','TAXI','SPORT UTILITY VEHICLE','PASSENGER VEHICLE','TRUCK','MOTORCYCLE','BICYCLE']:
      return VEHICLE_TYPE
  else:
      return None

# Update the vehicle_make columns
new_data['VEHICLE_TYPE'] = new_data['VEHICLE_TYPE'].apply(Clean_names)

print(new_data)

print(new_data['VEHICLE_TYPE'].unique())

print(new_data)

new_data=new_data.dropna(subset=['VEHICLE_TYPE'])

print(new_data)

new_data.insert(1,'counter','1')

new_data

new_data.groupby(['VEHICLE_TYPE'])[['counter']].count()

# Creating dataset
VEHICLE_TYPE = ['BICYCLE','BIKE',
        'BUS', 'MOTORCYCLE', 'SEDANS','SPORT UTILITY VEHICLE','TAXI','TRUCK','VAN','PASSENGER VEHICLE']
 
data = ['1','10400','7098','3328','210948','166351','14755','22683','3133','7']

palette_color = seaborn.color_palette('pastel')

 
# Creating plot
fig = plt.figure(figsize =(20, 10))
plt.pie(data,autopct='%1.1f%%',labels = VEHICLE_TYPE, colors=palette_color)
plt.title('Pie Chart for Vehicle Makes')
plt.legend()
# show plot
plt.show()

"""ANALYSIS """

q2019=q21

#finding the average value per month for the year 2019
countBmw19=q2019['CountBMW'].sum()
avgBmw19=countBmw19/4
countAudi19=q2019['CountAudi'].sum()
avgAudi19=countAudi19/4
countNiss19=q2019['CountNiss'].sum()
avgNiss19=countNiss19/4
countSuba19=q2019['CountSuba'].sum()
avgSuba19=countSuba19/4

q2020=q31

#finding the average value per month for the year 2020
countBmw20=q2020['CountBMW'].sum()
avgBmw20=countBmw20/4
countAudi20=q2020['CountAudi'].sum()
avgAudi20=countAudi20/4
countNiss20=q2020['CountNiss'].sum()
avgNiss20=countNiss20/4
countSuba20=q2020['CountSuba'].sum()
avgSuba20=countSuba20/4

q2021=q41

#finding the average value per month for the year 2021
countBmw21=q2021['CountBMW'].sum()
avgBmw21=countBmw21/4
countAudi21=q2021['CountAudi'].sum()
avgAudi21=countAudi21/4
countNiss21=q2021['CountNiss'].sum()
avgNiss21=countNiss21/4
countSuba21=q2021['CountSuba'].sum()
avgSuba21=countSuba21/4

CountAverage2019={countBmw19:avgBmw19,countAudi19:avgAudi19,countNiss19:avgNiss19,countSuba19:avgSuba19}

print(CountAverage2019)

CountAverage2020={countBmw20:avgBmw20,countAudi20:avgAudi20,countNiss20:avgNiss20,countSuba20:avgSuba20}

print(CountAverage2020)

CountAverage2021={countBmw21:avgBmw21,countAudi21:avgAudi21,countNiss21:avgNiss21,countSuba21:avgSuba21}

print(CountAverage2021)

