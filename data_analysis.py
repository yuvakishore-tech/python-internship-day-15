import pandas as pd

df = pd.read_csv("")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

for column in df.select_dtypes(include=['float64', 'int64']):
    df[column] = df[column].fillna(df[column].mean())

for column in df.select_dtypes(include=['object']):
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

high_salary = df[df["Salary"] > 60000]
print("\nEmployees with Salary > 60000:")
print(high_salary)

df_sorted = df.sort_values(by="Salary", ascending=False)
print("\nTop Salaries:")
print(df_sorted.head())

dept_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(dept_salary)

df["Annual_Bonus"] = df["Salary"] * 0.10

df.to_csv("cleaned_dataset.csv", index=False)

print("\nAnalysis Completed")
