def mod_exp(base, exponent, mod):
    """
    Computes (base^exponent) % mod using an iterative method.
    Complexity: O(log(exponent))
    """
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2:  # if exponent is odd
            result = (result * base) % mod
        exponent //= 2
        base = (base * base) % mod
    return result


# Example usage:
if __name__ == "__main__":
    print("3^200 mod 13 =", mod_exp(3, 200, 13))
