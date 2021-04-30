from types import SimpleNamespace


def longest_common_substring(first_input: str, second_input: str):
    substring = SimpleNamespace(max_len=0, word=[])

    def helper(first_idx: int, second_idx: int, slate: list, cur_len: int):
        if first_idx >= len(first_input) or second_idx >= len(second_input):
            return
        if substring.max_len < cur_len:
            substring.max_len = max(cur_len, substring.max_len)
            substring.word = "".join(slate.copy())

        if first_input[first_idx] == second_input[second_idx]:
            slate.append(first_input[first_idx])
            helper(first_idx + 1, second_idx + 1, slate, cur_len + 1)
            slate.pop()
        helper(first_idx + 1, second_idx, slate, 0)
        helper(first_idx, second_idx + 1, slate, 0)

    helper(0, 0, [], 0)
    print(substring)


def test_longest_common_substring():
    longest_common_substring("abdca", "cbda")
    longest_common_substring("passport", "ppsspt")


if __name__ == "__main__":
    test_longest_common_substring()
