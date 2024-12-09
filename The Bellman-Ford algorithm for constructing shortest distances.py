# Программа на Python для алгоритма единственного источника
# кратчайшего пути Беллмана-Форда.

# Класс для представления графа
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = []     # Список для хранения графа

    # Функция для добавления ребра в граф
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Вспомогательная функция для вывода решения
    def printArr(self, dist):
        print("Вершина Дистанция от источника")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

    # Основная функция, которая находит кратчайшие расстояния от src до
    # всех других вершин, используя алгоритм Беллмана-Форда. Функция
    # также обнаруживает отрицательный вес цикла
    def BellmanFord(self, src):

        # Шаг 1: Инициализация расстояний от src до всех других вершин
        # как БЕСКОНЕЧНОСТЬ
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Шаг 2: Расслабление всех рёбер |V| - 1 раз. Простой кратчайший
        # путь от src до любой другой вершины может иметь не более |V| - 1
        # рёбер
        for i in range(self.V - 1):
            # Обновляем значение dist и индекс родителя смежных вершин
            # выбранной вершины. Рассматриваем только те вершины, которые
            # всё ещё в очереди
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Шаг 3: Проверка на наличие циклов с отрицательным весом. Предыдущий шаг
        # гарантирует кратчайшие расстояния, если граф не содержит
        # отрицательного цикла. Если мы получаем более короткий путь, то это
        # означает наличие цикла.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Граф содержит цикл с отрицательным весом")
                return

        # Вывод всех расстояний
        self.printArr(dist)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Вывод решения
g.BellmanFord(0)