"""Честные замеры timeit. Запуск: py -m src.lab07.bench.

Квадратичные сортировки на 100 000 запускаются в отдельном процессе:
через 60 секунд незавершённый расчёт останавливается.
"""

import multiprocessing
import platform
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

OUT_CSV = Path("data/lab07/bench.csv")
SORT_SIZES = (1_000, 10_000, 100_000)
TWO_SUM_SIZES = (1_000, 10_000)
SEARCH_SIZE = 100_000
QUERIES = 10_000
TIME_LIMIT = 60
SEED = 42


def make_numbers(n: int) -> list[int]:
    """Подготовка данных выполняется до запуска секундомера."""
    return [random.randint(-1_000_000, 1_000_000) for _ in range(n)]


def measure(fn, number: int = 1) -> float:
    """Время одного вызова: суммарное время number запусков / number."""
    return timeit.timeit(fn, number=number) / number


def sort_worker(fn, data, connection) -> None:
    """Сообщить о готовности и измерить сортировку без времени старта процесса."""
    try:
        connection.send(("ready", None))
        seconds = measure(lambda: fn(data))
        connection.send(("ok", seconds))
    except Exception as error:
        connection.send(("error", repr(error)))
    finally:
        connection.close()


def measure_limited(fn, data, timeout: int = TIME_LIMIT) -> float | str:
    """Настоящее ограничение времени; остановленный запуск не выдаём за замер."""
    context = multiprocessing.get_context("spawn")
    receiver, sender = context.Pipe(duplex=False)
    process = context.Process(target=sort_worker, args=(fn, data, sender))
    process.start()
    sender.close()
    try:
        status, result = receiver.recv()
        if status != "ready":
            raise RuntimeError(result)
        if not receiver.poll(timeout):
            return f"> {timeout} s"
        status, result = receiver.recv()
        if status != "ok":
            raise RuntimeError(result)
        return result
    finally:
        if process.is_alive():
            process.terminate()
        process.join()
        receiver.close()
        process.close()


def seconds_text(seconds: float | str) -> str:
    return seconds if isinstance(seconds, str) else f"{seconds:.9f}"


def bench_sorts() -> list[tuple]:
    rows = []
    for n in SORT_SIZES:
        data = make_numbers(n)
        rows.append(("sort", n, "sorted", seconds_text(measure(lambda: sorted(data), 20))))
        for fn in (bubble_sort, insertion_sort, selection_sort):
            print(f"Замер {fn.__name__}, n={n}...", flush=True)
            if n == 100_000:
                seconds = measure_limited(fn, data)
            else:
                seconds = measure(lambda: fn(data))
            rows.append(("sort", n, fn.__name__, seconds_text(seconds)))
    return rows


def run_queries(fn, data, queries) -> None:
    """Один вызов этой функции — весь пакет из 10 000 запросов."""
    for x in queries:
        fn(data, x)


def bench_search() -> list[tuple]:
    print("Замер поиска: 10 000 запросов к 100 000 элементам...", flush=True)
    data = make_numbers(SEARCH_SIZE)
    # Чередуем существующие и гарантированно отсутствующие значения.
    queries = [random.choice(data) if i % 2 == 0 else random.randint(1_000_001, 2_000_000)
               for i in range(QUERIES)]
    linear = measure(lambda: run_queries(linear_search, data, queries))
    preparation = measure(lambda: sorted(data), 20)
    ordered = sorted(data)
    binary = measure(lambda: run_queries(binary_search, ordered, queries), 10)
    return [
        ("search", SEARCH_SIZE, "linear_search", seconds_text(linear)),
        ("search", SEARCH_SIZE, "sort_before_binary", seconds_text(preparation)),
        ("search", SEARCH_SIZE, "binary_search", seconds_text(binary)),
    ]


def bench_two_sum() -> list[tuple]:
    rows = []
    for n in TWO_SUM_SIZES:
        print(f"Замер Two Sum, n={n}...", flush=True)
        # Только два отрицательных числа, в конце. Для target=-3
        # существует ровно одна пара: так перебор не завершится случайно рано.
        data = [random.randint(1, 1_000_000) for _ in range(n - 2)] + [-1, -2]
        for fn, number in ((two_sum_brute, 1), (two_sum_fast, 100)):
            seconds = measure(lambda: fn(data, -3), number)
            rows.append(("two_sum", n, fn.__name__, seconds_text(seconds)))
    return rows


def print_table(rows: list[tuple]) -> None:
    print(f"{'task':<10} {'n':>8} {'impl':<20} {'seconds':>14}")
    print("-" * 55)
    for task, n, impl, seconds in rows:
        print(f"{task:<10} {n:>8} {impl:<20} {seconds:>14}")


def main() -> None:
    random.seed(SEED)
    print(f"Python {platform.python_version()}, {platform.system()} {platform.machine()}", flush=True)
    print(f"seed={SEED}; лимит больших сортировок: {TIME_LIMIT} с", flush=True)
    rows = bench_sorts() + bench_search() + bench_two_sum()
    write_csv(rows, OUT_CSV, header=("task", "n", "impl", "seconds"))
    print_table(rows)
    print(f"Сохранено: {OUT_CSV}")
    print("search: время всего пакета из 10 000 запросов; подготовка — одна сортировка.")


if __name__ == "__main__":
    main()
