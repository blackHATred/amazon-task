import random
import time


t1 = time.time_ns()
# начальные данные
n, m = random.randint(1000, 5000), random.randint(1000, 5000)
array = []
for i in range(n):
    array.append([])
    for j in range(m):
        if i == 0:
            array[0].append(random.randint(1, 100))
        elif j == 0:
            array[i].append(array[i-1][0]+random.randint(1, 100))
        else:
            array[i].append(max(array[i-1][j], array[i][j-1])+random.randint(1, 100))
    if i == 0:
        array[0].sort()

k = random.choice((random.choice(random.choice(array)), -1))
# for i in array:
#     print(i)
t2 = time.time_ns()

i_, j_ = 0, m-1

# Оптимальный алгоритм
for s in array:
    low = i_
    high = j_ - 1
    mid = 0
    f = False
    while low <= high:
        mid = (high + low) // 2
        if s[mid] < k:
            low = mid + 1
        elif s[mid] > k:
            j_ = mid - 1
            high = mid - 1
        else:
            print(f'k == {k} находится в строке {s} на позиции {mid}')
            f = True
            break
    if f:
        break
t3 = time.time_ns()


array_ = array.copy()
# Обычный бинарный поиск
for s in array_:
    low = 0
    high = len(s) - 1
    mid = 0
    f = False
    while low <= high:
        mid = (high + low) // 2
        if s[mid] < k:
            low = mid + 1
        elif s[mid] > k:
            high = mid - 1
        else:
            print(f'k == {k} находится в строке {s} на позиции {mid}')
            f = True
            break
    if f:
        break
t4 = time.time_ns()
# Полный перебор
for s in array:
    f = False
    for i in s:
        if i == k:
            print(f'k == {k} находится в строке {s} на позиции {s.index(k)}')
            f = True
            break
    if f:
        break
t5 = time.time_ns()
print(f'Массив размера {n} x {m}\n'
      f'Создание массива заняло {(t2-t1)/pow(10,9)} с\n'
      f'Оптимальный алгоритм занял {(t3-t2)/pow(10,9)} с\n'
      f'Обычный бинарный поиск занял {(t4-t3)/pow(10,9)} с\n'
      f'Полный перебор занял {(t5-t4)/pow(10,9)} с')
