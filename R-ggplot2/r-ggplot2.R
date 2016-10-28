library(ggplot2)
cars <- read.csv("cars-sample.csv")

p <- ggplot(cars, aes(Weight, MPG, size = Weight, color = Manufacturer))
p + geom_point(alpha = 0.5)

