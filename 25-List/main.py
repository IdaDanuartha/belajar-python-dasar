## --- LIST ---

# list --> kumpulan data

lists = [1,"Danu",True, 4.56]
print(lists[1])

# cara alternatif membuat list
lists_range = range(0, 10, 2) # range(start, stop, step)
print(lists_range)
data_lists = list(lists_range)
print(data_lists)

# membuat list dengan for loop, list comprehension
lists_with_for = [i**2 for i in range(0,10)]
print(lists_with_for)

# membuat list pake for dan if
lists_with_for_if = [i for i in range(1,10) if i != 5]
print(lists_with_for_if)