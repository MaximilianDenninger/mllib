from .datastructure import DataStructure
from .converter import *
from . import utilities


class Data(object):
    """
    This class contains the data loaded in the readers, it can be used to train various models.

    Important to note is that the data has an inner structure, which is specified over the datastructure.
    That means that accessing times can be improved if the best datastructure is chosen.

    This class can be used for Regression as well as Classification, the labels or regression values are saved
    in both cases in the variable y (accessible with get_y())
    """

    def __init__(self, data_type, x, y, has_class):
        self._x = x
        self._y = y
        dim_for_dim = 0 if DataStructure.is_row(data_type) else 1
        self._len_of_x = x.shape[dim_for_dim]
        if y.shape[0] > 0:
            self._len_of_y = y.shape[dim_for_dim]
        if self._len_of_x > 0:
            other_dim = (dim_for_dim + 1) % 2
            self._dim = self._x.shape[other_dim]
            if len(y.shape) > other_dim:
                self._dimForY = self._y.shape[other_dim]
            else:
                self._dimForY = 1
        else:
            utilities.print_error("No points were provided!")
        self._has_class = has_class
        if DataStructure.is_valid(data_type):
            self._data_type = data_type
        else:
            utilities.print_error("This type is unknown!")

    def switch_type(self, type):
        if DataStructure.is_valid(type):
            if type != self._data_type:
                if DataStructure.is_combined(type) and DataStructure.is_combined(self._data_type):
                    self._x = self._x.transpose()  # both types are combined, and switch is from C -> S or S -> C
                elif DataStructure.is_separated(type) and DataStructure.is_separated(self._data_type):
                    self._x = self._x.transpose()  # both are separated, switch is from C -> S or S -> C
                    self._y = self._y.transpose()
                else:
                    if DataStructure.is_combined(self._data_type):
                        result = convert_data_for_combined(self._x, self._data_type, type, self._len_of_x)
                    else:
                        result = convert_data_for_separated(self._x, self._y, self._data_type, type, self._len_of_x)
                    if DataStructure.is_combined(type):
                        self._x = result
                    else:
                        self._x = result[0]
                        self._y = result[1]

    def get_x(self):
        if DataStructure.is_separated(self._data_type):
            return self._x
        else:
            new_type = DataStructure.switch_combine_separate(self._data_type)
            return convert_data_for_combined(self._x, self._data_type, new_type, self._len_of_x)[0]

    def get_y(self):
        if DataStructure.is_separated(self._data_type):
            return self._y
        else:
            new_type = DataStructure.switch_combine_separate(self._data_type)
            return convert_data_for_combined(self._x, self._data_type, new_type, self._len_of_x)[1]

    def get_data(self):
        if DataStructure.is_combined(self._data_type):
            return self._x
        else:
            new_type = DataStructure.switch_combine_separate(self._data_type)
            return convert_data_for_separated(self._x, self._y, self._data_type, new_type, self._len_of_x)

    def has_class(self):
        return self._has_class

    def dim(self):
        return self._dim

    def dim_for_y(self):
        return self._dimForY

    def get_type(self):
        return self._data_type

    def __repr__(self):
        if DataStructure.is_separated(self._data_type):
            return str(self._x) + '\n' + str(self._y)
        else:
            return str(self._x)

    def __str__(self):
        if DataStructure.is_separated(self._data_type):
            return str(self._x) + '\n' + str(self._y)
        else:
            return str(self._x)
