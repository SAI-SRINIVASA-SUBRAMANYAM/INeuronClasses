# Try to print a prime number in between 1 to 1000
def is_prime_number(num: int):
    '''Validate whether give number is prime or not!'''
    m = num // 2 + 1
    for j in range(2, m):
        if (num % j == 0):
            return False
    return True


def find_prime_numbers(n: int):
    '''Find the prime number 1 to n numbers'''
    if type(n) != int:
        raise Exception('Invalid input, '+str(n))
    elif n <= 1:
        yield None
    elif n == 2:
        yield 2
    else:
        for i in range(2, n + 1):
            if (is_prime_number(i)):
                yield i

if __name__ == '__main__':
    try:
        for i in find_prime_numbers(10):
            if i: print(i, end=", ")
    except Exception as e:
        print(e)