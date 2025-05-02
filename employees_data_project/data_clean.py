# import libraries
import numpy as np
import pandas as pd

# load CSV file
df = pd.read_csv(r'D:\python_prog\NUMPY\employees_data_project\employees.csv')
print(df.head())

# check missing values
print("Missing values in each column")
print(df.isnull().sum())

# check columns
print("Column at index 3:", df.columns[3])
print("Columns in the dataset:", df.columns.tolist())

# fill missing values in 'SALARY' column
df['SALARY'].fillna(df['SALARY'].mean(), inplace=True)

# verify missing values handled
print(df.isnull().sum())

# check top rows of SALARY
print(df['SALARY'].head())

# drop duplicate rows
df.drop_duplicates(inplace=True)
print(df.head())

# fix negative salary values
df['SALARY'] = np.where(df['SALARY'] < 0, df['SALARY'].mean(), df['SALARY'])  # ❗Fixed: df['SALARY '] → df['SALARY']

# remove outliers beyond 3 standard deviations
salary_mean = df['SALARY'].mean()
salary_std = df['SALARY'].std()
lower = salary_mean - (3 * salary_std)
upper = salary_mean + (3 * salary_std)
df = df[(df['SALARY'] >= lower) & (df['SALARY'] <= upper)]

# save cleaned data to CSV
df.to_csv('employees_cleaned.csv', index=False)

print('Data cleaning completed. Saved as employees_cleaned.csv')

