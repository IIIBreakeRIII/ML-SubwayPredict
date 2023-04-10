import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

from Dividing_Function_Loss import MonthLoss as ML

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', header=0, usecols=[3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36])
Loss = ML

Subway = np.array(Subway).reshape(-1, 2)
Loss = np.array(Loss).reshape(-1, 1)

poly = PF(degree=3, include_bias=False)
poly.fit(Subway)
train_poly = poly.transform(Subway)

train_input, test_input, train_target, test_target = tts(train_poly, Loss, test_size=0.25, random_state=42)

print(len(train_input), len(test_input), len(train_target), len(test_target))

lr = LR()
lr.fit(train_input, train_target)

print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

coef = lr.coef_
intercept = lr.intercept_

predictValue = 25918000
predictValue2 = 3728315

sum = 0

for i in range(5):
  if i == 0:
    sum = sum + (coef[0][0] * predictValue)
  elif i == 1:
    sum = sum + (coef[0][1] * predictValue2)
  elif i == 2:
    sum = sum + (coef[0][2] * predictValue ** 2)
  elif i == 3:
    sum = sum + (coef[0][3] * predictValue * predictValue2)
  elif i == 4:
    sum = sum + (coef[0][4] * predictValue2 ** 2)
  elif i == 5:
    sum = sum + (coef[0][5] * predictValue ** 3)
  elif i == 6:
    sum = sum + (coef[0][6] * predictValue ** 2 * predictValue2)
  elif i == 7:
    sum = sum + (coef[0][7] * predictValue * predictValue2 ** 2)
  elif i == 8:
    sum = sum + (coef[0][8] * predictValue2 ** 3)

sum = sum + intercept[0]

print(sum)

print(5.33599202e+09)