import time


def two_sum_using_extra_space(numbers: list, target: int) -> tuple:
    if not numbers:
        raise ValueError("List can't be empty")

    already_traveled: dict = {}
    for num in numbers:
        if target - num in already_traveled:
            return target - num, num
        already_traveled[num] = 1
    return -1


if __name__ == "__main__":
    start_time: float = time.time()
    arr: list = [9, 3, 1, 7, 5, 2, 8, 17, 16, 11, 5]
    print(two_sum_using_extra_space(arr, 10))

    arr: list = [15, 7, 11, 2]
    print(two_sum_using_extra_space(arr, 9))

    print(f"seconds => {time.time() - start_time}")