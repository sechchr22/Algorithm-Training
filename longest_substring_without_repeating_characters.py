# Find the longest substring without repeating characters

def longest_substring_without_repeating_character(s: str) -> str:
    if len(s) == 0 or len(s) == 1:
        return s

    unrepeated_substrings = []
    buf = ""
    i = 0
    y = 0
    while i < len(s):
        if s[i] in buf:
            unrepeated_substrings.append(buf)
            buf = ''
            y += 1
            i = y
        else:
            buf += s[i]
            i += 1
    unrepeated_substrings.append(buf)

    longest = ''
    for substring in unrepeated_substrings:
        if len(substring) > len(longest):
            longest = substring
    
    return longest

if __name__ == "__main__":
    # Test cases
    print(longest_substring_without_repeating_character("abcabcbb"))  # "abc"
    print(longest_substring_without_repeating_character("bbbbb"))     # "b"
    print(longest_substring_without_repeating_character("pwwkew"))    # "wke"
    print(longest_substring_without_repeating_character(""))           # ""
    print(longest_substring_without_repeating_character("a"))          # "a"
    print(longest_substring_without_repeating_character("dvdf"))       # "vdf"