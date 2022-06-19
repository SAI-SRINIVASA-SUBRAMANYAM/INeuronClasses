# Try to write a 10 different example of lambda function with a choice of your task
from datetime import datetime
import math
# Examples
# 1
# Description: Sum of n natural numbers
sum_of_n_natural_nums = lambda n: n*(n+1)/2
print("Sum of given natural numbers are: ", sum_of_n_natural_nums(10))

# 2
# Description: Check whether given number even or not. Return True if even else false
is_even = lambda n: True if type(n) in[int, float] and n%2 == 0 else False
print('Ten is Even number: ', is_even(10))
print('Nine is Even number: ', is_even(9))

# 3
# Description: Check whether given string contains vowels or not if contains True else false
contains_vowels = lambda s: True in {c.lower() in "aeiou" for c in str(s)}
print("Does your word contains vowels? ", contains_vowels("rainbow"))

# 4
# Description: Capitalize each word fo a scentence.
capitalize_words = lambda s: " ".join([w.capitalize() for w in s.split(" ")])
print("Capitalize each word from given sentence", capitalize_words("This is a test message"))

# 5
# Description: Get system date time in string format
get_sys_datetime = lambda : datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
print("Current system date and time:", get_sys_datetime())

# 6
# Description: Flat the 2 dimensional array
flatten_2d_arr = lambda a: [s for x in a for s in x]
print("Flattened two dimensional array list:", flatten_2d_arr([[1, 2], [3, 4], [5, 6]]))

# 7
# Description: Get nearest square root for given number
sq_root_n = lambda n : math.log10(n)/math.log10(2)
print("Nearest square root of given number: ",sq_root_n(16))

# 8
# Description: Get area of a circle
area_of_circle = lambda r: math.pi * (r**2)
print("Area of a circle for given radius: ", area_of_circle(10))

# 9
# Description: Find whether given number is palindrome or not
is_palindrome = lambda s: s.lower() == s.lower()[::-1]
print("Given word is palindrome? ", is_palindrome("malayalam"))

# 10
# Description: Exclude specific keys from dictionary
generate_new_dict = lambda d, xKeys: { key: value for key, value in d.items() if key not in xKeys }
person = {
    "name": "some name",
    "age": 99,
    "demograph": {
        "address1": "some address",
        "address2": "some address"
    },
    "mobile": 911992299,
    "aadhar": 'XXXX-YYYY-ZZZZ-AAAA'
}
print("Generate new dictonary by excluding specific keys", generate_new_dict(person, ['mobile', 'aadhar']))

