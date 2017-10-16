import matplotlib.pyplot as plt
from matplotlib  import cm
from ..basics import utilities
import numpy as np
from ..basics import datastructure


def plot(data):
    if data.has_class():
        if data.dim() == 2:
            current_type = data.get_type()
            data.switch_type(datastructure.DataStructure.CS)
            fig = plt.figure(figsize=(6,6))
            ax = fig.add_subplot(111)
            x = data.get_x()
            c = data.get_y()
            max = float(np.amax(c))
            classes = [float(ele) / max for ele in c]
            print(classes)
            ax.scatter(x[0], x[1], c=classes, cmap=cm.hsv)
            plt.show()
            data.switch_type(current_type)
        else:
            utilities.printError('Currently only 2D visualizations are supported!')
    else:
        if data.dim() == 1 and data.dim_for_y() == 1:
            current_type = data.get_type()
            data.switch_type(datastructure.DataStructure.CS)
            fig = plt.figure(figsize=(6,6))
            ax = fig.add_subplot(111)
            x = data.get_data()
            x = data.get_x()
            y = data.get_y()
            ax.plot(x[0], y[0], 'ro')
            plt.show()
            data.switch_type(current_type)
        else:
            utilities.printError('Currently only 2D visualizations are supported!')

