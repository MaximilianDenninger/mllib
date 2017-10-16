import mllib
import mllib.visualize.visu as Visu
import os

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
reader = mllib.Reader(dir_path + "text.txt")
reader.set_style('x,y')
#Visu.plot(reader.get_data())

sepReader = mllib.SeparateReader(dir_path + "text.txt", dir_path + "label.txt")
sepReader.set_style("x,x", "c")
data = sepReader.get_data()
Visu.plot(data)

