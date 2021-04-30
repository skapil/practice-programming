from types import SimpleNamespace


def is_palindrom(input: str):
    left, right = 0, len(input) - 1
    while left <= right:
        if input[right] != input[left]:
            return False
        right -= 1
        left += 1
    return True


def longest_palindrom_subsequnce(input: str):
    if input is None:
        return None
    if not input or is_palindrom(input):
        return len(input)
    palindrom = SimpleNamespace(word="", max_len=0)

    def helper(idx: int, slate: list, cur_len: int):
        if cur_len > palindrom.max_len and is_palindrom("".join(slate)):
            palindrom.max_len = cur_len
            palindrom.word = "".join(slate)
        if idx >= len(input):
            return

        slate.append(input[idx])
        helper(idx + 1, slate, cur_len + 1)
        slate.pop()
        helper(idx + 1, slate, cur_len)

    helper(0, [], 0)
    print(palindrom)


def longest_palindrom_subsequnce_bu(input: str):
    if input is None:
        return None
    if not input or is_palindrom(input):
        return len(input)
    palindrom = SimpleNamespace(word="", max_len=0)

    def helper(left: int, right: int):
        if left > right:
            return 0
        if left == right:
            return 1

        cur_len: int = 0
        if input[left] == input[right]:
            cur_len = 2 + helper(left + 1, right - 1)
            palindrom.max_len = max(palindrom.max_len, cur_len)
            return cur_len

        first: int = helper(left + 1, right)
        second: int = helper(left, right - 1)
        return max(first, second)

    helper(0, len(input) - 1)
    print(palindrom)


def longest_palindrom_substring(input: str):
    palindrom = SimpleNamespace(max_len=1, word="")

    def helper(left: int, right: int):
        if right > len(input) or left >= len(input) - 1:
            return
        word = input[left : right + 1]
        if len(word) >= palindrom.max_len and is_palindrom(word):
            palindrom.max_len = max(palindrom.max_len, len(word))
            palindrom.word = word

        if right == len(input):
            helper(left + 1, left + 1)
        helper(left, right + 1)

    helper(0, 1)
    print(palindrom)


def longest_palindrom_substring_bu(input: str):
    def helper(left: int, right: int):
        if left > right:
            return 0
        if left == right:
            return 1

        if input[left] == input[right]:
            cur_len = (right - left) - 1
            if cur_len == helper(left + 1, right - 1):
                return cur_len + 2

        left_palindrom: int = helper(left + 1, right)
        right_palindrom: int = helper(left, right - 1)
        return max(left_palindrom, right_palindrom)

    print(helper(0, len(input) - 1))


def test_longest_palindrom_substring():
    longest_palindrom_substring_bu("abdbca")
    longest_palindrom_substring_bu("cddpd")
    longest_palindrom_substring_bu("pqr")


def test_longest_palindrom_subsequnce():
    longest_palindrom_subsequnce_bu("abdbca")
    longest_palindrom_subsequnce_bu("cddpd")
    longest_palindrom_subsequnce_bu("pqr")


if __name__ == "__main__":
    test_longest_palindrom_substring()