L = [1,2,8,5,6,7,8,4,8]

largest = max(L)

count = 0

for i  in L:

    if(i == largest):
        count += 1

print(count)