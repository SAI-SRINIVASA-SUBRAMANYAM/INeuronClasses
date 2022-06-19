def is_prime_number(p):
    '''Validate whether given number is prime or not'''
    m = p // 2 + 1
    for j in range(2, m):
        if (p % j) == 0:
            return False
    return True

def get_prime_numbers(n):
    '''Get the prime number between 1 to n'''
    if n <= 1:
        return
    elif n == 2:
        yield n
    for i in range(2, n+1):
        if is_prime_number(i):
            yield i

if __name__ == '__main__':
    for i in get_prime_numbers(31):
        print(i, end = ", ")