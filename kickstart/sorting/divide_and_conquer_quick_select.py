import time


def divide_and_conquere_quick_select(
    arr: list, target: int, left: int, right: int
) -> list:
    if left < right:
        result: list = partition(arr, target, left, right)
        if len(result) == 2:
            return result
        divide_and_conquere_quick_select(arr, target, left, result[0] - 1)
        divide_and_conquere_quick_select(arr, target, result[0] + 1, right)


def partition(arr: list, target: int, left: int, right: int) -> list:
    pivot_index: int = random.randint(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    start, pivot = left, arr[left]

    for index in range(start + 1, right):
        if pivot + arr[index] == target:
            return [pivot, arr[index]]
        if arr[index] < pivot:
            start += 1
            arr[start], arr[index] = arr[index], arr[start]

    arr[left], arr[start] = arr[start], arr[left]
    return [start]


if __name__ == "__main__":
    start_time: float = time.time()
    arr: list = [9, 3, 1, 7, 5, 2, 8, 17, 16, 11, 5]
    print(divide_and_conquere_quick_select(arr, 10, 0, len(arr) - 1))
    arr: list = [15, 7, 11, 2]
    print(divide_and_conquere_quick_select(arr, 9, 0, len(arr) - 1))
    print(f"seconds => {time.time() - start_time}")