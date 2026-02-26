getwd()
setwd("C:/Users/NAVEEN VARMA/Downloads")

# 1. Read the data into ‘R’. Note: the data is 
# saved as a .CSV file. You may need to know how to read a CSV
# file into ‘R’ if you have not done this before.

data <- read.csv("wages.csv", header=T)
names(data)
head(data)


#  Race has missing values which are denoted by ‘?’. Delete the samples with these missing values and
#  save this column as a factor for the following analysis.


Race <- data$Race
i = which(Race=='?')
i

data <- data[-i]
is.factor(data$Race)
data$Race <- factor(data$Race)
is.factor(data$Race)


# 3. is.na

j <- which(apply(is.na(data),1, any))
data <- data[-j,]


# 4.  
data$Sex <- factor(data$Sex)
data$Union <- factor(data$Union)
data$Occupation <- factor(data$Occupation)
data$Marital_status <- factor(data$Marital_status)

str(data)


#5.
x = data$Age
y = data$Wage

model1 <- lm(y~x)

summary(model1)



7. 
plot(x, y, xlab = "Age", ylab = "Wage")
abline(model1, col="blue")


8. 
model2 <- lm(y ~ Education + Work_experience + Age, data=data)
summary(model2)


anova(model1, model2)

           





