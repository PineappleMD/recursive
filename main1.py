def recursive_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + recursive_sum(lst[1:])
      
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_list = recursive_sum(my_list)
print(sum_of_list)
