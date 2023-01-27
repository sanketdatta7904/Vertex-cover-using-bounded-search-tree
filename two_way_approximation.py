from helper import generateEdges
# vertex_cover_approx
# Generates an approximately optimal vertex cover for a given graph using the APPROX-VERTEX-COVER algorithm
# found in (Cormen - Introduction to algorithms Page page 1025 )


#Change to compare output for min solution
import random
def vertex_cover_approx(graph, size_, res):
    # generate all edges present in graph
    edges = generateEdges(graph)
    s = 0
    
    # res_cover = ['a' for i in range (len(graph.keys()))]
    # iteration_count = len(graph.keys())
    # Added this iteration for better result
    # for i in range (iteration_count):  
    cover_ = []
    random.shuffle(edges)
    for edge in edges:
        if edge[0] not in cover_ and edge[1] not in cover_:
            cover_.append(edge[0])
            cover_.append(edge[1])
            s += 2
        # if(len(cover_)<len(res_cover)):
        #     res_cover = cover_
    size_.append(s)
    return cover_
