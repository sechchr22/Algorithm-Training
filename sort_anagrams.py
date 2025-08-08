from collections import defaultdict
import pdb

def group_anagrams(strs):
    pdb.set_trace()
    #defaultdict allows to create an empty dict (no keys) with a default value
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    pdb.set_trace()
    return list(anagram_map.values())

# Example usage
if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


