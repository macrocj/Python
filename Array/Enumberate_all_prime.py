# Author: JC
# Date: 7/23/2018
# Version: 1.0

import time


def timeduring(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total processing time: ", float(end - start))

    return wrapper


@timeduring
def generate_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    print(primes)
    return primes


print(generate_primes(10000))



def try_generate_prime(n):
    primes = []
    is_prime = [False, False] + [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for p in range(i, n + 1, i):
                is_prime[i] = False
    return primes

@timeduring
def generate_prime_adv(n):
    if n<2:
        return []
    size =(n -3) // 2 + 1
    primes = [2]
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(2 * i ** 2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes

print(generate_prime_adv(10000))