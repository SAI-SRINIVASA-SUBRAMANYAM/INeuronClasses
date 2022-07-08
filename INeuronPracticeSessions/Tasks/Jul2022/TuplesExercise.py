from CTuple import Tuple

t1 = Tuple()
print(t1.item)

t2 = Tuple((1, 2, 3, 4))
print(t2.item)
print(t2.extract_string())


t2 = Tuple((1, ['T', 3, 'F', {5, 'S'}]))
print(t2.item)
print(t2.extract_string())
