# Implement prime_list(n). Return a list of all prime numbers from 2 to n inclusive. A prime number has exactly two positive divisors. Students may need to research a simple primality test or the Sieve of Eratosthenes.
def prime_list(n):
    primes = []

    for num in range(2, n + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            primes.append(num)

    return primes