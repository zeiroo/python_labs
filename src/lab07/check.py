"""Проверка поиска и сортировок. Запуск: py -m src.lab07.check."""

import random

from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> int:
    """Сравнить сортировку с sorted и вернуть число проверенных случаев."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = nums.copy()
        result = fn(nums)
        message = f"{fn.__name__}: nums={original}, result={result}"
        assert result == sorted(original), message
        assert nums == original, f"Изменён исходный список: {message}"
        assert result is not nums, f"Возвращён исходный список: {message}"
    return trials


def check_search(trials: int = 100) -> int:
    """Проверить поиск на случайных списках, краях и коротких списках."""
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-20, 20) for _ in range(n)]
        x = random.randint(-20, 20)
        if x in nums:
            expected = nums.index(x)
        else:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, f"linear_search: nums={nums}, x={x}, got={got}"
        checks += 1

        ordered = sorted(nums)
        got = binary_search(ordered, x)
        message = f"binary_search: nums={ordered}, x={x}, got={got}"
        if expected == -1:
            assert got == -1, message
        else:
            assert 0 <= got < len(ordered) and ordered[got] == x, message
        checks += 1

        if ordered:
            for edge in (ordered[0], ordered[-1]):
                got = binary_search(ordered, edge)
                assert 0 <= got < len(ordered) and ordered[got] == edge, (
                    f"binary_search: nums={ordered}, x={edge}, got={got}"
                )
                checks += 1

    assert binary_search([], 5) == -1, "binary_search: nums=[], x=5"
    assert binary_search([5], 5) == 0, "binary_search: nums=[5], x=5"
    assert binary_search([5], 7) == -1, "binary_search: nums=[5], x=7"
    assert binary_search([1, 3], 3) == 1, "binary_search: nums=[1, 3], x=3"
    return checks + 4


def check_two_sum(trials: int = 100) -> int:
    """Сравнить существование ответа и проверить пары обеих реализаций."""
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-30, 30) for _ in range(n)]
        target = random.randint(-60, 60)
        slow = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        message = f"nums={nums}, target={target}, brute={slow}, fast={fast}"
        if slow is None:
            assert fast is None, message
            continue
        assert fast is not None, message
        for name, pair in (("two_sum_brute", slow), ("two_sum_fast", fast)):
            i, j = pair
            assert 0 <= i < j < len(nums), f"{name}: {message}"
            assert nums[i] + nums[j] == target, f"{name}: {message}"
    return trials


def main() -> None:
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")


if __name__ == "__main__":
    main()
