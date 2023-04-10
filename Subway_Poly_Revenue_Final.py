import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import PolynomialFeatures as PF

from Dividing_Function_Revenue import MonthRevenue as MR

Subway = pd.read_excel('Data/Subway_Old_Final.xlsx', header=0, usecols=[3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36])
Revenue = MR

Subway = np.array(Subway).reshape(-1, 2)
Revenue = np.array(Revenue).reshape(-1, 1)

poly = PF(degree=3, include_bias=False)
poly.fit(Subway)
train_poly = poly.transform(Subway)

train_input, test_input, train_target, test_target = tts(train_poly, Revenue, test_size=0.1, random_state=42)

lr = LR()
lr.fit(train_input, train_target)
RevenueTrainScore = lr.score(train_input, train_target)
RevenueTestScore = lr.score(test_input, test_target)

RevenueCoef = lr.coef_
RevenueIntercept = lr.intercept_