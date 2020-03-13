"""
**************  pandas cheat sheet     ***************************
@author: I0001192
"""

import pandas as pd
df = pd.read_csv("train.csv", header = 0,skiprows=[3])

#  INSPECT
df.head()
df.tail(2)
df.info()
df.shape
df.columns
df.isnull()
type(df)
type(df["Age"])
df.index
df.describe() # summary
df["Survived"].value_counts()
df["Fare"].quantile()
df.corr()
df[1,:].unique()


#   SUBSET
df[1:2]
#select columns 
df.loc[7,"Fare" ]  # loc for column names , iloc for column indices
df.iloc[0:3, 0:4]
df[df['Age'] == 20]

df.loc[df.Fare>100]
df.loc[:, df.columns != 'Age']
df.loc[:, df.columns.isin(['Age','Survived'])]
df.loc[:,~ df.columns.isin(['Age','Survived'])]


# TRANSFORM
df.append(df)
df.drop_duplicates()
df.dropna()
df.dropna(axis=1) # for column dropping
#converting to pd 
#df df = pd.DataFrame(data = flight_radar_24_data)

df1 = df.sort_values("Fare", ascending = False)
    

# PLOTS
df['Fare'].plot(kind='hist', title='Fare')
df.plot(kind='scatter', x='Age', y='Fare', title='Age VS fare')
df


### FUNCTIONS
