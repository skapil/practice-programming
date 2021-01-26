def merge_sort(arr: list, left: int, right: int) -> list:
    if left < right:
        mid = left + ((right - left) // 2)
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    return arr


def merge(arr: list, left: int, mid: int, right: int) -> list:
    aux: arr = [0] * (right - left + 1)
    index, left_index, right_index = 0, left, mid + 1

    while left_index <= mid and right_index <= right:
        if arr[left_index] < arr[right_index]:
            aux[index] = arr[left_index]
            left_index += 1
        else:
            aux[index] = arr[right_index]
            right_index += 1
        index += 1

    while left_index <= mid:
        aux[index] = arr[left_index]
        left_index += 1
        index += 1
    while right_index <= right:
        aux[index] = arr[right_index]
        right_index += 1
        index += 1

    for temp_index in range(left, right + 1):
        arr[temp_index] = aux[temp_index - left]


print(merge_sort([9, 8, 4, 2, 5, 1], 0, 5))