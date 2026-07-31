# Implement prime_list(n). Return a list of all prime numbers from 2 to n inclusive. A prime number has exactly two positive divisors. Students may need to research a simple primality test or the Sieve of Eratosthenes.

def prime_list(n):
    """Returns a list of all prime numbers from 2 to n inclusive."""
    if n < 2:
        return []

    # Initialize a boolean array "is_prime" corresponding to numbers 0 to n.
    # Initially, assume all numbers greater than or equal to 2 are prime.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Iterate from 2 up to the square root of n
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p as not prime, starting from p^2
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Filter and collect all numbers that are still marked as prime
    return [i for i, prime in enumerate(is_prime) if prime]