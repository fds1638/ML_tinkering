# Gaussian naive bayes with the iris dataset.
# Followed the calculation on this page:
# https://www.machinelearningplus.com/predictive-modeling/how-naive-bayes-algorithm-works-with-example-and-full-code/
# Use the training and test breakdown here:
# https://raw.githubusercontent.com/selva86/datasets/master/iris_train.csv
# https://raw.githubusercontent.com/selva86/datasets/master/iris_test.csv
# I got the same answers as that webpage: all correct except 4 of 15 in versicolor test data were classified as virginica.

import csv
import tokenize
import numpy as np
import csv
import math

def prob(x, m, v):
	return 1.0/math.sqrt(2*3.14159265359*v)*math.exp(-1.0*(x-m)*(x-m)/2/v)


# Set up a matrix called expect, which for each of 3 categories records
# for each of the four measurements the mean and variance.
# First add up all the values and the squared values.
# Last entry is the count.
expect = np.zeros((3,9));
with open('iris_train.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		idx = -1
		if row[4]=="setosa":
			idx = 0
		elif row[4]=="versicolor":
			idx = 1
		elif row[4]=="virginica":
			idx = 2
		expect[idx][0] += float(row[0])
		expect[idx][1] += float(row[0])*float(row[0])
		expect[idx][2] += float(row[1])
		expect[idx][3] += float(row[1])*float(row[1])
		expect[idx][4] += float(row[2])
		expect[idx][5] += float(row[2])*float(row[2])
		expect[idx][6] += float(row[3])
		expect[idx][7] += float(row[3])*float(row[3])
		expect[idx][8] += 1

# Find mean and variance by dividing through by count,
# and then subtracting off the mean squared to get the variance.
for rr in range(len(expect)):
	expect[rr][0] /= expect[rr][8]
	expect[rr][1] /= expect[rr][8]
	expect[rr][1] -= expect[rr][0]**2
	expect[rr][2] /= expect[rr][8]
	expect[rr][3] /= expect[rr][8]
	expect[rr][3] -= expect[rr][2]**2
	expect[rr][4] /= expect[rr][8]
	expect[rr][5] /= expect[rr][8]
	expect[rr][5] -= expect[rr][4]**2
	expect[rr][6] /= expect[rr][8]
	expect[rr][7] /= expect[rr][8]
	expect[rr][7] -= expect[rr][6]**2
			

print expect

# Now have mean and variance for each X and each category
# First get probabilities of all three categories.
p0 = expect[0][8] / ( expect[0][8]+expect[1][8]+expect[2][8] )
p1 = expect[1][8] / ( expect[0][8]+expect[1][8]+expect[2][8] )
p2 = expect[2][8] / ( expect[0][8]+expect[1][8]+expect[2][8] )


# Get the test data and for each find the conditional probability of having the evidence.
# Ignore the denominator which is constant throughout.
# Choose the greatest using max and maxprob.
# See if it is correct.
with open('iris_test.csv') as test_file:
	test_reader = csv.reader(test_file, delimiter=',')
	for row in test_reader:
		x1 = float(row[0])
		x2 = float(row[1])
		x3 = float(row[2])
		x4 = float(row[3])
		prob0 = p0 * prob(x1,expect[0][0],expect[0][1])* prob(x2,expect[0][2],expect[0][3])* prob(x3,expect[0][4], expect[0][5])*prob(x4,expect[0][6],expect[0][7])
		prob1 = p1 * prob(x1,expect[1][0],expect[1][1])* prob(x2,expect[1][2],expect[1][3])* prob(x3,expect[1][4], expect[1][5])*prob(x4,expect[1][6],expect[1][7])
		prob2 = p2 * prob(x1,expect[2][0],expect[2][1])* prob(x2,expect[2][2],expect[2][3])* prob(x3,expect[2][4], expect[2][5])*prob(x4,expect[2][6],expect[2][7])
		max = -1
		maxprob = -1
		if prob0 > prob1:
			max = 0
			maxprob = prob0
		else:
			max = 1
			maxprob = prob1
		if prob2 > maxprob:
			max = 2
			maxprob = prob2
		if row[4]=="setosa":
			idx = 0
		elif row[4]=="versicolor":
			idx = 1
		elif row[4]=="virginica":
			idx = 2
		if max == idx:
			print max, idx, "true"
		else:
			print max, idx, "false"

