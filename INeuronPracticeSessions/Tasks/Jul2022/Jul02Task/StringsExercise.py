from CString import String

# Case 1: All the cases
s1 = String("As")
print(s1.len())
print(s1.reverse())
print(s1.format('u'))
print(s1.format('l'))
print(s1.format('c'))
print(s1.concat(": {122}"))
print(s1.text)

# Case 2: Operator overloading
s2 = String("ab")
print(s1+s2)

# case 3: Exception handling
try:
    s3 = String(1)
except Exception as e:
    print(e)

try:
    s4 = String("")
    print(s4.len())
except Exception as e:
    print(e)

try:
    s5 = String("")
    print(s5.reverse())
except Exception as e:
    print(e)

try:
    s6 = String("A")
    print(s6.concat(""))
except Exception as e:
    print(e)


try:
    s7 = String("A")
    print(s7.concat(1))
except Exception as e:
    print(e)


try:
    s7 = String("Hello world")
    print(s7.format(''))
except Exception as e:
    print(e)

try:
    s8 = String("Hello world")
    print(s8.format('x'))
except Exception as e:
    print(e)


