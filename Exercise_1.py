'''
Group Anagrams

Given an array of strings, group anagrams together.

Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"], Output: [ ["ate","eat","tea"], ["nat","tan"], ["bat"] ]

Note: All inputs will be in lowercase. The order of your output does not matter.

Solution:
1. For each word, count the frequency of each character in the word to generate a 26-length key. Use the key to store the word in a hashmap.
Time: O(MN), Space: O(N) (M = no of words in the input list, N = len of longest word)

'''
from collections import defaultdict

def make_array_of_character_counts(w):
    d = [0]*26

    for c in w: # O(N), N = len of characters in word w
        try:
            d[ord(c)-ord('a')] += 1
        except Exception as e:
            print(f"Invalid word = '{w}' contains a character '{c}' that is not a-z")
            return ""
    counts = [str(d[k]) for k in range(26)]
    key = "".join(counts)
    return key

def group_anagrams(W):
    counts2words = defaultdict(list)
    for w in W: # O(M) = no. of words in the list
        key = make_array_of_character_counts(w) # O(N)
        if key:
            counts2words[key].append(w)
    return list(counts2words.values())

def run_group_anagrams():
    W = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "cinema", "dad", "triangle", "add", "silent", "integral", "anemic", "altering", "a", " a"]
    print(f"List of words = {W}")
    print(f"Grouped anagrams: {group_anagrams(W)}")

run_group_anagrams()
