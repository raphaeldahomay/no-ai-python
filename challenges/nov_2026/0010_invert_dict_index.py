## raw findings, written in 5min32
def invert_dict_index(your_dict):
    new_dict = {}

    for key, value in your_dict.items():
        for i in range(len(value)):
            new_dict[value[i]] = key

    return new_dict


## testing
dict_example = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

print(invert_dict_index(dict_example))

# result is right:
{'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}


## solution from platform
def invert_bibliography(data):
    inverted = {}
    for author, books in data.items():
        for book in books:
            inverted[book] = author
    return inverted