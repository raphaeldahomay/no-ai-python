## raw findings, written in 4min37
def remove_duplicates(your_list):
    no_duplicate_list = []
    size = len(your_list)

    for l in your_list:
        count = 0
        for i in range(size):
            if l == your_list[i]:
                count += 1

        if count == 1:
            no_duplicate_list.append(l)

    return no_duplicate_list


## testing
test_list = [1, 2, 2, 3, 1, 4, 2]

print(remove_duplicates(test_list))

# result wrong:
[3, 4]


## debugging
def remove_duplicates_adj(your_list):
    no_duplicate_list = []

    for l in your_list:
        if l not in no_duplicate_list:
            no_duplicate_list.append(l)

    return no_duplicate_list

print(remove_duplicates_adj(test_list))

# result is right:
[1, 2, 3, 4]


## solution from platform
def remove_duplicates_ordered(items):
    seen = set()
    result = []
    
    for x in items:
        if x not in seen:
            result.append(x)
            seen.add(x)
            
    return result