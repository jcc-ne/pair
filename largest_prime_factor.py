import numpy as np


def largestprimefactor(number):
    for i in range(number, 1, -1):
        if number % i == 0:
            if prime_checker(i):
                return i


def primefactor(number):
    print number
    prime_list = []
    # for i in range(1,number + 1):
    for i in range(number, 1, -1):
        print 'i', i
        if number % i == 0:
            if prime_checker(i):
                prime_list.append(i)
    return prime_list



def prime_checker(num):
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


def elemetarySchoolWay(number):
    lastdigit = int(str(number)[-1])
    print 'last', lastdigit

    if lastdigit in [0, 2, 4, 5, 6, 8]:
        return 'easy case'
    elif lastdigit == 3:
        listnum = [int(k) for k in list(str(number))]


# Solution #2
import math

def max_prime_factor(number):
    for divisor in range(2, int(math.sqrt(number + 1))):
        if (number % divisor == 0):
            return(max(divisor, max_prime_factor(number/divisor)))
    return(number)


# Solution #3
num = 600851475143
n_primes = 10**5
no_prime = set(j for i in range(2, n_primes) for j in range(i*2,n_primes,i ) )
prime = [j for j in range(2,n_primes) if (j not in no_prime)]

p_great = 2
for i in prime:
    if num%i ==0:
        if num > p_great:
            p_great = i
print(p_great)

# Solution #4
def largestPrimeFactor(n):
    candidate = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prime_checker(n//i):


def largestPrimeFactor(n):
        i = 1
        while i <= n ** 0.5:
            # keep knocking down the same factor
            if n % i == 0:
                n = n // i
            else:
                i += 1
        return n
