d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined = dict(d1)
for key in d2:
    if key in combined:
        combined[key] = combined[key] + d2[key]
    else:
        combined[key] = d2[key]
print(combined)
print()




d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

freq = {}
for key in d:
    val = d[key]
    if val in freq:
        freq[val] += 1
    else:
        freq[val] = 1
print(freq)
print()




def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
print()




def get_distinct(lst):
    distinct = []
    for item in lst:
        if item not in distinct:
            distinct.append(item)
    return distinct

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(get_distinct(sample_list))
print()


def count_elements(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for key in counts:
        print(key, "=>", counts[key], end=", ")
    print()

sample_list2 = [10, 20, 30, 30, 30, 30, 20, 40]
count_elements(sample_list2)
print()



starts_with = lambda s, sub: s.startswith(sub)

print(starts_with("Hello World", "Hello"))
print(starts_with("Hello World", "World"))
