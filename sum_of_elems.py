def sum_of_elements(ls, exclude_negative=False):
    if not exclude_negative:
        return sum([int(elem) for elem in ls])
    else:
        return sum([int(elem) for elem in ls if int(elem) > 0])


list1 = list(input("Give numbers separated by spaces: ").split())
exclude = 0 if input("Do you want to exclude negative numbers(yes or no): ") == "yes" else 1
print(sum_of_elements(list1, bool(exclude)))


