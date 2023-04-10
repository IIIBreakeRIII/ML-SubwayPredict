from Subway_Poly_Revenue_Final import RevenueCoef as revenueCoef
from Subway_Poly_Revenue_Final import RevenueIntercept as revenueIntercept
from Subway_Poly_Revenue_Final import RevenueTrainScore as revenueTrainScore
from Subway_Poly_Revenue_Final import RevenueTestScore as revenueTestScore

from Subway_Poly_Loss_Covid import LossCoef as lossCoef
from Subway_Poly_Loss_Covid import LossIntercept as lossIntercept
from Subway_Poly_Loss_Covid import LossTrainScore as lossTrainScore
from Subway_Poly_Loss_Covid import LossTestScore as lossTestScore

print("전체 이용자와 만 65세 이상 이용자 수를 적으세요.")
AllPeople, OldPeople = map(int, input().split())

sum = 0

for i in range(9):
  if i == 0:
    sum = sum + (revenueCoef[0][0] * AllPeople)
  elif i == 1:
    sum = sum + (revenueCoef[0][1] * OldPeople)
  elif i == 2:
    sum = sum + (revenueCoef[0][2] * AllPeople ** 2)
  elif i == 3:
    sum = sum + (revenueCoef[0][3] * AllPeople * OldPeople)
  elif i == 4:
    sum = sum + (revenueCoef[0][4] * OldPeople ** 2)
  elif i == 5:
    sum = sum + (revenueCoef[0][5] * AllPeople ** 3)
  elif i == 6:
    sum = sum + (revenueCoef[0][6] * AllPeople ** 2 * OldPeople)
  elif i == 7:
    sum = sum + (revenueCoef[0][7] * AllPeople * OldPeople ** 2)
  elif i == 8:
    sum = sum + (revenueCoef[0][8] * OldPeople ** 3)

RevenueSum = 0
RevenueSum = sum + revenueIntercept[0]

sum = 0

for i in range(9):
  if i == 0:
    sum = sum + (lossCoef[0][0] * AllPeople)
  elif i == 1:
    sum = sum + (lossCoef[0][1] * OldPeople)
  elif i == 2:
    sum = sum + (lossCoef[0][2] * AllPeople ** 2)
  elif i == 3:
    sum = sum + (lossCoef[0][3] * AllPeople * OldPeople)
  elif i == 4:
    sum = sum + (lossCoef[0][4] * OldPeople ** 2)
  elif i == 5:
    sum = sum + (lossCoef[0][5] * AllPeople ** 3)
  elif i == 6:
    sum = sum + (lossCoef[0][6] * AllPeople ** 2 * OldPeople)
  elif i == 7:
    sum = sum + (lossCoef[0][7] * AllPeople * OldPeople ** 2)
  elif i == 8:
    sum = sum + (lossCoef[0][8] * OldPeople ** 3)

LossSum = 0
LossSum = sum + lossIntercept[0]

print("지하철 전체 이용자에 대한 수입액 학습에 대한 Train, Test 정확도")
print("Train Score :", revenueTrainScore)
print("Test Score :", revenueTestScore)
print("예상 수입액 :", RevenueSum)
print(" ")
print("지하철 만 65세 이상에 대한 적자액 학습에 대한 Train, Test 정확도")
print("Train Score :", lossTrainScore)
print("Test Score :", lossTestScore)
print("예상 적자액 :", LossSum)

# 23183000, 3229908 --> 2019년 2월 전체 이용자와 노인 이용자
# 수입액 : 1.76540063e+10
# 적자액 : 4.89869447e+09
# print(1.76540063e+10)
# print(4.89869447e+09)