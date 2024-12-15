def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый дочерний элемент
    right = 2 * i + 2  # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше наибольшего элемента
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        # Рекурсивно применяем heapify к затронутому поддереву
        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)

    # Индексы родительских узлов начинаются с n//2 - 1 до 0
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# Пример использования
if __name__ == "__main__":
    array = [3, 19, 1, 14, 8, 7]
    build_heap(array)
    print("Построенная куча:", array)