def linear_search(nums, x) -> int:
    """Вернуть индекс первого вхождения x или -1, если x отсутствует."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums, x) -> int:
    """Вернуть индекс любого вхождения x или -1.

    Список должен быть отсортирован по возрастанию.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] < x:
            lo = mid + 1
        elif sorted_nums[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """Перебором найти индексы i < j с суммой target или вернуть None."""
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """За один проход найти индексы i < j с суммой target или вернуть None."""
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None
