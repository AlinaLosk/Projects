# Задание 22.9.1 (HW-03)

array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
array = sorted(array)
print(sorted(array))
element = int(input('Введите одно из введенных чисел в списке: '))
left = int(array[0])
right = int(array[-1])

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:
        return middle  # возвращаем индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

if element < left or element > right:
    print('Числа нет в диапазоне')
else:
    print(binary_search(array, element, 0, len(array) - 1))

print(array)
print('Индекс введенного числа: ', binary_search(array, element, 0, len(array) - 1))
