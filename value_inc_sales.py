# -*- coding: utf-8 -*-
"""
Created on Sun May  1 12:01:15 2022

@author: Shreya
"""

import pandas as pd

#file_name = pd.read_csv('file.csv')   <--format  of read csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')
#data summary

data.info()

#cost per transaction calculation
CostPerItem = data['CostPerItem']

NoOfItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NoOfItemsPurchased 

SellPerItem = data['SellingPricePerItem']

SellPerTransaction = SellPerItem * NoOfItemsPurchased

#adding new column datafram
data['CostPerTransaction'] = CostPerTransaction
data['SellPerTransaction'] = SellPerTransaction

#profit
data['profitPerTransaction'] = data['SellPerTransaction'] - data['CostPerTransaction']

#markup
data['markup'] =  (data['SellPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

#round markup
roundMarkup = round(data['markup'],2)

data['markup'] =  round(data['markup'],2)

#checking column data type

#print(data['Day'].dtype)

#convert another data type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
#print(day.dtype)

my_date = day + '-'+ data['Month'] + '-' + year

data['date'] =  my_date


#using iloc to view specific row column

data.iloc[0]

data.iloc[0:3]  #first three

data.iloc[-5:]  #last 5 rows

data.head(5) #first 5 rows


data.iloc[:,2] #all rows of specific column 0,1,2
data.iloc[4,2] #4th row, 2nd column

#splitting ClientKeywords
#new_var = column.str.split('seperator',expand =True) #expand=True means it will split everything, not stop after 1 coma

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new column for split columns

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using replace function(remove bracket in ClientAge , LengthOfContract)


data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')


data['ItemDescription'] = data['ItemDescription'].str.lower()



data_season = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging data set
# merge_df = pd.merge(old_df,new_df,on = 'key')

data = pd.merge(data,data_season, on='Month')

#drop column
#df = df.drop('column name', axis = 1)

data = data.drop('ClientKeywords', axis=1)

data = data.drop('Day', axis=1)

#drop multiple column
data = data.drop(['Year','Month'], axis=1)

data.to_csv('Value_inc_cleaned.csv', index = False)




























































































