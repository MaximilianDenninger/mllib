import numpy as np
from .datastructure import DataStructure
import utilities


def convert_data_for_combined(data, current_type, desired_type, len_of_x):
    if current_type == desired_type:
        return data
    if DataStructure.is_valid(desired_type) and DataStructure.is_combined(current_type):
        if DataStructure.is_combined(desired_type):
            return data.transpose()  # both are combined, just transpose the content
        else:
            if DataStructure.is_row(current_type) and DataStructure.is_row(desired_type):  # perform split
                return np.append(data[:, :len_of_x], data[:, len_of_x:])  # split data
            elif DataStructure.is_column(current_type) and DataStructure.is_column(desired_type):  # perform split
                return np.append(data[:len_of_x, :], data[len_of_x:, :])  # split data
            else:  # last option (both change)
                switched_type = DataStructure.switch_combine_separate(current_type)
                temp_split = convert_data_for_combined(data, current_type, switched_type, len_of_x)  # split data
                return convert_data_for_separated(temp_split[0], temp_split[1], switched_type, desired_type,
                                                  len_of_x)  # transpose it
    else:
        utilities.print_error("This type is unknown!")
        return None


def convert_data_for_separated(data, labels, current_type, desired_type, len_of_x):
    same_dim = 1 if DataStructure.is_row(current_type) else 0
    if data.shape[same_dim] != labels.shape[same_dim]:
        utilities.print_error("The labels and data don't have the same amount!")
    if current_type == desired_type:
        return data
    if DataStructure.is_valid(desired_type) and DataStructure.is_separated(current_type):
        if DataStructure.is_separated(desired_type):
            return [data.transpose(), labels.transpose()]  # both are separated, just transpose the content
        else:
            if DataStructure.is_row(current_type) and DataStructure.is_row(desired_type):  # combine data
                new_data = np.zeros([data.shape[0] + labels.shape[0], data.shape[1]])
                new_data[:len_of_x, :] = data
                new_data[len_of_x:, :] = labels
                return new_data
            elif DataStructure.is_column(current_type) and DataStructure.is_column(desired_type):  # combine data
                new_data = np.zeros([data.shape[0], data.shape[1] + labels.shape[1]])
                new_data[:, :len_of_x] = data
                new_data[:, len_of_x:] = labels
                return new_data
            else:  # last option (both change)
                switched_type = DataStructure.switch_combine_separate(current_type)
                temp_combined = convert_data_for_separated(data, labels, current_type, switched_type,
                                                           len_of_x)  # combine data
                return convert_data_for_combined(temp_combined, switched_type, desired_type, len_of_x)  # transpose it
    else:
        utilities.print_error("This type is unknown!")
        return None
