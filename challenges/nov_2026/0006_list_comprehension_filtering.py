## raw findings, written in 3min18
list_of_string = []

filtered_list = [i for i in list_of_string if len(i) > 5 and i[0].lower() in ('a', 'e', 'i', 'o', 'u')]


##testing
list_of_string = ["apple", "education", "ice", "ocean", "python", "umbrella"]

filtered_list = [i for i in list_of_string if len(i) > 5 and i[0].lower() in ('a', 'e', 'i', 'o', 'u')]

print(filtered_list)

# result is right:
['education', 'umbrella']


## solution from platform
words = ["apple", "education", "ice", "ocean", "python", "umbrella"]

vowel_long = [
    w for w in words 
    if len(w) > 5 and w[0].lower() in 'aeiou'
]