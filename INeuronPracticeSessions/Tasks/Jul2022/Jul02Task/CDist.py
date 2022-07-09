from Utils.helper import get_type,\
    is_required_type,\
    custom_definition, \
    extract_specific_type_from_dict, \
    gather_keys
from CustomException import CExcept
from CustomLogging import Logger


class Dictionary:
    __required_type = custom_definition(dict)

    def __init__(self, value: dict = {}):
        """
        This function takes input as dictionary and assign it to its class variable. \n
        :param value: dict
        """
        item = self.__is_dict_type(value)
        self.item = item

    def extract_numeric(self):
        """
        Extract the numeric from given dictionary.\n
        :return: list
        """
        result = None
        if len(self.item.keys()) == 0:
            Logger(f"Can not extract data from empty dictionary")
        else:
            try:
                result_int = extract_specific_type_from_dict(self.item, custom_definition(int), [])
                result_float = extract_specific_type_from_dict(self.item, custom_definition(float), [])
                result = result_float + result_int
            except Exception as e:
                CExcept(e)
            return result

    def get_total_keys(self):
        """
        Extract the total number of keys from given dictionary.\n
        :return: (keys, count)
        """
        count = len(list(self.item.keys()))
        if count == 0:
            Logger(f"Unable fetch keys from empty dictionary")
        else:
            keys = gather_keys(self.item, [])
            t_count = len(keys)
            return keys, t_count

    def __is_dict_type(self, param):
        if not is_required_type(param, self.__required_type):
            message = f"Expected '{self.__required_type}' but received type of '{get_type(param)}'."
            CExcept(message)
        return param
