import bokeh
from bokeh.charts import Scatter, output_file, show
import pandas


def findColor(manu):
    colorDict = {"ford": "yellow", "bmw": "pink", "honda": "green", "mercedes": "blue", "toyota": "purple"}
    colorList = []
    for a in manu:
        colorList.append(colorDict[a])
    return colorList

cars = pandas.read_csv("cars-sample.csv")
TOOLS="hover,crosshair,pan,wheel_zoom,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"
pic = bokeh.plotting.figure(tools=TOOLS)

pic.scatter(cars["Weight"], cars["MPG"], radius=cars["Weight"]/50, fill_alpha=0.5, fill_color=findColor(cars["Manufacturer"]))
pic.xaxis.axis_label = "Weight"
pic.xaxis.ticker = bokeh.models.FixedTicker(ticks=[1000, 2000, 3000, 4000, 5000])
pic.yaxis.axis_label = "MPG"
pic.yaxis.ticker = bokeh.models.FixedTicker(ticks=[10, 20, 30, 40, 50])

output_file("bokeh.html")

show(pic)

