
s = "hello .py"
words = s.split(" ")
result = ""
for w in words:
    result = result + w[::-1] + " "
result = result.strip()
print(result)



word = "madam"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")



numbers = [12, 45, 2, 89, 34, 7]
max_val = numbers[0]
min_val = numbers[0]
for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n
print(max_val, " Min =", min_val)



values = [10, 20, 30, 40, 50]
target = 30
index = -1
for i in range(len(values)):
    if values[i] == target:
        index = i
        break
print(target, "is", index)




lst = [10, 20, 30, 20, 50]
for i in range(len(lst)):
    if lst[i] == 20:
        lst[i] = 200
print(lst)



lst2 = [10, 20, 30, 20, 50]
new_list = []
for item in lst2:
    if item not in new_list:
        new_list.append(item)
print(new_list)



words_list = ['aca', 'xyz', 'aba', '1221']
count = 0
for w in words_list:
    if len(w) >= 2 and w[0] == w[-1]:
        count = count + 1
print(count)