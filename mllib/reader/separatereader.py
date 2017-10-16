from . import basicreader
from ..basics import utilities
from ..basics import data
from ..basics import datastructure


class SeparateReader(object):

    def __init__(self, data_file, label_file):
        self._dataReader = basicreader.BasicReader(data_file)
        self._labelReader = basicreader.BasicReader(label_file)

    def set_style(self, data_style, label_style):
        self._dataReader.set_style(data_style)
        self._labelReader.set_style(label_style)

    def get_data(self):
        x = self._dataReader.get_data()
        labels = self._labelReader.get_data()
        return data.Data(datastructure.DataStructure.RS, x.get_x(), labels.get_y(), self._labelReader.has_class())

    def num_of_lines(self):
        if self._dataReader.num_of_lines() == self._labelReader.num_of_lines():
            return self._dataReader.num_of_lines()
        else:
            utilities.print_error("The number of lines in the data and the label file does not correspond!")
            return 0
