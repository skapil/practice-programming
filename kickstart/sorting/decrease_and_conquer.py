import time


def decrease_and_conquere(arr: list, target: int) -> tuple:
    for slow_index in range(len(arr)):
        for back_index in range(len(arr) - 1, slow_index, -1):
            if arr[back_index] < arr[back_index - 1]:
                arr[back_index], arr[back_index - 1] = (
                    arr[back_index - 1],
                    arr[back_index],
                )
        print(arr)
        for index in range(slow_index + 1, len(arr)):
            if arr[index] + arr[slow_index] == target:
                return arr[index], arr[slow_index]
    return -1


if __name__ == "__main__":
    start_time: float = time.time()
    arr: list = [9, 3, 1, 7, 5, 2, 8, 17, 16, 11, 5]
    print(decrease_and_conquere(arr, 10))
    arr: list = [15, 7, 11, 2]
    print(decrease_and_conquere(arr, 9))
    print(f"seconds => {time.time() - start_time}")
