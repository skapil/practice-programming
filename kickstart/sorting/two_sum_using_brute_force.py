def brute_force(arr: list, target: int) -> tuple:
    for slow_index in range(len(arr)):
        for fast_index in range(slow_index + 1, len(arr)):
            if arr[slow_index] + arr[fast_index] == target:
                return arr[slow_index], arr[fast_index]
    return -1


if __name__ == "__main__":
    start_time: float = time.time()
    arr: list = [9, 3, 1, 7, 5, 2, 8, 17, 16, 11, 5]
    print(brute_force(arr, 10))
    arr: list = [15, 7, 11, 2]
    print(brute_force(arr, 9))
    print(f"seconds => {time.time() - start_time}")