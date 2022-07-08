from functools import reduce


def custom_definition(c_type):
    object_definition = {
        str: 'String',
        int: 'Int',
        float: 'Float',
        set: 'Set',
        tuple: 'Tuple',
        dict: 'Dict',
        list: 'List',
        bool: 'Boolean',
        complex: 'Complex'
    }
    return object_definition.get(c_type, "Unknown")


def get_type(obj):
    return "None" if obj is None else custom_definition(type(obj))


def is_required_type(src, dest_type):
    return get_type(src) == dest_type


def is_primitive_type(obj):
    return obj is None or type(obj) in [int, float, bool, str, complex]


def extract_specific_type_from_dict(d: dict, destination_type, p_s_arr: list):
    s_arr = p_s_arr
    for key, value in d.items():
        if get_type(key) == destination_type:
            s_arr.append(key)
        elif get_type(key) == custom_definition(tuple):
            extract_specific_type_from_list(key, destination_type, s_arr)

        if get_type(value) == destination_type:
            s_arr.append(value)
        elif get_type(value) == custom_definition(dict):
            extract_specific_type_from_dict(value, destination_type, s_arr)
        elif get_type(value) in [custom_definition(list), custom_definition(tuple), custom_definition(set)]:
            extract_specific_type_from_list(value, destination_type, s_arr)
    return s_arr


def extract_specific_type_from_list(ls, destination_type, p_s_arr: list = []):
    s_arr = p_s_arr
    for l in ls:
        if get_type(l) == destination_type:
            s_arr.append(l)
        elif get_type(l) in [custom_definition(list), custom_definition(tuple), custom_definition(set)]:
            extract_specific_type_from_list(l, destination_type, s_arr)
        elif get_type(l) == custom_definition(dict):
            extract_specific_type_from_dict(l, destination_type, s_arr)
    return s_arr


def product_m_n(m, n):
    """
    This function calculate product of two numbers\n
    :param m: int | float
    :param n: number: int | float
    :return: number: int | float
    """
    if get_type(m) not in [custom_definition(int), custom_definition(int)]:
        raise Exception(f"Given parameters {m} or not valid numeric")
    elif get_type(n) not in [custom_definition(int), custom_definition(int)]:
        raise Exception(f"Given parameters {n} or not valid numeric")
    return m * n


def array_product(num_array):
    """
    This function calculates the product of sub array.\n
    :param num_array: list
    :return: int | float
    """
    if get_type(num_array) != custom_definition(list):
        raise Exception(f"Given parameter '{num_array}' is not of type list.")
    p = 0
    try:
        p = reduce(product_m_n, num_array)
    except Exception as e:
        pass
    return p


def dict_flatten(d, p_result):
    result = p_result
    for key, value in d.items():
        if is_primitive_type(key):
            result.append(key)
        elif get_type(key) == custom_definition(tuple):
            list_flatten(key, result)

        if is_primitive_type(value):
            result.append(value)
        elif get_type(value) in [custom_definition(list), custom_definition(tuple), custom_definition(set)]:
            list_flatten(value, result)
        elif get_type(value) == custom_definition(dict):
            dict_flatten(value, result)
    return result


def list_flatten(arr, p_result):
    result = p_result
    for a in arr:
        if is_primitive_type(a):
            result.append(a)
        elif get_type(a) in [custom_definition(list), custom_definition(tuple), custom_definition(set)]:
            list_flatten(a, result)
        elif get_type(a) == custom_definition(dict):
            dict_flatten(a, result)
    return result


def gather_keys(d, p_keys):
    r_keys = p_keys
    if get_type(d) == custom_definition(dict):
        r_keys += list(d.keys())
        values = list(d.values())
        for value in values:
            gather_keys(value, r_keys)
    return r_keys