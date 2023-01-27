import sys
import random
import copy

def genSubsets(set_, k):
    curr_subset = []
    res = []
    generateSubsets(set_, curr_subset, res, k, 0)
    return res


def generateSubsets(set_, curr_subset, subsets_, k, next_index):
    if len(curr_subset) == int(k):
        subsets_.append(curr_subset)
        return
    if next_index + 1 <= len(set_):
        curr_subset_exclude = curr_subset.copy()
        curr_subset.append(set_[next_index])
        generateSubsets(set_, curr_subset, subsets_, k, next_index+1)
        generateSubsets(set_, curr_subset_exclude, subsets_, k, next_index+1)


# verifies if the cover is indeed a vertex cover
def verifyVertexCover(cover, edges):
    # check if atleast 1 vertice from each edge is appearing in cover

    for edge in edges:
        in_cover = False
        if edge[0] in cover or edge[1] in cover: 
            in_cover = True
        # stop processing as soon as 1 edge not found in cover
        if in_cover == False:
            return False
    # return true if all edges have atleast 1 endpoint in cover
    return True


def generateEdges(graph):
    edges = []
    for node in graph: 
        for neighbour in graph[node]:
            if (node,neighbour) and (neighbour, node) not in edges:
                edges.append((node,neighbour))
    return edges


def countDegrees(edges, vertices):
    degrees = {}
    for v in vertices:
        degrees[v] = 0
    for edge in edges:
        degrees[edge[0]] = degrees[edge[0]] + 1
        degrees[edge[1]] = degrees[edge[1]] + 1
    return degrees

def findHighestDegree(graph):
    if(len(graph.keys()) == 0):
        return 0
    h = 0
    vertice = 'a'
    for v, neighbors in graph.items():
        n_size = len(neighbors)
        if (n_size > h):
            h = n_size
            vertice = v
    return h, vertice


def cleanVerticeFromGraph(graph, vertices):
    # if(len(vertices) == 1):
    #     graph.pop(vertices, 'None')
    #     for v,neighbors in graph.items():
    #         graph[v] = list(filter(lambda x : x != vertices, neighbors))
    #     return graph
    # else:
        for v in vertices:
            graph.pop(v, 'None')
        for v,neighbors in graph.items():
            for i in vertices:
                graph[v] = list(filter(lambda x : x != i, neighbors))
        return graph



# cleanGraph(graph351)
# print(graph351)

def pickArbitraryEdge(graph):
    src = None
    for v,neighbors in graph.items():
        if(len(neighbors)>0):
            src = v
            dst = neighbors[0]
    if(src is None):
        return None, None
    return src, dst

def pickDegree3Vertice(graph):
    pass

# print(pickArbitraryEdge(graph351))