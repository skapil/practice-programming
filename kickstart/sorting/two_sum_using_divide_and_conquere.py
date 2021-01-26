import time


def devide_and_conquere_merge(arr: list, target: int, left: int, right: int) -> tuple:
    if left < right:
        mid: int = left + ((right - left) // 2)
        devide_and_conquere_merge(arr, target, left, mid)
        devide_and_conquere_merge(arr, target, mid + 1, right)
        pair: list = merge_and_find_target(arr, target, left, mid, right)
        if sum(pair) == target:
            return pair


def merge_and_find_target(
    arr: list, target: int, left: int, mid: int, right: int
) -> list:
    index, left_index, right_index = 0, left, mid + 1
    aux: list = [0] * (right - left + 1)

    while left_index <= mid and right_index <= right:
        sum_values: int = arr[left_index] + arr[right_index]
        print(f"Values =>  {arr[left_index]}::{arr[right_index]}")
        if sum_values == target:
            print(f"Sum Values =>  {arr[left_index]}::{arr[right_index]}")
            return [arr[left_index], arr[right_index]]

        if arr[left_index] < arr[right_index]:
            aux[index] = arr[left_index]
            left_index += 1
        else:
            arr[index] = arr[right_index]
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

    for temp_index in range(left, right):
        arr[temp_index] = aux[temp_index - left]

    return arr


if __name__ == "__main__":
    start_time: float = time.time()
    arr: list = [9, 3, 1, 7, 5, 2, 8, 17, 16, 11, 5]
    print(devide_and_conquere_merge(arr, 10, 0, len(arr) - 1))
    arr: list = [15, 7, 11, 2]
    print(devide_and_conquere_merge(arr, 9, 0, len(arr) - 1))
    print(f"seconds => {time.time() - start_time}")
