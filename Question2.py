
import math


def floyd_marshall(graph):
    n = len(graph)
    d = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (d[i][k] < math.inf and  d[k][j] < math.inf):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d



nodes = {'u' : 0, 'v' : 1, 'w' : 2, 'x' : 3, 'y' : 4, 'z' : 5}

graph = [[0, 2, 5, 1, math.inf, math.inf], 
[2, 0, 3, 2, math.inf, math.inf], 
[5, 3, 0, 3, 1, 5], 
[5, 3, 3, 0, 1, math.inf], 
[math.inf, math.inf, 1, 0, 1, 1], [math.inf, math.inf, 5, math.inf, 1, 0]]

final  = floyd_marshall(graph)
for i in final:
    print(f"Shortest paths: {i}")

