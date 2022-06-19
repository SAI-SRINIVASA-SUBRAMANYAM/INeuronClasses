# Try to write a function which  is equivalent  to print function in python
import sys

w = sys.stdout.write
err = sys.stderr.write
is_primitive_type = lambda data: type(data) in [str, int, float, bool]
is_linear_collection = lambda data: type(data) in [list, tuple, set]
is_dict_collection = lambda data: type(data) in [dict]


def get_tags(t):
    if t == list:
        return ("[", "]")
    elif t == tuple:
        return ("(", ")")
    elif t == dict or t == set:
        return ("{", "}")
    else:
        return ("", "")


def get_dict_collection_content(data: dict, content_type):
    """Parsing the dictonary data"""
    open_symbol, closing_symbol = get_tags(content_type)
    content = open_symbol
    for key, value in data.items():
        key = "'" + str(key) + "'" if type(key) == str else "" + str(key) + ""
        if (content != open_symbol):
            content += ", "

        if (is_primitive_type(value)):
            t_val = "'" + value + "'" if type(value) == str else str(value)
            tmp = key + ": " + t_val
            content += (tmp)
        elif (is_linear_collection(value)):
            tmp = key + ": " + get_linear_collection_content(value, type(value))
            content += tmp
        elif (is_dict_collection(value)):
            tmp = key + ": " + get_dict_collection_content(value, type(value))
            content += tmp
    content += closing_symbol
    return content


def get_linear_collection_content(data, content_type):
    """Parsing the list, tuple, set collection content"""
    open_symbol, closing_symbol = get_tags(content_type)
    content = open_symbol
    for d in data:
        if (content != open_symbol):
            content += ", "

        if (is_primitive_type(d)):
            content += "'" + str(d) + "'" if type(d) == str else "" + str(d) + ""
        elif (is_linear_collection(d)):
            content += get_linear_collection_content(d, type(d))
        elif (is_dict_collection(d)):
            content += get_dict_collection_content(d, type(d))
    content += closing_symbol
    return content


def my_print(*args, sep = " ", end =""):
    content = ""
    for arg in args:
        if (content != ""):
            content += sep
        if (is_primitive_type(arg)):
            content += str(arg)
        elif (is_linear_collection(arg)):
            content += get_linear_collection_content(arg, type(arg))
        elif (is_dict_collection(arg)):
            content += get_dict_collection_content(arg, type(arg))
    w(content + end)

if __name__ == '__main__':
    my_print({"a": [1,2,3], "b": '456'},[99,88,77],(0,1,0),{5,"5",5}, sep="\n", end="\n")
    print()
    print({"a": [1,2,3], "b": '456'},[99,88,77],(0,1,0),{5,"5",5}, sep="\n", end="\n")