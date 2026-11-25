"""Проверки против эталона. Запуск из корня: py -m src.lab07.check."""

import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def sorting_cases(trials: int) -> list[list[int]]:
    """Обязательные крайние случаи и trials случайных списков."""
    cases = [[], [5], [2, 1], [1, 2], [3, 3, 3], [-3, 0, -3, 2]]
    cases += [list(range(10)), list(range(9, -1, -1))]
    for _ in range(trials):
        cases.append([random.randint(-100, 100) for _ in range(random.randint(0, 50))])
    return cases


def check_sorting(fn, trials: int = 100) -> None:
    """Сравнить fn с sorted и проверить новый список и сохранность входа."""
    for nums in sorting_cases(trials):
        original = list(nums)
        result = fn(nums)
        message = f"{fn.__name__}: nums={original}, result={result}"
        assert isinstance(result, list), message
        assert result == sorted(original), message
        assert nums == original, f"Изменён исходный список: {message}"
        assert result is not nums, f"Возвращён исходный объект: {message}"


def search_cases() -> list[tuple[list[int], int]]:
    """Случайный запрос, отсутствующее число и края каждого списка."""
    cases = []
    for nums in sorting_cases(100):
        ordered = sorted(nums)
        queries = [random.randint(-100, 100), -101, 101]
        if ordered:
            queries += [ordered[0], ordered[-1]]
        for x in queries:
            cases.append((nums, x))
    return cases


def check_search() -> None:
    """Линейный поиск — первое вхождение, бинарный — любое вхождение."""
    for nums, x in search_cases():
        original = list(nums)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, f"linear_search: nums={nums}, x={x}, got={got}, expected={expected}"
        assert nums == original, f"linear_search изменил {original}"

        ordered = sorted(nums)
        ordered_copy = list(ordered)
        try:
            expected = ordered.index(x)
        except ValueError:
            expected = -1
        got = binary_search(ordered, x)
        message = f"binary_search: nums={ordered_copy}, x={x}, got={got}"
        if expected == -1:
            assert got == -1, message
        else:
            # list.index возвращает первое вхождение, а binary_search — любое.
            assert isinstance(got, int) and 0 <= got < len(ordered), message
            assert ordered[got] == x, message
        assert ordered == ordered_copy, f"binary_search изменил {ordered_copy}"


def two_sum_cases(trials: int) -> list[tuple[list[int], int]]:
    """Повторы, отсутствие ответа, несколько ответов и случайные данные."""
    cases = [([], 0), ([4], 8), ([4, 4], 8), ([1, 2], 10),
             ([0, 0], 0), ([-3, 1, 2], -1), ([4, 9, 2, 7], 11)]
    for trial in range(trials):
        nums = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        target = random.randint(-200, 200)
        if trial % 2 == 0 and len(nums) >= 2:
            i, j = random.sample(range(len(nums)), 2)
            target = nums[i] + nums[j]
        cases.append((nums, target))
    return cases


def check_two_sum(trials: int = 100) -> None:
    """Проверить существование ответа, границы индексов и сумму обеих версий."""
    for nums, target in two_sum_cases(trials):
        original = list(nums)
        # Независимый эталон: какие пары действительно подходят.
        valid_pairs = {(i, j) for i in range(len(nums))
                       for j in range(i + 1, len(nums))
                       if nums[i] + nums[j] == target}
        results = []
        for fn in (two_sum_brute, two_sum_fast):
            result = fn(nums, target)
            message = f"{fn.__name__}: nums={original}, target={target}, result={result}"
            if not valid_pairs:
                assert result is None, message
            else:
                assert isinstance(result, tuple) and len(result) == 2, message
                i, j = result
                assert isinstance(i, int) and isinstance(j, int), message
                assert 0 <= i < j < len(nums), message
                assert nums[i] + nums[j] == target, message
            assert nums == original, f"Изменён исходный список: {message}"
            results.append(result)
        assert (results[0] is None) == (results[1] is None), (
            f"Разные выводы о существовании пары: nums={nums}, target={target}, results={results}"
        )


def main() -> None:
    total = 0
    # Для всех сортировок одинаковые 100 случайных и 8 крайних примеров.
    for fn in (bubble_sort, insertion_sort, selection_sort):
        random.seed(42)
        count = len(sorting_cases(100))
        random.seed(42)
        check_sorting(fn)
        print(f"{fn.__name__}: OK, {count} случаев")
        total += count

    random.seed(42)
    count = 2 * len(search_cases())
    random.seed(42)
    check_search()
    print(f"Поиск: OK, {count} вызовов двух функций")
    total += count

    random.seed(42)
    count = 2 * len(two_sum_cases(100))
    random.seed(42)
    check_two_sum()
    print(f"Two Sum: OK, {count} вызовов двух функций")
    total += count
    print(f"OK: {total} проверок")
    print("Одна проверка — один вызов алгоритма; assert внутри может быть несколько.")


if __name__ == "__main__":
    main()
