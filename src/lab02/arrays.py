def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Возвращает кортеж (минимум, максимум) списка чисел.
    Встроенные min() и max() не используются.

    Исключения:
        TypeError  - nums не является списком;
        ValueError - список пуст.
    """
    if type(nums) != list:
        raise TypeError("nums должен быть списком")
    if len(nums) == 0:
        raise ValueError("список пуст")

    minx = nums[0]
    maxx = nums[0]
    for x in nums:
        minx = (x if minx > x else minx)
        maxx = (x if maxx < x else maxx)
    return minx, maxx


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный по возрастанию список уникальных значений.
    Дубли убираются через set, сортировка выбором (sorted() и sort() не используются).
    Для пустого списка возвращает [].
    """
    new_list = list(set(nums))
    n = len(new_list)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if new_list[j] < new_list[min_idx]:
                min_idx = j

        temp = new_list[i]
        new_list[i] = new_list[min_idx]
        new_list[min_idx] = temp

    return new_list

def flatten(mat: list[list | tuple]) -> list:
    """
    «Расплющивает» список списков/кортежей в один список по строкам.

    Исключения:
        TypeError - mat не является списком или одна из его строк
                    не является списком/кортежем.
    """
    if type(mat) != list:
        raise TypeError("mat должен быть списком")

    row = []
    for i in range(len(mat)):
        part = mat[i]
        if type(part) != list and type(part) != tuple:
            raise TypeError("строка не строка строк матрицы")

        for j in range(len(part)):
            row.append(part[j])

    return row

# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))

# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))