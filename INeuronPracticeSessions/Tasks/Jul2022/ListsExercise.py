from CList import Lists

a = Lists([1, 2, 3, [199, 299, 399, 499], [33, 44, 55, 66, 77]])
a.concat([100, 200, 300], [777, 333, 555], [0])
print(a.extract_list())

print(a.item)


print([{('a',): {'a': 'a'}}])
print([{None: {'a': 'a'}}])

my_list1 = Lists(['a'])
print("my_list1", my_list1.extract_string())

my_list2 = Lists(['a', ['b', 'c']])
print("my_list2", my_list2.extract_string())

my_list3 = Lists(['a', ['b', 'c'], ('e', 'f')])
print("my_list3", my_list3.extract_string())

my_list4 = Lists(['a', ['b', 'c'], ('e', 'f'), {'g', 'h'}])
print("my_list4", my_list4.extract_string())

my_list5 = Lists([1, 2, 3, 4.5, 4.0j, True, None])
print("my_list5", my_list5.extract_string())

my_list6 = Lists(['a', ['b', 'c', ('e', 'f', {'g', 'h'})]])
print("my_list6", my_list6.extract_string())

my_list7 = Lists([{'a': ['Apple', 1, 'Ant']}])
print("my_list7", my_list7.extract_string())

my_list8 = Lists([{('a', 'b', 1): ['Apple', 1, 'Ant']}])
print("my_list8", my_list8.extract_string())

my_list9 = Lists([{('a', 'b', 1, None): ['Apple', (1, {'Ant'})]}])
print("'my_list9':", my_list9.extract_string())

my_list10 = Lists([1, 2, 3, 4.5, 4.0j, True, None])
print("my_list10", my_list10.extract_numbers())

my_list11 = Lists([{'a': ['Apple', 1, 'Ant']}])
print("my_list11", my_list11.extract_numbers())

my_list12 = Lists([{('a', 'b', 1): ['Apple', 1, 'Ant']}])
print("my_list12", my_list12.extract_numbers())

my_list13 = Lists([{('a', 'b', 1, None): ['Apple', (1, {'Ant'})]}])
print("'my_list13':", my_list13.extract_numbers())

my_list14 = Lists([{('a', 'b', 1, None): ['Apple', (1, {'Ant'})]}])
print("'my_list14':", my_list14.extract_alnums())

my_list15 = Lists(['1', '2', 3, 4.5, 4.0j, True, None])
print("my_list15", my_list15.extract_alnums())

my_list16 = Lists([[1, 2, 3], ['4A', 5, 6], 99, [7, 8, 8], 'A'])
print("my_list16::", my_list16.arrays_product())

my_list17 = Lists([[1, 2, 3], ['4A', 5, (6, 99, {7, 8, 8})], {'A': {153}}, ('FAF', 'GAG')])
print("my_list17", my_list17.flatten_list())

my_list18 = Lists()
my_list18.push(112)
print("my_list18", my_list18.item)

my_list19 = Lists([[1, 2, 3], ['4A', 5, (6, 99, {7, 8, 8})], {'A': {153}}, ('FAF', 'GAG')])
print("Before 'my_list19':", my_list19.item)
my_list19.delete()
print("After 'my_list19':", my_list19.item)

x = {}
print("xx",x, type(x))

