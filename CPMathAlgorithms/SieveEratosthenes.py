def sieve_of_eratosthenes(n):
    """
    Returns a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes.
    """
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]


# Example usage:
if __name__ == "__main__":
    n = 50
    primes = sieve_of_eratosthenes(n)
    print(f"Primes up to {n}:", primes)
