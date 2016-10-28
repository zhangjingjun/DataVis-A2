from ggplot import *
import pandas

cars = pandas.read_csv('cars-sample.csv')

print(ggplot(cars, aes('Weight', 'MPG', size="Wt", color='Manufacturer')) + geom_point(alpha=0.5) + scale_x_continuous('Weight', breaks=[1000, 2000, 3000, 4000, 5000]) + scale_y_continuous('MPG', breaks=[10, 20, 30, 40, 50]))

