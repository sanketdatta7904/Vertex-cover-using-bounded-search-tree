from helper import findHighestDegree, cleanVerticeFromGraph
import copy



def ibst(graph, c, k):
    highestDegree, v = findHighestDegree(graph)

    if(len(c) == k and highestDegree >=1):
        return False, c
    if(len(c) >k):
        return False, c
    if(highestDegree<1):
        return True,c

    neighbours = graph[v]
    graphv = copy.deepcopy(graph)
    cleanVerticeFromGraph(graphv, [v])
    coveredv = copy.deepcopy(c)
    coveredv.append(v)
    resv, resc1 = ibst(graphv, coveredv, k)
    if(resv == True):
        return True, resc1
    graphw = copy.deepcopy(graph)

    # Sending neighbor array to clean from the graph
    cleanVerticeFromGraph(graphv, neighbours)
    coveredw = copy.deepcopy(c)
    coveredw.append(v)
    resw, resc2 = ibst(graphw, coveredw, k)
    if(resw == True):
        return True, resc2
    return False, c