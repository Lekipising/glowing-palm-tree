def count_swaps(sorted_list, num_list):
    swaps = 0

    position_map = {}
    for index, num in enumerate(num_list):
        position_map[num] = index

    for index, num in enumerate(num_list):
        if num != sorted_list[index]:
            swaps += 1
            pos = position_map[sorted_list[index]]
            # IMPORTANT: update indices within position_map
            position_map[num_list[index]] = pos
            position_map[num_list[pos]] = index
            # swap values as well
            num_list[index], num_list[pos] = num_list[pos], num_list[index]

    return swaps


def lilysHomework(arr):
    arr_copy = list(arr)

    sorted_list_asc = sorted(arr, reverse=False)
    sorted_list_dsc = sorted(arr_copy, reverse=True)

    swaps_a = count_swaps(sorted_list_asc, arr)
    swaps_d = count_swaps(sorted_list_dsc, arr_copy)

    return min(swaps_a, swaps_d)


# pseduo code:
# 1. Create a copy of the array
# 2. Sort the array in ascending order
# 3. Sort the copy of the array in descending order
# 4. Count the number of swaps needed to sort the array in ascending order
# 5. Count the number of swaps needed to sort the copy of the array in descending order

# overall equation for running time:
# T = O(n log n)


if __name__ == '__main__':
    arr = [7, 15, 12, 3]
    arr2 = [3, 4, 1]
    arr3 = [2, 5, 3, 1, 9, 6, 7, 8, 4, ]

    print(lilysHomework(arr))
    print(lilysHomework(arr2))
    print(lilysHomework(arr3))
