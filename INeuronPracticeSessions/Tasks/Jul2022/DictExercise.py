from CDist import Dictionary

d1 = Dictionary()
print(d1.item)

d2 = Dictionary({'a': 'Apple', 'b': ['ball', 'bat'], 'e': ('enum', 'education'), 'f': {5, 55, 56}, 'g': {'go': 'language'}, 'h': 9.88})
print(d2.extract_numeric())

# d3 = Dictionary({'a': {'apple', {'b': 'banana', 'c': 'carrot'}}, '1': 'One', '2': 'Bi', ('Three', 'Four'): 'Hitting'})
d3 = Dictionary({'a': {'apple': {'b': 'banana', 'c': 'carrot'}}, 1: 'One', 2: 'Bi', ('Three', 'Four'): 'Hitting'})
keys, count = d3.get_total_keys()
print(f"There are total {count} key(s), of {keys}.")

