# Create two graphs G2 = (V2,E2) and G1 = (V1,E1)
V1 = [ "a", "b", "c", "d", "e", "f" ]
E1 = [ {"a", "b"}, {"a", "c"}, {"a", "f"}, {"b", "c"}, {"b", "d"}, {"b", "f"}, {"c", "d"}, {"d", "e"}, {"d",
"f"}, {"e", "f"} ]
V2 = ["g", "h", "k", "m", "n", "p"]
E2 = [ {"g", "h"}, {"g", "m"}, {"g", "p"}, {"h", "k"}, {"h", "m"}, {"h", "p"}, {"k", "p"}, {"k", "m"}, {"m",
"n"}, {"n", "p"} ]

# Create the graphs
G1 = (V1, E1)
G2 = (V2, E2)

# Exercise 1
# Create a function which checks if two graphs might be isomorphic
# It should check:
# 1. They have the same number of vertices
# 2. They have the same number of edges
# 3. They have the same degree sequences
def getNumberOfVertices(graph):
    return len(graph[0])

def getNumberOfEdges(graph):
    return len(graph[1])

def getDegree(V, E):
    counts = {v: 0 for v in V}
    for v in V:
        for e in E:
            if v in e:
                counts[v] += 1
    return counts

def getDegreeSequence(D):
    return sorted(D.values(), reverse=True)

def areGraphsIsomorphic(G1, G2):
    dtmp1 = getDegree(G1[0], G1[1])
    dtmp2 = getDegree(G2[0], G2[1])
    
    if getNumberOfVertices(G1) != getNumberOfVertices(G2):
        return False
    
    if getNumberOfEdges(G1) != getNumberOfEdges(G2):
        return False
    
    if getDegreeSequence(dtmp1) != getDegreeSequence(dtmp2):
        return False
    
    return True

# Test cases
print("Are G1 and G2 isomorphic?", areGraphsIsomorphic(G1, G2))

# Exercise 2
# Create a function which returns a dictionary of the of adjacent vertices.
def getAdjacentVertices(V, E):
    # Initialize an empty dictionary for adjacent vertices
    adj_dict = {v: set() for v in V}
    
    # Loop through each edge and add the adjacent vertices
    for edge in E:
        v1, v2 = list(edge)
        adj_dict[v1].add(v2)
        adj_dict[v2].add(v1)
    
    return adj_dict

# Test cases
print(getAdjacentVertices(V1, E1))

# Exercise 3
# Create a function which returns a dictionary of the degrees of adjacent vertices. (Use the answer from question 2)
def getDegreeOfAdjacentVertices(V, E):
    r_dict = {v: [] for v in V}
    adj_dict = getAdjacentVertices(V, E)
    degree_dict = getDegree(V, E)
    
    # For each vertex and its adjacency set
    for vertex, adj_vertices in adj_dict.items():
        # Get degrees of adjacent vertices
        degrees = [degree_dict[adj_v] for adj_v in adj_vertices]
        # Sort in descending order
        degrees.sort(reverse=True)
        r_dict[vertex] = degrees
    
    return r_dict

# Test the function
print("\nDegrees of adjacent vertices for G1:")
print(getDegreeOfAdjacentVertices(V1, E1))

# Exercise 4
# Create another function which converts from the dictionary, to an ordered list of lists of
# the values (not the keys).
def convertDictToList(D):
    tmp = [v for v in D.values()]
    return sorted(tmp)

print("\nConverted dictionary to list:")
print(convertDictToList(getDegreeOfAdjacentVertices(V1, E1)))