from Utils.helper import is_required_type, \
    custom_definition, \
    get_type, \
    extract_specific_type_from_list, \
    array_product, \
    list_flatten
from CustomException import CExcept
from CustomLogging import Logger


class Lists:
    __required_type = custom_definition(list)

    def __init__(self, item: list = []):
        """
        This function takes input as array and assign it to its class variable.
        :param item: list
        """
        res = self.__is_list_type(item)
        self.item = res

    def push(self, value):
        """
        This function appends the value at the end of the list.\n
        :param value: any
        :return: None
        """
        if self.item is None:
            self.item = [value]
        elif get_type(self.item) == custom_definition(list):
            self.item += [value]

    def concat(self, *lists) -> list:
        """
        This extends the given list into existing list.\n
        :param lists: list
        :return: list
        """
        if lists is None:
            message = f"Excepting parameters to be of list type."
            CExcept(message)
        else:
            for lst in lists:
                res_l = self.__is_list_type(lst)
                self.item += res_l

    def delete(self):
        """
        This function deletes the value at the end.
        :return:
        """
        length = len(self.item)
        if length == 0:
            CExcept("Cannot delete the element from empty list.")
        else:
            index = length - 1
            value = self.item[index]
            del self.item[index]
            return value
        return None

    def extract_list(self):
        """
        This extracts inner list from existing heterogeneous list items.\n
        :return: list
        """
        extracted_item = []
        for lst in self.item:
            if get_type(lst) == self.__required_type:
                extracted_item.append(lst)
        if len(extracted_item) == 0:
            Logger('There is no list type inside the given parameter')
        return extracted_item

    def extract_string(self):
        """
        This function extracts all string type value from existing list or inner objects.\n
        :return: list
        """
        string_type = custom_definition(str)
        return extract_specific_type_from_list(self.item, string_type, [])

    def extract_numbers(self):
        """
        This function extracts number from given heterogeneous collection.\n
        :return: list
        """
        int_type = custom_definition(int)
        return extract_specific_type_from_list(self.item, int_type, [])

    def extract_alnums(self):
        """
        This function extracts all the string & numeric data.\n
        :return: list
        """
        a = self.extract_string()
        b = self.extract_numbers()
        return a + b

    def arrays_product(self):
        """
        This function calculate the production of numbers inside of arrays.\n
        Supports up to 2 - level.\n
        :return: list
        """
        p = []
        try:
            for i in self.item:
                if get_type(i) == custom_definition(list):
                    print(i, array_product(i))
                    p.append(array_product(i))
                elif get_type(i) in [custom_definition(int), custom_definition(float)]:
                    p.append(i)
                else:
                    p.append(0)
        except Exception as e:
            CExcept(e)
        return p

    def flatten_list(self):
        """
        This function scan the list of object and make a flat array.\n
        :return: list
        """
        return list_flatten(self.item, [])

    def __is_list_type(self, param):
        if not is_required_type(param, self.__required_type):
            message = f"Expected '{self.__required_type}' but received type of '{get_type(param)}'."
            CExcept(message)
        return param
