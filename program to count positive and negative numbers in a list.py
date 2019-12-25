list1 = [10,-21,4,-45,66,-93,1]

pos_count, neg_count = 0, 0

for num in list1:
    if num >= 0:
        pos_count += 1

    else:
        neg_count += 1

print("Positive no in the list: ", pos_count)
print("Negative no in the list: ", neg_count)