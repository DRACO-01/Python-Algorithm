def extended_gcd(a, b):
    """
    Extended Euclidean algorithm.
    Returns a tuple of (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)


def mod_inverse(a, mod):
    """
    Computes the modular inverse of a under modulo mod using the extended Euclidean algorithm.
    Returns the inverse if it exists, otherwise raises an Exception.
    """
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise Exception(f'Modular inverse does not exist for a = {a} and mod = {mod}')
    else:
        return x % mod


# Example usage:
if __name__ == "__main__":
    a = 3
    mod = 11
    print(f"Modular inverse of {a} mod {mod} =", mod_inverse(a, mod))
