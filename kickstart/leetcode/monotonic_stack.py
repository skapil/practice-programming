from collections import deque


# https://leetcode.com/problems/next-greater-element-i/
def next_greater_element(first: list, second: list):
    result: list = [-1] * len(first)
    stack = deque()
    mapping: dict = {}

    for value in second:
        while stack and value > stack[-1]:
            mapping[stack.pop()] = value
        stack.append(value)

    while stack:
        mapping[stack.pop()] = -1

    for value in first:
        result.append(mapping[value])

    return result


def next_greater_element_same_array(arr: list):
    result: list = [-1] * len(arr)
    stack: Deque = deque()

    for index in range(len(arr)):
        while stack and arr[stack[-1]] < arr[index]:
            result[stack.pop()] = arr[index]
        stack.append(index)
    return result


def next_smaller_element(arr: list):
    result: list = [-1] * len(arr)
    stack: Deque = deque()

    for index, value in reversed(list(enumerate(arr))):
        while stack and arr[stack[-1]] < value:
            result[index] = stack.pop()
        stack.append(index)
    return result


def prev_smaller_element(arr: list):
    result: list = [-1] * len(arr)
    stack: Deque = deque()

    for index, value in reversed(list(enumerate(arr))):
        while stack and arr[stack[-1]] > value:
            result[stack.pop()] = value
        stack.append(index)
    return result


# https://leetcode.com/problems/next-greater-element-ii/
def next_element_in_circular(arr: list):
    len_arr: int = len(arr)
    result: list = [-1] * len(arr)
    stack: Deque = deque()

    for index in range(len(arr) * 2):
        while stack and arr[stack[-1]] < arr[index % len_arr]:
            result[stack.pop()] = arr[index % len_arr]
        stack.append(index % len_arr)

    return result


if __name__ == "__main__":
    first: list = [4, 1, 2]
    second: list = [1, 3, 4, 2]
    print(next_greater_element(first, second))

    arr: list = [2, 1, 2, 4, 3]
    print(next_greater_element_same_array(arr))

    arr: list = [2, 1, 2, 4, 3]
    print(next_smaller_element(arr))

    arr: list = [2, 1, 2, 4, 3]
    print(prev_smaller_element(arr))

    arr: list = [2, 1, 2, 4, 3, 1]
    print(next_element_in_circular(arr))

    arr: list = [1, 2, 1]
    print(next_element_in_circular(arr))