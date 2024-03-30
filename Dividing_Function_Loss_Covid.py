import pandas as pd
import numpy as np

Subway = pd.read_excel('Data/Subway_Old_Final_Covid.xlsx', index_col=0, header=0)
Loss = pd.read_excel('Data/All_Revenue_Loss_Covid.xlsx', index_col=0, header=0)

index = [2, 6, 10, 14, 18, 22, 26, 30, 34]

MonthPeople = []
for i in range(24):
  tempList = []
  for j in index:
    SumPeople = 0
    SumPeople = Subway.iloc[i, j] // 1000
    tempList.append(SumPeople)
  MonthPeople.append(tempList)

ratio = []
for i in range(24):
  AllMonthPeople = 0
  tempList2 = []

  for j in range(9):
    AllMonthPeople = AllMonthPeople + MonthPeople[i][j]

  for k in range(9):
    temp = 0
    temp = MonthPeople[i][k] / AllMonthPeople
    tempList2.append(temp)
  ratio.append(tempList2)

MonthLoss = []
for i in range(24):
  tempList3 = []
  Loss.drop
  for j in range(9):
    LossYear = 0
    LossYear = Loss.iloc[i, 1] * ratio[0][j]
    tempList3.append(LossYear)
  MonthLoss.append(tempList3)

# MonthLoss = np.array(MonthLoss)
# print(MonthLoss)
