# This is the same as before, so I'm keeping all the same commentary below.
# The only new line is the lines breaking up the Embarked column (with entries of S, C, and Q)
# into Embarked_S and Embarked_C, and using them in the linear regression. We don't need
# Embarked_Q because it is not linearly independent. Get a result of 0.76315, a slight improvement.
# Oddly, logistic regression does less well. Perhaps it will do better with more variables.


# As an introductory exercise, let us do a multiple linear regression on the Titanic dataset in order
# to familiarize ourselves with R. We will only pay attention to four columns:
# Age, Sex, Fare, and Survived.
# Survived is obviously the dependent variable, which we will assume depends linearly on the 
# other three variables.
# First we will import the training data, make the necessary alterations to the data in the data frame
# so that we can do a multiple linear regression. Then we'll apply the resulting coefficients to the
# testing data, and generate a file that we can upload for Kaggle to grade.

# Read in the training data downloaded from kaggle.
traindata <- read.csv("/Users/fds/Downloads/titanic/train.csv",header=TRUE,stringsAsFactors=FALSE)

# Sex is coded using characters, either "female" or "male". Change that to a numeric value to allow
# multiple linear regression.
traindata$Sex[traindata$Sex=="female"] <- 1
traindata$Sex[traindata$Sex=="male"] <- 0
# For missing data in Age and Fare, put zeros (it works better than the means).
traindata$Age[is.na(traindata$Age)]<-0
traindata$Fare[is.na(traindata$Fare)] <- 0

# lm stands for "linear model" and is R's function for a linear regression. The tilde ~ indicates
# that one variable varies as the (sum of) others.
lm(traindata$Survived~traindata$Age+traindata$Fare+traindata$Sex+traindata$Embarked_S+traindata$Embarked_C,data=traindata)

# Import the training data.
testdata <- read.csv("/Users/fds/Downloads/titanic/test.csv",header=TRUE,stringsAsFactors=FALSE)

# If there is no age and/or fare entered, make it zero instead of NA.
testdata$Age[is.na(testdata$Age)]<-0
testdata$Fare[is.na(testdata$Fare)] <- 0

# Change female and male to 1 and 0.
testdata$Sex[testdata$Sex=="male"] <- 0
testdata$Sex[testdata$Sex=="female"] <- 1

# Just to make sure that R is interpreting everything as a number rather than as characters,
# force the relevant columns to be numeric.
testdata[,4]<-as.numeric(testdata[,4])
testdata[,5]<-as.numeric(testdata[,5])
testdata[,9]<-as.numeric(testdata[,9])


# This applies our function to the testdata set, once again forcing everything to be numeric.
# Note that once we apply the multiple linear regression model to a line in testdata, we need to 
# make it categorical. So if the result is greater than 0.5 it is coded as a 1 (i.e. survived),
# and if not it is a zero.
ff = function(x) { age <- as.numeric(x[5]); fare = as.numeric(x[9]); sex = as.numeric(x[4]); es = as.numeric(x[12]); ec = as.numeric(x[13]); if (0.1332066 - 0.0001176*age + 0.0013695*fare + 0.5198241*sex - 0.0001727*es + 0.1095772*ec > 0.5) {1} else {0}}

# Put the result of our calculation in the column "Survived".
testdata$Survived <- apply(testdata,1,ff)


# Put the two columns we want in a new data frame.
submit <- cbind(testdata[,1],testdata[,12])

# Give the submit data frame the column names Kaggle requires.
colnames(submit) <- c("PassengerID","Survived")

# Write the data frame as a csv file, ready to upload to Kaggle.
write.table(submit, "titanic_MLR_submit.csv", row.names=FALSE, col.names=TRUE, sep=",")

# As noted above, this now yields 0.76315
