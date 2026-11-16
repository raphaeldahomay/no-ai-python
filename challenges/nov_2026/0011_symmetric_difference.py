## raw findings, written in 4min57
def find_either_not_both(lst_1, lst_2) -> list:
    set_lst_1 = set(lst_1)
    set_lst_2 = set(lst_2)

    right_numbers = []

    for i in set_lst_1:
        if i not in set_lst_2:
            right_numbers.append(i)

    for i in set_lst_2:
        if i not in set_lst_1:
            right_numbers.append(i)

    return right_numbers


## testing
list1 = [101, 102, 103]
list2 = [103, 104, 105]

print(find_either_not_both(list1, list2))

# result almost right:
[101, 102, 104, 105]


## solution from platform
def get_exclusive_ids(ids1, ids2):
    set1 = set(ids1)
    set2 = set(ids2)
    
    # Symmetric difference
    return set1 ^ set2