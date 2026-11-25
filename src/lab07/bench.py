"""Замеры timeit и таблица результатов. Запуск: py -m src.lab07.bench."""

import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

OUT_CSV = "data/lab07/bench.csv"
SEED = 42
SORT_SIZES = (1_000, 10_000, 100_000)
QUADRATIC_LIMIT = 10_000
SEARCH_SIZE = 100_000
QUERIES = 10_000
TWO_SUM_SIZES = (1_000, 10_000)
SKIPPED = "skipped"


def make_numbers(n: int) -> list[int]:
    """Создать случайные данные до начала замера."""
    return [random.randint(-1_000_000, 1_000_000) for _ in range(n)]


def measure(fn, number: int = 1) -> float:
    """Среднее время одного вызова в секундах."""
    return timeit.timeit(fn, number=number) / number


def bench_sorts() -> list[tuple]:
    """Сравнить три сортировки и sorted на одинаковых данных."""
    rows = []
    for n in SORT_SIZES:
        data = make_numbers(n)
        rows.append(("sort", n, "sorted", f"{measure(lambda: sorted(data), 100):.6f}"))
        for fn in (bubble_sort, selection_sort, insertion_sort):
            name = fn.__name__.replace("_sort", "")
            if n > QUADRATIC_LIMIT:
                rows.append(("sort", n, name, SKIPPED))
                continue
            rows.append(("sort", n, name, f"{measure(lambda: fn(data)):.6f}"))
    return rows


def bench_search() -> list[tuple]:
    """Измерить пакет запросов и отдельно подготовку бинарного поиска."""
    data = make_numbers(SEARCH_SIZE)
    queries = [random.choice(data) for _ in range(QUERIES)]
    rows = [("search", SEARCH_SIZE, "linear",
             f"{measure(lambda: [linear_search(data, x) for x in queries]):.6f}")]
    rows.append(("search", SEARCH_SIZE, "sort_before_binary",
                 f"{measure(lambda: sorted(data), 10):.6f}"))
    ordered = sorted(data)
    rows.append(("search", SEARCH_SIZE, "binary",
                 f"{measure(lambda: [binary_search(ordered, x) for x in queries]):.6f}"))
    return rows


def bench_two_sum() -> list[tuple]:
    """Сравнить перебор и словарь; хотя бы одна подходящая пара существует."""
    rows = []
    for n in TWO_SUM_SIZES:
        data = make_numbers(n)
        target = data[-2] + data[-1]
        rows.append(("two_sum", n, "brute",
                     f"{measure(lambda: two_sum_brute(data, target)):.6f}"))
        rows.append(("two_sum", n, "fast",
                     f"{measure(lambda: two_sum_fast(data, target), 100):.6f}"))
    return rows


def print_table(rows: list[tuple]) -> None:
    """Вывести таблицу с выравниванием колонок."""
    print(f"{'task':<8} {'n':>8} {'impl':<20} {'seconds':>10}")
    print("-" * 50)
    last = None
    for task, n, impl, seconds in rows:
        if last is not None and (task, n) != last:
            print()
        print(f"{task:<8} {n:>8} {impl:<20} {seconds:>10}")
        last = (task, n)


def main() -> None:
    random.seed(SEED)
    rows = bench_sorts() + bench_search() + bench_two_sum()
    print_table(rows)
    write_csv(rows, OUT_CSV, header=("task", "n", "impl", "seconds"))
    print(f"Сохранено: {OUT_CSV}")


if __name__ == "__main__":
    main()
