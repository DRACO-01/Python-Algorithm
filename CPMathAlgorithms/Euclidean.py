def gcd(a, b):
    """
    Computes the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a


# Example usage:
if __name__ == "__main__":
    print("gcd(48, 18) =", gcd(48, 18))
