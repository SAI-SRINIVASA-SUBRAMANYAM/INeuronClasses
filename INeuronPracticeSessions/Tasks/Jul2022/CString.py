from Utils.helper import custom_definition, get_type, is_required_type
from CustomException import CExcept
from CustomLogging import Logger


class String:
    __required_type = custom_definition(str)

    def __init__(self, text: str):
        """
        Validate the given string and declare.\n
        :param text: string
        """
        result = self.__is_string_type(text)
        self.text = result

    def __add__(self, other):
        return self.text + other.text

    def ____(self):
        return self.text

    def len(self):
        """
        Return the length of a string.\n
        :return: int
        """
        _l = len(self.text)
        if _l == 0:
            Logger("Length of the given text is empty", 'i')
        return _l

    def reverse(self):
        """
        Reverse the given string when not blank.\n
        :return: str/None
        """
        if len(self.text) == 0:
            message = "Reverse operation cannot be performed on empty string"
            CExcept(message)
        return self.text[::-1]

    def format(self, style: str):
        """
        Format the text to specified style.\n
        Style: 'l' is Lower, 'u' is Upper, 'c' is capitalize
        :return: str/None
        """
        if len(self.text) == 0:
            _format_len_error = "Format operation cannot be performed on empty string"
            CExcept(_format_len_error)
        elif style == "":
            _format_style_error = "Formatting, style can not be blank."
            CExcept(_format_style_error)
            return None
        elif style[0] in ['C', 'c']:
            return self.text.capitalize()
        elif style[0] in ['U', 'u']:
            return self.text.upper()
        elif style[0] in ['L', 'l']:
            return self.text.lower()
        else:
            _format_error_message = "Expected style to be 'l', 'u', 'c'."
            CExcept(_format_error_message)

    def concat(self, destination_text: str):
        """
        Concatenate given new string to existing string.\n
        :param destination_text: str\n
        :return: str/None
        """
        if destination_text == "":
            Logger(f"To concatenate destination string is blank/empty", 'w')
        else:
            self.__is_string_type(destination_text)

        return self.text + destination_text

    def __is_string_type(self, param):
        if not is_required_type(param, self.__required_type):
            message = f"Expected '{self.__required_type}' but received type of '{get_type(param)}'."
            CExcept(message)
        return param

