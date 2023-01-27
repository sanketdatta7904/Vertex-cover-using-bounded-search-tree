import sys
from helper import generateEdges, genSubsets, verifyVertexCover

def vertexCoverBrute(graph, res):
    vertices = list(dict(graph).keys())
    k = len(vertices)
    # generate all edges present in graph
    edges = generateEdges(graph)
    for i in range(1, k):
        # generate all subset of size i from set vertices
        subsets_ = genSubsets(vertices, i)
        for s in subsets_:
            # check if subset s is a cover for graph
            if verifyVertexCover(s, edges) == True:
                # since subsets are generated in  increasing size, the first
                # subset that is cover can be returned as the minimal one
                res.append(s)
                return res
    # no cover was found so return set of all edges as minimal cover
    # res.append(vertices)