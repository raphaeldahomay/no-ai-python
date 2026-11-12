## raw findings, written in 7min58s
def merge_dict(dict_1, dict_2):
    newly_dict = {}
    for k_1, v_1 in dict_1:
        for k_2, v_2 in dict_2:
            if k_1 == k_2:
                newly_dict[k_1] = v_1 + v_2
            else:
                newly_dict[k_1] = v_1
                newly_dict[k_2] = v_2
    return newly_dict


## post changes for testing
dict_1 = {'a': 10, 'b': 20}
dict_2 = {'b': 5, 'c': 15}

print(merge_dict(dict_1, dict_2))

#raised an error: "not enough values to unpack (expected 2, got 1)"


## solution from platform
def merge_dicts(d1, d2):
    # Start with a copy of d1 to avoid modifying the original
    result = d1.copy()
    
    for key, value in d2.items():
        # .get(key, 0) returns 0 if the key doesn't exist yet
        result[key] = result.get(key, 0) + value
    
    return result