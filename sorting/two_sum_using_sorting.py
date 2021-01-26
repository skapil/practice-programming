import time


def two_sum_using_sorting(numbers: list, target: int) -> tuple:
    if not numbers:
        raise ValueError("List can't be empty")

    numbers: list = sorted(numbers)
    low, high = 0, len(numbers) - 1

    while low < high:
        sum_num: int = numbers[low] + numbers[high]
        if sum_num > target:
            high -= 1
        elif sum_num < target:
            low += 1
        else:
            return numbers[low], numbers[high]
    return -1


if __name__ == "__main__":
    start_time: float = time.time()
    arr: list = [9, 3, 1, 7, 5, 2, 8, 17, 16, 11, 5]
    print(two_sum_using_sorting(arr, 10))

    arr: list = [15, 7, 11, 2]
    print(two_sum_using_sorting(arr, 9))

    print(f"seconds => {time.time() - start_time}")
