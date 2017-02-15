'''
Dijkstra's Algorithm on a given graph in the form of dictionary of dictionaries
COMPLETED
'''

def dijkstra(graph, source):
    visited = []
    nodes = {}
    for node in graph.keys(): nodes[node] = float('inf')
    nodes[source] = 0
    newNode = source
    already = {}

    for node in graph.keys():
        nodes = reconstruct(graph, newNode, nodes, visited)
        visited.append(newNode)
        already[newNode] = nodes[newNode]
        nodes[newNode] = float('inf')

        newNode = min(nodes, key=nodes.get)

    return already

def reconstruct(graph, source, nodes, visited):
    newNodes = graph[source]
    for node, distance in newNodes.iteritems():
        if not node in visited and nodes[node] > distance + nodes[source]: 
            nodes[node] = distance + nodes[source]
    return nodes

graph = {'a':{'b':7, 'c':9, 'f':14},
         'b':{'a':7, 'c':10, 'd':15},
         'c':{'a':9, 'b':10, 'd':11, 'f':2},
         'd':{'b':15, 'c':11, 'e':6},
         'e':{'d':6, 'f':9},
         'f':{'a':14, 'c':2, 'e':9}}

print dijkstra(graph, 'a')