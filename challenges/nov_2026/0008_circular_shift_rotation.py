## raw findings, written in 11min19
def rotate_list(lst, n, direction):
    new_list = []

    if direction == "right":
        for j in lst:
            for i in range(n):
                if lst.find(j) == i:
                    new_list[i] = lst[n - 2]
                else:
                    new_list.append(j)
    else:
        for j in lst:
                for i in range(-n, -1):
                    if lst.find(j) == i:
                        new_list[i] = lst[n + 2]
                    else:
                        new_list.append(j)

    return new_list


## testing
List = [1, 2, 3, 4, 5]
Shift = 2
Direction = 'right'

print(rotate_list(List, Shift, Direction))

# result wrond with this error:
"AttributeError: 'list' object has no attribute 'find'"


## solution from platform
def rotate_list(lst, n, direction='right'):
    if not lst:
        return lst
        
    # Handle shifts larger than the list length
    n = n % len(lst)
    
    if direction == 'right':
        # Take the last n elements and put them at the front
        return lst[-n:] + lst[:-n]
    else:
        # Take the first n elements and put them at the back
        return lst[n:] + lst[:n]