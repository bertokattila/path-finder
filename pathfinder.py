import math
import copy


class Vertex:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)


# decides whether given set is empty
def is_empty(set):
    return len(set) == 0


def min_distance_key(set):
    min_val = math.inf
    min_key = -1  # invalid
    for key in set:
        if set[key].distance_from_start <= min_val:
            min_val = set[key].distance_from_start
            min_key = key
    return min_key


# returns the distance between two verticies
def distance(vertex1, vertex2):
    return math.sqrt(
        pow(abs(vertex1.coordinates[0] - vertex2.coordinates[0]), 2)
        + pow(abs(vertex1.coordinates[1] - vertex2.coordinates[1]), 2)
    )


def dijkstra(start, end, verticies):
    graph = copy.copy(verticies)
    for key in graph:
        graph[key].visited = False
        graph[key].distance_from_start = math.inf
    graph[start].distance_from_start = 0

    while not is_empty(graph):
        vertex = graph[min_distance_key(graph)]
        if vertex.id == end:
            return round(vertex.distance_from_start, 2)
        del graph[vertex.id]

        for neighbour in vertex.neighbours:
            alternative_distance = vertex.distance_from_start + distance(
                vertex, neighbour
            )
            if alternative_distance < neighbour.distance_from_start:
                neighbour.distance_from_start = alternative_distance

    return math.inf


# entry point
verticies = dict()
number_of_paths = int(input())
number_of_vertices = int(input())
number_of_edges = int(input())

paths = []
input()  # empty line
# reading the paths
while number_of_paths > 0:
    number_of_paths = number_of_paths - 1
    line = input().split("\t")
    paths.append((int(line[0]), int(line[1])))

input()  # empty line

index = 0
# reading the coordinates
while number_of_vertices > 0:
    line = input().split("\t")
    verticies[index] = Vertex(index, (int(line[0]), int(line[1])))
    number_of_vertices = number_of_vertices - 1
    index = index + 1

input()  # empty line

# reading the edges
while number_of_edges > 0:
    line = input().split("\t")
    verticies[int(line[0])].add_neighbour(verticies[int(line[1])])
    verticies[int(line[1])].add_neighbour(verticies[int(line[0])])
    number_of_edges = number_of_edges - 1

for item in paths:
    print("{:.2f}".format(dijkstra(item[0], item[1], verticies)), end="\t")
print("")
