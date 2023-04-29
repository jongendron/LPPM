# Successive pairs of values are compared and swapped if not in order

def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)  # function calls take longer than getting value of variable
    comparison_count = 0

    for i in range(n - 1):
        swapped = False
        # for j in range(n - 1):  # fixed # iterations and causes redundant comps
        for j in range(n - 1 - i):  # variable # iterations to limit redundancies (True Bubble sort) 
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # swap 2 values
                swapped = True

        print(f"End of pass {i}. `data` is now {data}")
        if not swapped:
            # The last pass resulted in no swaps.
            # The data is now sorted and we can break loop.
            break
    print(f"comparison_count is {comparison_count}")


# numbers = [3, 2, 4, 1, 5, 7, 6]  # random
# numbers = list(range(1,5))[::-1]  # worst case
# numbers = [1, 2, 3, 4, 6, 5, 7]  # mostly pre-sorted
# numbers = [2, 1, 3, 4, 5, 6, 7]  # mostly pre-sorted
# numbers = list(range(1,8))  # best case (presorted; n)
numbers = list(range(7,0,-1))  # worst case (n^2)
print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")

# for x in range(2,11):
#     numbers = list(range(x,0, -1)) # worst case
#     # print(f"Sorting {numbers}")
#     print(f"{x}: ", end='\t')
#     bubble_sort(numbers)

# Testing value swap
# x = 1
# y = 2
# print(x, y)
# x, y = y, x
# print(x,y)
