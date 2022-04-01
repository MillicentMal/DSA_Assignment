
import math

from numpy import short

# TASK A
visited=set() #track and store visited vertices as a set
def dfs(visited, graph, vertex): #function for dfs traversal
    if vertex not in visited: #if  node is not visited mark false, and append visited node
        print(vertex)
        visited.add(vertex)
        for neighbour in graph[vertex]:#recurse dfs
            dfs(visited, graph, neighbour)

print(" ")           

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = {}
        else:
            print("Node already in graph")
    
    def add_neighbour(self, vertex1, vertex2, weight):
        if vertex1 not in self.nodes:
            self.add_node(vertex1)
            self.nodes[vertex2] = weight
        if vertex2 not in self.nodes:
            self.add_node(vertex2)
            self.nodes[vertex2][vertex1] = weight
        self.nodes[vertex1][vertex2] = weight
        self.nodes[vertex2][vertex1] = weight 
    
    def print(self):
        print(self.nodes)
    

# TASK B
    def dijkstra(self, start):
        """
        Able to only iterate from C to its neighbours. 
        Not sure how to change to other nodes
        

        """

        final = {}
        visited = []
        shortest_path = {}
        shortest_path[start] = 0
        for i in self.nodes:
            shortest_path[i] = math.inf
        shortest_path[start] = 0
        for i in range(len(self.nodes)):
        
            for i in self.nodes[start]:
                if i in visited:
                    continue
                if self.nodes[start][i] < shortest_path[i]:
                    shortest_path[i] = self.nodes[start][i]
            
            self.dijkstra(start)
        return shortest_path


    

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")

graph.add_neighbour("A", "B", 13)
graph.add_neighbour("A", "D", 10)
graph.add_neighbour("C", "B", 5)
graph.add_neighbour("D", "B", 17)
graph.add_neighbour("E", "B", 20)
graph.add_neighbour("F", "B", 18)
graph.add_neighbour("C", "E", 22)
graph.add_neighbour("C", "F", 30)

graph.print()
print("Running Dijkstra")
print(graph.dijkstra("C"))
print("Printing the DFS: ")
dfs(visited,graph.nodes,"C") #test using vertex C; print output
