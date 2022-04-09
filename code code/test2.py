str1 = 'aaaaaabgfdsay'

str2 = []
for i in str1:
    if i not in str2:
        str2.append(i)
count = 0
for i in range(len(str1)):
    if str1[i] not in str1[i+1:]:
        print('yes')
        count = count+1

print(count)
print(str2, len(str2))

print(len(set(str1)))
