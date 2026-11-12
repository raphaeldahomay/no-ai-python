## raw findings: find in 1min57s ##
list_example = []

[i.upper() for i in list_example if len(i) >= 4]


## post modification to be testable ##
# result is right
list_example_2 = ["apple", "bat", "cherry", "dog", "elderberry"]

result = [i.upper() for i in list_example_2 if len(i) >= 4]

print(result)


## solution from platform ##
words = ["apple", "bat", "cherry", "dog", "elderberry"]

[w.upper() for w in words if len(w) >= 4]

