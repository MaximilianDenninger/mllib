

class DataStructure(object):
    RC = 1  # row combined
    RS = 2  # row separated
    CC = 3  # column combined
    CS = 4  # column separated

    def __setattr__(self, *_):
        pass

    @staticmethod
    def is_valid(type):
        return type == DataStructure.RC or type == DataStructure.RS or type == DataStructure.CC or type == DataStructure.CS

    @staticmethod
    def is_separated(type):
        return type == DataStructure.RS or type == DataStructure.CS

    @staticmethod
    def is_combined(type):
        return type == DataStructure.RC or type == DataStructure.CC

    @staticmethod
    def switch_combine_separate(type):
        if type == DataStructure.RC:
            return DataStructure.RS
        elif type == DataStructure.RS:
            return DataStructure.RC
        elif type == DataStructure.CC:
            return DataStructure.CS
        elif type == DataStructure.CS:
            return DataStructure.CC

    @staticmethod
    def is_column(type):
        return type == DataStructure.CC or type == DataStructure.CS

    @staticmethod
    def is_row(type):
        return type == DataStructure.RC or type == DataStructure.RS