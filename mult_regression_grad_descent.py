# To tinker with linear regression, I made up these numbers and used gradient descent
# to calculate the weight b0, b1, and b2 (i.e. two independent variables).
# I checked it against this online multiple regression calculator, which gave me the same
# answers: 
# https://www.socscistatistics.com/tests/multipleregression/default.aspx
# answers:
# b0 =  5.32845
# b1 = -0.38912
# b2 =  0.22646
# I don't know why I had to use such a small alpha to get a result.
# Hopefully I'll get some more insight on that later.

import csv
import tokenize
import numpy as np

X = np.array([[1,2,3],[1,5,7],[1,6,5],[1,3,8],[1,6,9],[1,7,5],[1,9,5],[1,4,7],[1,1,3]])
y = np.array([[3],[6],[4],[7],[1],[2],[5],[9],[6]])

b0 = 0
b1 = 0
b2 = 0

b = np.array([[0],[0],[0]])
alpha = 0.01

m = 9

yhat = X[:,0]*b0+X[:,1]*b1+X[:,2]*b2


for _ in range(100000):
	yhat = X[:,0]*b0+X[:,1]*b1+X[:,2]*b2
	error = yhat-y.transpose()
	b0temp = b0-alpha/m*np.sum(np.multiply( error , X[:,0] ))
	b1temp = b1-alpha/m*np.sum(np.multiply( error , X[:,1] ))
	b2temp = b2-alpha/m*np.sum(np.multiply( error , X[:,2] ))
	b0 = b0temp
	b1 = b1temp
	b2 = b2temp
print b0, b1, b2


