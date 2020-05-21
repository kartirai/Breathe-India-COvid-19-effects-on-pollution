# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#basic commands on datasets
city_data = pd.read_csv('C:/Users/karti/Documents/Kartikey DS/city_day.csv')
display(city_data.head(5))
city_data.info()

#finding out the missing values
def missing_values_table(city_data):
    mis_value = city_data.isnull().sum()
    mis_value_percent = 100 * (city_data.isnull().sum()/len(city_data))
    mis_value_table = pd.concat([mis_value,mis_value_percent],axis=1)
    mis_value_table_ren_columns = mis_value_table.rename(columns = {0:'Missing values',1:'% of Total values'})
    mis_value_table_ren_columns = mis_value_table_ren_columns[mis_value_table_ren_columns.iloc[:,1]!=0].sort_values('% of Total values',ascending=False).round(1)
    print('Your selected data frame has ' + str(city_data.shape[1]) + ' columns\n' 'There are ' + str(mis_value_table_ren_columns.shape[0]) + ' columns that have missing values.')
    return mis_value_table_ren_columns

missing_values = missing_values_table(city_data)
missing_values.style.background_gradient(cmap='Reds')

#extracting list of cities from the dataset
cities = city_data['City'].value_counts()
print(f'Total number of cities in the dataset : {len(cities)}')
print(cities.index)

city_data['Date'] = pd.to_datetime(city_data['Date'])
print(f"The available data is between {city_data['Date'].min()} and {city_data['Date'].max()}")
