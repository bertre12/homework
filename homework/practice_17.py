"""Задание
1. Найти все простые циклы в графе.
2. Проверить, является ли дерево симметричным.
3. Определить, является ли граф деревом.
4. Найти диаметр дерева.
5.* Написать свой класс для работы с графом.
"""

"""2"""


# Создаём класс TreeNode с ключевыми аргументами.
class TreeNode:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


# Создаём функцию symmetric и проверяем симметричность/зеркальность в ветках.
def symmetric(root):
    def check(left, right):
        if not left and not right:
            return True
        if left and right:
            return left.value == right.value and check(left.left, right.right) and check(left.right, right.left)
        return False
    
    if not root:
        return True
    
    return check(root.left, root.right)


# Создание объекта и значений для проверки.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(symmetric(root))

"""5"""


# Создание класса граф.
class Graph:
    def __init__(self) -> None:
        # Создание пустого словаря для добавления вершин и рёбер.
        self.graph: dict = {}
    
    def add_vertex(self, vertex) -> None:
        """Добавление узлов графа."""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2) -> None:
        """Добавление рёбер графа."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def get_neighbors(self, vertex) -> None:
        """Определение соседства узла графа."""
        if vertex in self.graph:
            return self.graph[vertex]
        return []
    
    def get_vertices(self):
        """Список всех узлов графа."""
        return list(self.graph.keys())


# Создание объекта и значений для проверки.
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')

print(graph.get_neighbors('A'))
print(graph.get_vertices())
