getwd()
advertising <- read.csv("Advertising.csv", header = T)
advertising


head(advertising)

attach(advertising)

summary(advertising)

advertising[,2]

detach(advertising)


advertising$sales

summary(model.Tv <- lm(sales ~ TV))

summary(model.newspaper <- lm(sales ~ newspaper))


par(mfrow = c(1,3))
plot(TV, sales , col= "red")
abline(model.Tv, lwd= 3 , col="blue")
