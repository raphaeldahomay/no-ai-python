## raw findings, build in 1min36
def flatten_list(nested_list: list) -> list:
    flat_list = []
    for i in nested_list:
        for j in i:
            flat_list.append(j)
    return flat_list


## testing
nested = [1, [2, 3], [4, [5, 6]], 7]

# result: 'int' object is not iterable


## updating my raw function
# was helped by ai
def flatten_list_modified(nested_list: list) -> list:
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list_modified(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list_modified(nested))


## solution from the platform
def flatten(lst):
    flat_list = []
    
    for item in lst:
        if isinstance(item, list):
            # Recursion: if it's a list, flatten it and extend our results
            flat_list.extend(flatten(item))
        else:
            # Base case: it's a single value, just add it
            flat_list.append(item)
            
    return flat_list