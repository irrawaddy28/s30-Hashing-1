'''
Word pattern

Given a pattern and a string str, find if str follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1: Input: pattern = "abba", str = "dog cat cat dog" Output: true

Example 2: Input: pattern = "abba", str = "dog cat cat fish" Output: false

Example 3: Input: pattern = "aaaa", str = "dog cat cat dog" Output: false

Example 4: Input: pattern = "abba", str = "dog dog dog dog" Output: false Notes: You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

Assume there are N characters in the pattern and M words in the string.

Solution:
1. Brute Force: This is similar to the isomorphic strings problem. At each index i, note the character c = pattern[i] and word w = str[i]. Now, check if this (character, word) = (c,w) pair has already been encountered at a previous index j. We can do this by traversing to the left (j = i-1, i-2, ..., 0) and checking:
    if pattern[j] == c:
        yes: if str[j] == word.
             yes: proceed to the next character i++
        no:  return False (not a bijection map)
    Since for each i, 0<=i<=N-1, we traverse j=0,..,i-1, the time complexity is O(N^2).
Time: O(N^2), Space: O(1)

2. Hashing: We use two hashmaps, one each for c2w  (char2word) and w2c (word2char). For c2w, the keys are the characters in pattern and the corresponding values are words in str. For w2c, the keys are the words in str and the corresponding values are chars in pattern. Why can't we use only one hashmap instead of two? Ans: To establish bijection.
Eg. pattern = abbc, str = "dog cat cat dog", then c2w = {a:dog,b:cat,c:dog} (assume only one hash map). Thus, we can convert pattern->str. But for a bijection map, we should be able to convert pattern->str and str->pattern as well. For each word in str, we read the value in c2w and output the corresponding key.  Thus, for the value 'dog', we have two keys
a and c (c2w[a] = dog, c2w[c] = dog). We are unable to choose which key to select because of the many-to-one mapping. Hence, the mapping is not a bijection.
Time: O(N), Space: O(26 + M) = O(M)

(Note: Space is not O(N + M) because the size of the hash map is restricted to the no. of lowercase letters in pattern which is not dependent on the length of the pattern)
'''
from collections import defaultdict

def generate_next_word(sent):
    '''
    generator to generate the next word from a sentence
    '''
    def whitespace(w): # word/char is a whitespace?
        return w.isspace()

    K = len(sent)
    i = 0
    word =""
    while i < K:
        if not whitespace(sent[i]):
            word += sent[i]
        else:
            if word:
                yield word
            word =""
        i += 1
    # last word is not empty and not whiteshapce
    if word and not whitespace(word):
        yield word
    else:
        yield None

def word_pattern(pattern, strings):
    c2w = defaultdict(str) # character to word map
    w2c = defaultdict(str) # word to character map
    get_word = generate_next_word(strings)
    for tgt_char in pattern: # O(N)
        tgt_word = next(get_word)

        w = c2w[tgt_char] # Time: O(1), Space: O(26) = O(1)
        if not w: # w is an empty string
            c2w[tgt_char] = tgt_word
        else:
            if w != tgt_word:
                return False

        c = w2c[tgt_word] # Time: O(1), Space: O(M)
        if not c: # c is an empty string
            w2c[tgt_word] = tgt_char
        else:
            if c != tgt_char:
                return False
    return True

def run_word_pattern():
    pattern = "abba" # one-to-one map (bijection map)
    str = "dog cat cat dog"
    is_bijection = word_pattern(pattern, str)
    print(f"pattern = {pattern}, str = {str}, bijection = {is_bijection}")

    pattern = "abba" # one-to-many map (1 char -> 2 words)
    str = "dog cat cat fish"
    is_bijection = word_pattern(pattern, str)
    print(f"pattern = {pattern}, str = {str}, bijection = {is_bijection}")

    pattern = "abbc" # many-to-one map (2 chars -> 1 word)
    str = "dog cat cat dog"
    is_bijection = word_pattern(pattern, str)
    print(f"pattern = {pattern}, str = {str}, bijection = {is_bijection}")

    pattern = "aaaa" # one-to-one map (bijection map)
    str = "dog cat cat dog"
    is_bijection = word_pattern(pattern, str)
    print(f"pattern = {pattern}, str = {str}, bijection = {is_bijection}")

    pattern = "abba" # many-to-one map (2 chars -> 1 word)
    str = "dog dog dog dog"
    is_bijection = word_pattern(pattern, str)
    print(f"pattern = {pattern}, str = {str}, bijection = {is_bijection}")

run_word_pattern()