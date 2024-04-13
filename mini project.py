import pandas as pd

# reading data set
df = pd.read_csv(r"C:\\Users\\sarth\\Desktop\\DATA SCI\\ml-20m\\ml-20m\\movies.csv")
df1 = pd.read_csv(r"C:\\Users\\sarth\\Desktop\\DATA SCI\\ml-20m\\ml-20m\\tags.csv")
df2 = pd.read_csv(r"C:\\Users\\sarth\\Desktop\\DATA SCI\\ml-20m\\ml-20m\\ratings.csv")

# checking for null values 
df.isnull().sum()
df1.isnull().sum()
df2.isnull().sum()

# counting null values
print(df.isnull().sum().sum())
print(df1.isnull().sum().sum())
print(df2.isnull().sum().sum())

# removing null values
df.drop('title', axis=1, inplace=True)
df1.drop('movieId', axis=1, inplace=True)
df2.drop('movieId', axis=1, inplace=True)

# grouping 
grouped_df = df.groupby('genres')
grouped_df1 = df1.groupby('userId')
grouped_df2 = df2.groupby('userId')



