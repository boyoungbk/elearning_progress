import pandas as pd

date = "20200826"
path = "./xlsx/학습이력_{}.xlsx".format(date)

dt = pd.read_excel(path, skiprows=4, usecols="B:F", header=None, encoding="euc-kr")
print(dt)