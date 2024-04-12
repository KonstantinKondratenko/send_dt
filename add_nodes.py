class Node:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position[0]}, {self.position[1]})"

class Graph:
    def __init__(self):
        self.sub_vertices = {}
        self.path = []
        self.node_dict = {}

    def add_sub_vertices(self, v1_name, v2_name, sub_vertices_names):
        v1 = self.node_dict[v1_name]
        v2 = self.node_dict[v2_name]
        sub_vertices = [self.node_dict[sv_name] for sv_name in sub_vertices_names]
        self.sub_vertices[(v1, v2)] = sub_vertices
        self.sub_vertices[(v2, v1)] = sub_vertices[::-1]

    def set_path(self, path_names):
        self.path = [self.node_dict[name] for name in path_names]

    def insert_sub_vertices(self):
        new_path = []
        for i in range(len(self.path) - 1):
            v1 = self.path[i]
            v2 = self.path[i + 1]
            if (v1, v2) in self.sub_vertices:
                new_path.extend([v1] + self.sub_vertices[(v1, v2)])
            else:
                new_path.append(v1)
        new_path.append(self.path[-1])
        return [n.name for n in new_path]

vertex_dict = {
    '1': [0, 0],
    '2': [1, 0],
    '3': [2, 0],
    'V1': [0.5, 0],
    'V2': [1.5, 0],
}
if __name__ == '__main__':
    graph = Graph()

    for name, position in vertex_dict.items():
        node = Node(name, position)
        graph.node_dict[name] = node

    graph.add_sub_vertices('1', '2', ['V1', 'V2'])

    graph.set_path(['1', '2', '3'])

    print("Исходный путь:", graph.path)
    print("Путь с подвершинами:", graph.insert_sub_vertices())
