## raw findings, written in 5min38
def is_anagram(str_1, str_2):
    if len(str_1.strip()) != len(str_2.strip()):
        return False
    
    str_2_reverse = ""
    neg_len = len(str_2) * (-1)

    for i in range(-1, neg_len):
        str_2_reverse += str_2[i]
    
    if str_1 == str_2_reverse:
        return True

    return False


## post changes for testing
word1 = "listen"
word2 = "silent"

print(is_anagram(word1, word2))

# result = False
# but misunderstood problem
word3 = "salut"
word4 = "tulas"

print(is_anagram(word3, word4))

# result = still false lmao


## some debugging
def is_anagram_test(str_1, str_2):
    if len(str_1.strip()) != len(str_2.strip()):
        return False
    
    str_2_reverse = ""
    neg_len = (len(str_2) + 1) * (-1)

    for i in range(-1, neg_len, -1):
        str_2_reverse += str_2[i]
    
    if str_1 == str_2_reverse:
        return True

    return False

print(is_anagram_test(word3, word4))

# result = True


## solution from the platform
def is_anagram_2(str1, str2):
    # Clean and sort both strings
    s1 = sorted(str1.lower().replace(" ", ""))
    s2 = sorted(str2.lower().replace(" ", ""))
    
    # If the sorted lists are identical, they are anagrams
    return s1 == s2