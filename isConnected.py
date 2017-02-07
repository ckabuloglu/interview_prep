'''
Cracking the Coding Interview
4.1
Route Between Two Node: Given a graph, find if there's route between two given nodes
'''

def isConnected(graph, n1, n2):
    visitList = list(graph[n1])
    visited = set()
    visited.add(n1)

    while visitList:
        currentNode = visitList.pop(0)
        if currentNode == n2: return True
        visited.add(currentNode)
        for node in graph[currentNode]:
            if node not in visitList and node not in visited: visitList.append(node)
    return False

graph = {1:[2, 3, 4],
         2:[1, 3, 6],
         3:[1, 2, 4, 7],
         4:[1, 3, 5],
         5:[4, 8],
         6:[2, 7],
         7:[3, 6, 8, 9],
         8:[5, 7, 9],
         9:[7, 8],
         10:[11, 12],
         11:[10, 12],
         12:[10,11]}

print isConnected(graph, 9, 12)
