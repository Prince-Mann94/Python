titanic_ffill = titanic.copy()
print(titanic_ffill.fillna(method="ffill"))