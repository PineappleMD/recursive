def find_largest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_largest(lst[1:]))
      
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
largest_item = find_largest(my_list)
print(largest_item)
