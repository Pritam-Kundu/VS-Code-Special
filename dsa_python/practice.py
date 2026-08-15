lst = [10, 20, 30, 40, 50]
item = 35
for i in range(len(lst)):
    if item < lst[i]:
        lst.insert(i, item)
        break
else:
    lst.append(item)
print("Updated List:", lst)