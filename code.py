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
city_data.head(5)
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

#analyzing the complete city level daily data
city_data['BTX'] = city_data['Benzene'] + city_data['Toluene'] + city_data['Xylene']
city_data.drop(['Benzene','Toluene'],axis=1)
city_data['Particulate Matter'] = city_data['PM2.5']+city_data['PM10']
pollutants = ['PM2.5','PM10','NO2','CO','SO2','O3','BTX']

#visualizing the city data
city_data.set_index('Date',inplace=True)
axes = city_data[pollutants].plot(marker='.',alpha=0.5,linestyle='None',figsize=(16,20),subplots=True)
for ax in axes:
    ax.set_xlabel('Years')
    ax.set_ylabel('ug/m3')

df = city_data

#Year-month wise distribution 
def trend_plot(dataframe,value):
    df['year'] = [d.year for d in df.Date]
    df['month'] = [d.strftime('%b') for d in df.Date]
    year = df['year'].unique()
    
    #draw the plot
    fig,axes = plt.subplots(1,2,figsize = (14,6),dpi = 80)
    sns.boxplot(x='year',y=value,data = df,ax = axes[0])
    sns.pointplot(x='month',y=value,data = df.loc[~df.year.isin([2015,2020]), :])
    
    #Set title
    axes[0].set_title('Year wise Box Plot \n(The Trend)',fontsize=18);
    axes[1].set_title('Month wise Plot \n(The seasonality)',fontsize = 18)
    plt.show()

#NO2
df.reset_index(inplace=True)
df = df.copy()
value = 'NO2'
trend_plot(df,value)    

#SO2
df.reset_index(inplace=True)
df = df.copy()
value = 'SO2'
trend_plot(df,value)    

#BTX
df.reset_index(inplace=True)
df = df.copy()
value='BTX'
trend_plot(df,value)

#PM2.5
value = 'PM2.5'
trend_plot(df,value)

#PM10
value = 'PM10'
trend_plot(df,value)

#finding out which city has the most pollution
def max_polluted_city(pollutants):
    x1 = city_data[[pollutants,'City']].groupby(["City"]).mean().sort_values(by=pollutants,ascending=False).reset_index()
    x1[pollutants] = round(x1[pollutants],2)
    return x1[:10].style.background_gradient(cmap='OrRd')

from IPython.display import display_html
def display_side_by_side(*args):
    html_str=''
    for df in args:
        html_str+=df.render()
    display_html(html_str.replace('table','table_style="display:inline"'), raw=True)

pm2_5 = max_polluted_city('PM2.5')
pm10 = max_polluted_city('PM10')
no2 = max_polluted_city('NO2')
so2 = max_polluted_city('SO2')
co = max_polluted_city('CO')
btx = max_polluted_city('BTX')

display_side_by_side(pm2_5,pm10,no2,so2,co,btx)














































