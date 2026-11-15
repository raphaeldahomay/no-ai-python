## raw findings, written in 7min
def merge_dict_value_group(dict_1, dict_2):
    check_value = set()

    for k_1, v_1 in dict_1.items():
        for k_2, v_2 in dict_2.items():
            if k_2 in check_value:
                continue
            else:
                check_value.append(k_2)
                if k_1 == k_2:
                    dict_1[k_1] = list(v_1, v_2)
                else:
                    dict_1[k_2] = v_2

    return dict_1


## testing
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# result is wrong:
"AttributeError: 'set' object has no attribute 'append'"


## updating myself
def merge_dict_value_group_adj(dict_1, dict_2):
    new_dict = dict_1.copy()
    check_value = []

    for k_1, _ in dict_1.items():
        check_value.append(k_1)

    for k_2, v_2 in dict_2.items():
        if k_2 in check_value:
            new_dict[k_2] = [new_dict.get(k_2), v_2]
        else:
            new_dict[k_2] = v_2

    return new_dict

print(merge_dict_value_group_adj(d1, d2))

# result almost right:
{'a': 1, 'b': [2, 3], 'c': 4}


## solution from platform
def merge_and_group(dict1, dict2):
    combined = {}
    # Get all unique keys from both dictionaries
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    for key in all_keys:
        values = []
        if key in dict1:
            values.append(dict1[key])
        if key in dict2:
            values.append(dict2[key])
        combined[key] = values
        
    return combined