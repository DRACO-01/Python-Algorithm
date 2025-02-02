def mod_inverse_fermat(a, p):
    """
    Computes the modular inverse of a under modulo p using Fermat's Little Theorem.
    p must be a prime number.
    Returns a^(-1) mod p.
    """
    return pow(a, p - 2, p)


# Example usage:
if __name__ == "__main__":
    a = 3
    p = 11  # prime modulus
    print(f"Modular inverse of {a} mod {p} =", mod_inverse_fermat(a, p))
