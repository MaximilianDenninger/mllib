import mllib
import mllib.visualize.visu as Visu
import os

"""
	This is a small machine learning library, it provides an easy way of loading data and visualizing it.
	
	At first the used data must be loaded with the Reader. It uses a normal text file, where in each line a new point 
	can be specified. The format of each line can be specified over the set_style() function. See reader/basicreader.py.
	
	The data can be visualized with the Visu module, it contains a plot function, which can visualize Data objects.
	
	All this is a starting platform for your own machine learning approaches.
"""

dir_path = mllib.utilities.get_path_of_main_file()  # gets the path to the main file

# set up the reader with the path to the used text file for the data
reader = mllib.Reader(os.path.join(dir_path, "data", "data.txt"))
# set the style in each line in the text file
reader.set_style('x,y')
# read data and save it in data
data = reader.get_data()
# visualize the data
Visu.plot(data)

sepReader = mllib.SeparateReader(os.path.join(dir_path, "data", "data.txt"), os.path.join(dir_path, "data", "label.txt"))
sepReader.set_style("x,x", "c")
data = sepReader.get_data()
Visu.plot(data)



