## raw findings, built in 11min14s
def map_counter(word: str) -> dict:
    modified_word = word.strip().lower()
    count = 1
    map = {}
    for l in modified_word:
        pos = modified_word.find('l')
        for i in range(len(modified_word)):
            if i == pos:
                pass
            else:
                if modified_word[i] == l:
                    count += 1
        map[l] = count

    return map


## post changes to test
text = "Python Programming"

print(map_counter(text))

# results
{'p': 13, 'y': 4, 't': 5, 'h': 6, 'o': 17, 'n': 29, ' ': 11, 'r': 21, 'g': 31, 'a': 22, 'm': 26, 'i': 27}


## trying to improve from my own logic
# had to use AI as I couldn't find where's my mistakes
# check in the .md file what it was
def new_map_counter(word: str) -> dict:
    modified_word = word.replace(' ', '').lower()
    map = {}
    for l in modified_word:
        count = 1
        pos = modified_word.find(l)
        for i in range(len(modified_word)):
            if i == pos:
                continue
            else:
                if modified_word[i] == l:
                    count += 1
        map[l] = count
    
    return map

print(new_map_counter(text))

# result is now right:
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}


## solution from the platform
from collections import Counter

def get_frequency(input_string):
    # Clean the string: remove spaces and lowercase everything
    clean_text = input_string.lower().replace(" ", "")
    
    # Counter automatically builds the frequency map
    return Counter(clean_text)