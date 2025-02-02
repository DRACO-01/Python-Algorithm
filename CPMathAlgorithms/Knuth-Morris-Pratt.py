def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for KMP algorithm.
    lps[i] is the length of the longest proper prefix which is also a suffix for pattern[0...i].
    """
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # try the previous longest prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Searches for occurrences of `pattern` in `text` using the KMP algorithm.
    Returns a list of starting indices where pattern is found.
    """
    if not pattern:
        return []

    lps = compute_lps(pattern)
    result = []
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


# Example usage:
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(text, pattern)
    print("Pattern found at indices:", matches)
