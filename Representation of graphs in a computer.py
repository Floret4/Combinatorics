                # Матрица смежности #
def create_adjacency_matrix(num_vertices, edges):
    # Создаем матрицу смежности заполненную нулями
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Заполняем матрицу смежности
    for edge in edges:
        u, v = edge
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1  # Поскольку граф неориентированный

    return adjacency_matrix

# Пример использования
num_vertices = 5  # Количество вершин
edges = [(0, 1), (0, 4), (1, 4), (1, 3), (3, 4)]  # Рёбра графа

adjacency_matrix = create_adjacency_matrix(num_vertices, edges)

# Вывод матрицы смежности
for row in adjacency_matrix:
    print(row)