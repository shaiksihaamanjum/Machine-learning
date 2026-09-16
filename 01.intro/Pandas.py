import pandas as pd 
# pandas has two datatypes-1.sSeries(1D),2.DataFrame(2D)
df=pd.read_csv("train.csv",sep=",")
print(df.head())  # first 5 rows of dataset 
print(df.tail())  # last 5 rows of dataset 
print(df.info())  # to get basic info on dataset 
print(df.describe())  # to get mathematical and statistical calculations on each column of dataset 
print(df.columns)  # to get column names of dataset
print(df.duplicated().sum()) # to check duplicate values presence
print(df.drop_duplicates(inplace=True)) # to remove duplicates 
print(df.isnull().sum()[df.isnull().sum()>0])  # to get columns with null values and count 
print(df.shape)
df=df.fillna({'Age':df['Age'].median(),'Cabin':df['Cabin'].fillna("None"),'Embarked':df['Embarked'].fillna(0)})  # filling missing values with suitable values
print(df.isnull().sum()) # to check if any missing values are present 
df['family']=df['SibSp']+df['Parch']  # adding new column 
print(df['family'])
del df['family']        # to delete any column
#accessing
print(df.loc[0:10])     #  gives 0 to 10 rows 
print(df.loc[0:10,['Pclass','Name','Embarked']])  # gives 0 to 10 rows with only these columns-'Pclass','Name','Embarked'
print(df.iloc[0:10,[2,3,11]])        # gives 0 to 10 rows with columns-'Pclass','Name','Embarked' but with id's 
#filtering 
df1=df[df['Age']<=20]           # filters passengers with only age less than or equal to 20 
print(df1['Age'].count())       # printing count 
df['Ticket']=df['Ticket'].str.replace('/',"",regex=False) #to replace unnecessary symbols with empty string from columns
print(df.loc[0:5,['Ticket']])
df2=df.groupby('Pclass')['Survived'].sum() # to groupby pclass as index and sum is applied on survived 
df3=df[df['Embarked']=='S']
print(df3.shape)
df4=pd.pivot_table(df,index='Pclass',columns='Sex',values=['Survived'],aggfunc='sum') # to get a summary table for understanding 
print(df4.head())
print(df.corr(numeric_only=True)) # to check correlation between numerical columns
df.to_csv("cleaned_data.csv")   # to save cleaned data into new file
