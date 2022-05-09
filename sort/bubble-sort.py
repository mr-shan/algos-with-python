def bubble_sort(numbers_list):
    """
    Sorts the existing list using bubble sort.
    """
    execution = 0
    comparison = 0
    list_length = len(numbers_list)
    
    for i in range(0, list_length - 1):
        swapped = False
        for j in range(0, list_length - 1 - i):     #optimization 1
            execution += 1
            if numbers_list[j] > numbers_list[j + 1]:
                comparison += 1
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                swapped = True
        print()
        if not swapped:     #optimization 2
            break
                
    print("No. of comparisons: {}\nNo. of swapping: {}".format(execution, comparison))
                
# random list
# nums = [6, 2, 5, 1, 3, 7, 9, 4]

# almost sorted list
nums = [1, 2, 3, 4, 6, 5, 7]

bubble_sort(nums)
print(nums)
