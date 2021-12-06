intArr = [int(el) for el in input("Array of nums: ").split(" ")]  # 1 -4 -1 -2 7 5 2


def counting_sort(arr):
    k = len(arr)
    offset = min(0, min(arr))
    median = [0 for i in range(offset, max(arr) + 1)]
    sortedArr = [0 for i in range(k)]

    for num in arr:
        median[abs(num - offset)] += 1

    for i in range(1, len(median)):
        median[i] = median[i] + median[i - 1]

    for num in arr:
        sortedArr[median[abs(num - offset)] - 1] = num
        median[abs(num - offset)] -= 1

    return sortedArr


print(counting_sort(intArr))
