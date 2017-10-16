
from os.path import isfile
from ..basics import utilities
import numpy as np
from ..basics import data
from ..basics import datastructure

class Style(object):

    def __init__(self, style, splitEle):
        self._hasClass = False
        self._numberOfDim = 0
        self._numberOfDimForReg = 0
        self._splitEle = splitEle
        style = utilities.remove_white_chars(style)
        self._type = []
        self._xtype = 1
        self._ytype = 2
        self._ctype = 3
        for ele in style.split(self._splitEle):
            if ele == 'x' or ele == 'X':
                self._numberOfDim += 1
                self._type.append(self._xtype)
            elif ele == 'y' or ele == 'Y' or ele == 'z' or ele == 'Z':
                self._numberOfDimForReg += 1
                self._type.append(self._ytype)
            elif ele == 'c' or ele == 'C':
                self._hasClass = True
                self._type.append(self._ctype)
            else:
                utilities.printError('This type is unknown!')
        if self._hasClass and self._numberOfDimForReg > 0:
            utilities.printError("It can not be regression and classification at the same time!")

    def has_class(self):
        return self._hasClass

    def interpret(self, new_line):
        new_line = utilities.remove_white_chars(new_line)
        x = np.zeros(self._numberOfDim)
        number_of_dim_for_reg = 1 if self._hasClass else self._numberOfDimForReg
        y = np.zeros(number_of_dim_for_reg)
        x_counter = 0
        y_counter = 0
        for ele, type in zip(new_line.split(self._splitEle), self._type):
            if type == self._xtype:
                x[x_counter] = float(ele)
                x_counter += 1
            elif type == self._ytype:
                y[y_counter] = float(ele)
                y_counter += 1
            elif type == self._ctype:
                y = int(ele)
            else:
                utilities.printError('This type is unknown!')
        return x, y


class BasicReader(object):

    def __init__(self, filePath, splitEle = ','):
        self._text = ""
        self._lineCounter = 0
        self._splitEle = splitEle
        self._style = None
        if isfile(filePath):
            with open(filePath,'r') as file:
                self._text = file.read()
                self._text = utilities.remove_comments_and_empty_lines(self._text)
                self._lines = self._text.split("\n")
        else:
            utilities.printError("This file is unknown!")
            exit(1)

    def set_style(self, style):
        self._style = Style(style, self._splitEle)

    def get_data(self):
        x = []
        y = []
        for line in self._lines:
            res = self._style.interpret(line)
            x.append(res[0])
            y.append(res[1])
        return data.Data(datastructure.DataStructure.RS, np.array(x), np.array(y), self.has_class())

    def has_class(self):
        return self._style.has_class()

    def num_of_lines(self):
        return len(self._lines)
