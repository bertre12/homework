"""
Задача 1
Реализовать алгоритм сортировки слиянием.
Примечание: Он заключается в разделении исходного массива на две равные половины, сортировке каждой из
половин и последующем их слиянии в отсортированный массив.
Важно: запрещено использовать стандартные функции сортировки в python.
"""


def merge_two_list(left: int, right: int) -> None:
    """Функция разделения одного массива/списка на 2 равных."""
    joint_len = left + right
    new_list = []
    while 0 != (len(joint_len)):
        new_list.append(joint_len.pop(joint_len.index(min(joint_len))))
    return new_list


def merge_sort(joint_len: int) -> None:
    """Функция сортировки массивов/списков через рекурсию."""
    if len(joint_len) == 1:
        return joint_len
    return merge_two_list(merge_sort(joint_len[0:len(joint_len) // 2]), merge_sort(joint_len[len(joint_len) // 2:]))


# mas = list(map(int, input().split()))
# print(*merge_sort(mas))
"""
Задача 2
Дан упорядоченный по возрастанию массив с числами, требуется сгенерировать все его перестановки.
Перестановка n объектов/элементов — это способ их последовательного расположения с учётом порядка.
Например: abc, bca и cab — это разные перестановки трёх букв.
Решите задачу итерационно и рекурсивно. Опишите, какой подход лучше и почему.
"""


# Перестановка элементов рекурсией.

def perm_recursion(n, k=0):
    # n - массив/список.
    # k - для массива/списка по умолчанию.
    if k == len(n):
        print(n)
    
    for i in range(k, len(n)):
        n[k], n[i] = n[i], n[k]
        perm_recursion(n, k + 1)
        n[k], n[i] = n[i], n[k]


perm_recursion(['a', 'b', 'c'])


# Перестановка элементов итеративно.

def perm_iterative(n):
    # n - массив/список.
    if not n:
        return []
    partial = []
    partial.append(n[0])
    
    for i in range(1, len(n)):
        for j in reversed(range(len(partial))):
            curr = partial.pop(j)
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + n[i] + curr[k:])
    
    print(partial)


perm_iterative(['a', 'b', 'c'])

"""Для меня перестановка рекурсивно оказалась более понятна для понимания и восприятия. При тесте на скорость
выполнения алгоритмов при большом количестве элементов (n=10) итеративный метод показал скорость выполнения 562 секунды,
а рекурсивный - 130 секунд. Но при малом количестве элементов (n < 10), итеративный метод показывает малую скорость
выполнения."""
