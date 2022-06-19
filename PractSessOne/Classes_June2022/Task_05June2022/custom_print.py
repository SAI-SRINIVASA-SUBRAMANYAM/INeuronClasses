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
        if (is_linear_collection(key) or is_dict_collection(key)):
            err("Key is not a hashable type")
            sys.exit("Invalid key exception")

        key = "'" + str(key) + "'" if type(key) == str else "" + str(key) + ""
        if (content != open_symbol):
            content += ", "

        if (is_primitive_type(value)):
            t_val = "'" + value + "'" if type(value) != str else str(value)
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


def my_print(*args, **kwargs):
    sep = kwargs.get("sep") or " "
    end = kwargs.get("end") or ""
    d_args = dict()
    if (len(kwargs) > 0):
        d_args = {key: value for key, value in kwargs.items() if key not in ["end", "sep"]}
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


my_print({"a": [1,2,3], "b": '456'},[99,88,77],(0,1,0),{5,"5",5})
print({"a": [1,2,3], "b": '456'},[99,88,77],(0,1,0),{5,"5",5})