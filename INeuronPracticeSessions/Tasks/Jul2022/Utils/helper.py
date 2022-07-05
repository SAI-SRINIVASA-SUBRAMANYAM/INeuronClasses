def custom_definition(cType):
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
    return object_definition.get(cType, "Unknown")


def get_type(obj):
    return "None" if obj is None else custom_definition(type(obj))


def is_required_type(src, dest_type):
    return get_type(src) == dest_type
