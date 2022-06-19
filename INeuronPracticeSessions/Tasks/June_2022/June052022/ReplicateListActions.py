# Try to write a function which is a replica of list append , extend and pop function
def extend_list(src=[], dest=[]):
    '''Extends the given source list with destination list.'''
    if type(src) != list:
        raise Exception('Given source is not a list type')
    elif type(dest) != list:
        raise Exception('Given destination is not a list type')
    src += dest

def append_list(value, l: list):
    '''Appeneds a character at the end of given list'''
    if type(l) != list:
       raise Exception('Invalid parameter, need provide a list type')
    s = len(l)
    l[s:] = [value]

def pop_list(l):
    '''Deletes an element from the end of the list'''
    s = len(l) - 1
    if (len(l)):
        del l[s]
        return s
    else:
        raise Exception('Delete operation can not be performed on empty list.')

if __name__ == '__main__':
    try:
        fruits = ['apple', 'mango']
        veggies = ['mango', 'banana', 'carrot']
        extend_list(fruits, veggies)
        print(fruits)
        # extend_list([], "") # Exception case
    except Exception as e:
        print(e)
    try:
        append_list('orange', fruits)
        print(fruits)
        append_list('pine apple', fruits)
        print(fruits)
        append_list(None, fruits)
        print(fruits)
        append_list(0, fruits)
        print(fruits)
        append_list(False, fruits)
        print(fruits)
        # append_list('pine apple', "") # Exception case
        print(fruits)
    except Exception as e:
        print(e)
    try:
        # 0
        pop_list(fruits)
        # 1
        pop_list(fruits)
        # 2
        pop_list(fruits)
        # 3
        pop_list(fruits)
        # 4
        pop_list(fruits)
        # 5
        pop_list(fruits)
        # Check
        print(fruits)
        # 6
        pop_list(fruits)
        # 7
        pop_list(fruits)
        # 8
        pop_list(fruits)
        # 9
        pop_list(fruits)
        # Check
        print(fruits)
        pop_list(fruits) # Exception case
    except Exception as e:
        print(e)