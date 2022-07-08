from CSets import Set

s1 = Set()
print(s1.item)

s2 = Set({1, '2', 3, 4, 'Bool'})
print(s2.item)

s3 = Set({'A', 2, 3.4, 'D', 3, 'E'})
print(s3.extract_string())
