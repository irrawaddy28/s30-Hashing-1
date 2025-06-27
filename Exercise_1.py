'''
Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings, group anagrams together.

Example: Input: ["eat", "tea", "tan", "ate", "nat", "bat"], Output: [ ["ate","eat","tea"], ["nat","tan"], ["bat"] ]

Note: All inputs will be in lowercase. The order of your output does not matter.

Let N = no of words in the input list, M = len of longest word

Solution:
1. Brute Force: For each word in array, sort the chars and compare the sorted char sequence with the sorted char seq of all the other words. In other words,
group = []
for i = 0:N-1: # O(N)
    word1 = array[i]
    char_seq1 = sorted(word1) # M log M
    group.append(word1)
    for j = i+1:N-1: # O(N)
        word2 = array[j]
        char_seq2 = sorted(word2) # M log M
         if char_seq1 == char_seq2: # O(M)
            group.append(word2)
Time: O( (NM log M) * NM^2 log M), Space: O(N)

2. Frequency count as hash map key: For each word, count the frequency of each character in the word to generate a 26-length key. Use the key to store the word in a hashmap.
Time: O(NM), Space: O(N)
Why is space O(N)? We could potentially have a case where there are
no anagrams in the input array of strings which results in a hash table of
size O(N)

3. Prime product as hash map key: Create a character to prime number map (a: 1, b:2, c:3, d:5, e:7, ...). For each word, get the characters and their corresponding prime numbers and compute the prime product. Use the prime product as the key to store the word in a hashmap.
Caveat: prime product might result in integer overflow
Key Mathematical property: Product of two prime numbers is unique
Time: O(NM), Space: O(N)
'''
from collections import defaultdict

def make_array_of_character_counts(w):
    d = [0]*26 # Space O(1)
    for c in w: # O(M),  M = len of characters in word w
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
    for w in W: # O(N) = no. of words in the list
        key = make_array_of_character_counts(w) # O(M)
        if key:
            counts2words[key].append(w)
    return list(counts2words.values())

def run_group_anagrams():
    W = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "cinema", "dad", "triangle", "add", "silent", "integral", "anemic", "altering", "a", " a"]
    print(f"List of words = {W}")
    print(f"Grouped anagrams: {group_anagrams(W)}")

run_group_anagrams()
