import pandas as pd
import numpy as np
titanic = pd.read_csv(r"c:\Users\Princ\OneDrive\Documents\titanic.csv")
print(titanic.isnull().sum())
titanic_drop_rows = titanic.dropna()
print(titanic_drop_rows.size)
print(titanic.size)
titanic_mean = titanic.copy()
titanic_mean["age"] = titanic_mean["age"].fillna(titanic_mean["age"].mean())
print(titanic_mean)
titanic_median = titanic.copy()
titanic_median["age"] = titanic_median["age"].fillna(titanic_median["age"].median())
print(titanic_median)

titanic_mode = titanic.copy()
titanic_mode["Embarked"] = titanic_mode["Embarked"].fillna(titanic_mode["Embarked"].mode())
print(titanic_mode)

titanic_interpolate = titanic.copy()
titanic_interpolate["age"] = titanic_interpolate["age"].interpolate()
titanic_interpolate.head(7)
titanic_interpolate.isnull().sum()
# titanic_ffill = titanic.copy()
# print(titanic_ffill.fillna(method="ffill"))
