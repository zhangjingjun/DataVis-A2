import matplotlib.pyplot
import pandas

def findColor(manu):
    colorDict = {"ford": "yellow", "bmw": "pink", "honda": "green", "mercedes": "blue", "toyota": "purple"}
    colorList = []
    for a in manu:
        colorList.append(colorDict[a])
    return colorList

cars = pandas.read_csv("cars-sample.csv")

pic = matplotlib.pyplot.figure()
sp = pic.add_subplot(1, 1, 1)
sp.scatter(cars["Weight"], cars["MPG"], s=cars["Weight"]/10, color=findColor(cars["Manufacturer"]), alpha=0.5)
matplotlib.pyplot.xlabel("Weight")
matplotlib.pyplot.ylabel("MPG")
matplotlib.pyplot.xticks((1000, 2000, 3000, 4000, 5000))
matplotlib.pyplot.yticks((10, 20, 30, 40, 50))

matplotlib.pyplot.show()