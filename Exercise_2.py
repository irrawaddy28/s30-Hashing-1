'''
Isomorphic strings

Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1: Input: s = "egg", t = "add" Output: true

Example 2: Input: s = "foo", t = "bar" Output: false

Example 3: Input: s = "paper", t = "title" Output: true Note: You may assume both s and t have the same length.

Assume there are N characters in s and t

Solution:
    1. Brute Force: At each index i, note the character c1 = s[i] and character c2 = t[i]. Now, check if this (c1,c2) pair has already been encountered at a previous index j. We can do this by traversing to the left (j = i-1, i-2, ..., 0) and checking:
    if s[j] == c1:
        yes: if t[j] == c2.
             yes: proceed to the next character in s (i++)
        no:  return False (not isomorphic)
    Since for each i, 0<=i<=N-1, we traverse j=0,..,i-1, the time complexity is O(N^2).
    Time: O(N^2), Space: O(1)

    2. Hashing:
    We use two hashmaps, one each for s and t. For hash_s, the keys are the characters in s and the corresponding values are chars in t. For hash_t, the keys are the characters in t and the corresponding values are chars in s. Why can't we use only one hashmap instead of two? Ans: To establish bijection.
    Eg. s = eggd, t = adda, then hash_s = {s:a,g:d,d:a} (assume only one hash map). Thus, given s, we can generate d. But if the s,t pair has to be isomorphic, we should be able to produce s from t. For each char in t, we read the value in hash_s and output the corresponding key.  Thus, for the value a, we have two keys
    s and d (hash_s[s] = a, hash_s[d] = a). We are unable to choose which key to select because of the many-to-one mapping. Hence, the mapping is not a bijection and consequently the strings are not isomorphic.
    Time: O(N), Space: O(26) = O(1)

    (Note: Space is not O(N) because the size of the hash map is restricted to the no. of lowercase letters in the string which is not dependent on the length of the string)
'''
def isomorphic(s1, s2):
    N = len(s1)
    assert N == len(s2), "both strings are not of the same length"
    h_s1, h_s2 = {}, {}
    for a,b in zip(s1,s2):
        if a not in h_s1:
            h_s1[a] = b
        else:
            c = h_s1[a]
            if c != b:
                return False

        if b not in h_s2:
            h_s2[b] = a
        else:
            c = h_s2[b]
            if c != a:
                return False
    return True


def run_isomorphic():
    s1, s2 = "egg", "add"
    print(f"{s1} and {s2} are isomorphic? {isomorphic(s1,s2)}")

    s1, s2 = "eggd", "adda"
    print(f"{s1} and {s2} are isomorphic? {isomorphic(s1,s2)}")

    s1, s2 = "foo", "bar"
    print(f"{s1} and {s2} are isomorphic? {isomorphic(s1,s2)}")

    s1, s2 = "paper", "title"
    print(f"{s1} and {s2} are isomorphic? {isomorphic(s1,s2)}")

run_isomorphic()