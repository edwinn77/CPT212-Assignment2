# Python3 Implementation of Boyer-Moore String Matching Algorithm with Bad Character Heuristic

# Number of possible characters in the input
NO_OF_CHARS = 256

def bad_char_heuristic(pattern, size):
    """
    Preprocessing function to create the bad character heuristic table.
    """
    # Initialize all occurrences to -1
    bad_char = [-1] * NO_OF_CHARS

    # Fill the table with the last occurrence of each character in the pattern
    for i in range(size):
        bad_char[ord(pattern[i])] = i

    return bad_char

def boyer_moore_search(text, pattern):
    """
    Boyer-Moore pattern searching algorithm that uses the bad character heuristic.
    """
    m = len(pattern)
    n = len(text)

    # Generate the bad character heuristic table for the pattern
    bad_char = bad_char_heuristic(pattern, m)

    # Initialize the shift of the pattern with respect to the text
    s = 0
    while s <= n - m:
        j = m - 1

        # Keep reducing the index j of the pattern while characters of the pattern and text match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # If the pattern is found at the current shift
        if j < 0:
            print(f"Pattern found at index {s}")

            # Shift the pattern to align with the next character in the text
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            # Shift the pattern to align the bad character with its last occurrence in the pattern
            s += max(1, j - bad_char[ord(text[s + j])])

# Example usage
def main():
    text = "ABAAABCD"
    pattern = "ABC"
    boyer_moore_search(text, pattern)

if __name__ == '__main__':
    main()
