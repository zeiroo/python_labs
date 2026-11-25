"""Проверка поиска и сортировок. Запуск: py -m src.lab07.check."""

import random

from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> int:
    """Сравнить сортировку с sorted и вернуть число проверенных случаев."""
    for _ in range(trials):
        nums = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        original = nums.copy()
        result = fn(nums)
        message = f"{fn.__name__}: nums={original}, result={result}"
        assert result == sorted(original), message
        assert nums == original, f"Изменён исходный список: {message}"
        assert isinstance(result, list) and result is not nums, message
    return trials


def check_search(trials: int = 100) -> int:
    """Проверить поиск на случайных списках, краях и коротких списках."""
    checks = 0
    for _ in range(trials):
        nums = [random.randint(-20, 20) for _ in range(random.randint(0, 50))]
        x = random.randint(-20, 20)
        try:
            expected = nums.index(x)
        except ValueError:
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

    for nums, x, expected in (([], 5, -1), ([5], 5, 0), ([5], 7, -1), ([1, 3], 3, 1)):
        got = binary_search(nums, x)
        assert got == expected, f"binary_search: nums={nums}, x={x}, got={got}"
        checks += 1
    return checks


def check_two_sum(trials: int = 100) -> int:
    """Сравнить существование ответа и проверить пары обеих реализаций."""
    for _ in range(trials):
        nums = [random.randint(-30, 30) for _ in range(random.randint(0, 30))]
        target = random.randint(-60, 60)
        slow = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        message = f"nums={nums}, target={target}, brute={slow}, fast={fast}"
        assert (slow is None) == (fast is None), message
        if slow is None:
            continue
        for name, pair in (("two_sum_brute", slow), ("two_sum_fast", fast)):
            assert isinstance(pair, tuple) and len(pair) == 2, f"{name}: {message}"
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
