from helper import findHighestDegree, cleanVerticeFromGraph, pickArbitraryEdge
import copy


def bst(graph, c, k):
    # Checking highest possible edges in the graph
    highestDegree, vertice = findHighestDegree(graph)
    # print("Highest degree >>>", highestDegree)
    # Checking 
    if (len(c) >= k and  highestDegree>=1):
        # print("Current cover>>", c)
    # if (len(c) >= k and  highestDegree >=1):
        return False, c
    if(len(c) >k):
        return False, c
    if(highestDegree == 0 and len(c) <= k ):
        return True, c
    v, w = pickArbitraryEdge(graph)

    graphv = copy.deepcopy(graph)
    # Cleaning graph with the vertice chosen
    cleanVerticeFromGraph(graphv, [v])
    coveredv = copy.deepcopy(c)
    coveredv.append(v)
    resv, resc1 = bst(graphv, coveredv, k)
    if(resv == True):
        return True, resc1
    graphw = copy.deepcopy(graph)
    cleanVerticeFromGraph(graphw, [w])
    coveredw = copy.deepcopy(c)
    coveredw.append(w)
    resw, resc2 = bst(graphw, coveredw, k)
    if(resw == True):
        return True, resc2
    return False, c


