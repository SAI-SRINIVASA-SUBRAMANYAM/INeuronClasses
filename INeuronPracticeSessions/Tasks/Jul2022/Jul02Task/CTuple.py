from Utils.helper import custom_definition, \
    get_type, \
    is_required_type, \
    extract_specific_type_from_list
from CustomException import CExcept
from CustomLogging import Logger


class Tuple:
    __required_type = custom_definition(tuple)

    def __init__(self, value=tuple()):
        """
        This function takes input as tuple and assign it to its class variable. \n
        :param value: tuple
        """
        item = self.__is_tuple_type(value)
        self.item = item

    def extract_string(self):
        """
        Extract all the string from given tuple.\n
        """
        if len(self.item) == 0:
            Logger(f"Unable to extract strings from empty tuple")
        else:
            return extract_specific_type_from_list(self.item, custom_definition(str), [])

    def __is_tuple_type(self, param):
        if not is_required_type(param, self.__required_type):
            message = f"Expected '{self.__required_type}' but received type of '{get_type(param)}'."
            CExcept(message)
        return param

