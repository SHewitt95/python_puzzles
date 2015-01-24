import time
'''
The function isprime(n) was found at this website:
https://www.daniweb.com/software-development/python/
code/216880/check-if-a-number-is-a-prime-number-python
'''

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs
    # to go up to the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def find_prime(goal):
    counter = 0
    n = 2 # First prime number
    while (True):
        if (not isprime(n)):
            n += 1
        else:
            counter += 1
            if (counter == goal):
                return n
            n += 1

start = time.time()
solution = find_prime(10001)
final_time = (time.time() - start) * 1000 # Time in milliseconds

print("Found prime number %s in %s milliseconds." %(solution, final_time))
