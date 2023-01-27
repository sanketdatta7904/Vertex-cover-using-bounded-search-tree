from brute_force import vertexCoverBrute
from two_way_approximation import vertex_cover_approx
from helper import findHighestDegree, verifyVertexCover
from improved_bst import ibst
from bst import bst
import time
import math

inputfilename = './exercise03/public/vc-exact_001.gr'
graph351 = {'A': ['B'],
            'B': ['C', 'A'],
            'C': ['B', 'D', 'E'],
            'D': ['C', 'E', 'F', 'G'],
            'E': ['C', 'D', 'F'],
            'F': ['D', 'E'],
            'G': ['D']}

graphBipartite = {'A': ['F', 'G'],
                  'B': ['F'],
                  'C': ['H', 'G'],
                  'D': ['H', 'J'],
                  'E': ['I', 'J'],
                  'F': ['A', 'B'],
                  'G': ['A', 'C'],
                  'H': ['C', 'D'],
                  'I': ['E'],
                  'J': ['D', 'E']}

graphConnected = {'A': ['B', 'C', 'D', 'E', 'F', 'G'],
                  'B': ['A', 'C', 'D', 'E', 'F', 'G'],
                  'C': ['A', 'B', 'D', 'E', 'F', 'G'],
                  'D': ['A', 'C', 'B', 'E', 'F', 'G'],
                  'E': ['A', 'C', 'D', 'B', 'F', 'G'],
                  'F': ['A', 'C', 'D', 'E', 'B', 'G'],
                  'G': ['A', 'C', 'D', 'E', 'F', 'B']}


graphBig = {'A': ['B', 'E', 'D'],
            'B': ['A', 'E', 'F', 'C'],
            'C': ['B', 'F'],
            'D': ['A', 'E', 'H', 'G'],
            'G': ['D', 'H', 'K', 'J'],
            'J': ['G', 'K', 'N', 'M'],
            'M': ['J', 'N', 'Q', 'P'],
            'P': ['M', 'Q', 'T', 'S'],
            'F': ['E', 'B', 'C', 'I'],
            'I': ['H', 'E', 'F', 'L'],
            'L': ['K', 'H', 'I', 'O'],
            'O': ['N', 'K', 'L', 'R'],
            'R': ['Q', 'N', 'O', 'U'],
            'E': ['D', 'A', 'B', 'F', 'I', 'H'],
            'H': ['G', 'D', 'E', 'I', 'L', 'K'],
            'K': ['J', 'G', 'H', 'L', 'O', 'N'],
            'N': ['M', 'J', 'K', 'O', 'R', 'Q'],
            'Q': ['P', 'M', 'N', 'R', 'U', 'T'],
            'T': ['S', 'P', 'Q', 'U'],
            'S': ['P', 'T'],
            'U': ['T', 'Q', 'R']}


# print(matrix)
graph1 = {}
edges1 = []
with open(inputfilename, 'r', encoding='utf-8') as f:
    print(f)
    firstline = True
    linecount = 0
    for line in f:
        linecount = linecount+1
        # print(line)
        if(firstline == True):
            v = line.strip().split(" ")[2]
            e = line.strip().split(" ")[3]
            firstline = False
        else:
            src = line.strip().split(" ")[0]
            dst = line.strip().split(" ")[1]
            edges1.append([src, dst])
            if (src in graph1):
                graph1[src].append(dst)
            else:
                graph1[src] = [dst]
            if(dst in graph1):
                graph1[dst].append(src)
            else:
                graph1[dst] = [src]
        if(linecount > 100):
            break

# print(graph)


# vertexCoverBrute(graph351, [])
# print( bst(graph351, [], 3))
# print(bst(graphBig, [], 13))
# print(bst(graph, [], 12))
# print(vertex_cover_approx(graph, [], []))

def testResult():
        n = int(input())
        if(n == 1):
                graph = graph351
        elif(n == 2):
                graph = graphBipartite
        elif(n==3):
                graph = graphConnected
        elif(n==4):
                graph = graphBig
        elif(n==5):
                graph = graph1
                edges = edges1
                
        
        if(n!=5):
                edges=[]
                for v, neighbors in graph.items():
                        for neighbor in neighbors:
                                edges.append([v, neighbor])
        

# Brute Force 
# Please comment for running 5 th option as brute force will take very long time
        cm_time_sta = time.time()
        res = vertexCoverBrute(graph, [])
        cm_time_end = time.time()
        cm_tim = cm_time_end - cm_time_sta
        print("Brute force vertex cover time(sec) = %f" %cm_tim)
        

        print("Result is >>", res)
        print("Now verifying vertex cover")
        ver = verifyVertexCover(res[0], edges)
        print("Vertex cover result is >>", ver)

# Comment till here for running 5th option Uncomment for other options
        if(n!= 5):
                k = len(res[0])
        else:
                k = 12

#2 approx
        cm_time_sta = time.time()
        res = vertex_cover_approx(graph, [], [])
        cm_time_end = time.time()
        cm_tim = cm_time_end - cm_time_sta
        print("Two approximation vertex cover time(sec) = %f" % cm_tim)

        print("Result is >>", res)
        print("Now verifying vertex cover")
        ver = verifyVertexCover(res, edges)
        print("Vertex cover result is >>", ver)

        
        print("parameter passing as k", k)
# Imrpoved bst
        cm_time_sta = time.time()
        res = ibst(graph, [], k)
        cm_time_end = time.time()
        cm_tim = cm_time_end - cm_time_sta

        print("Improved Bounded search tree time(sec) = %f" % cm_tim)

        print("Result is >>", res)
        print("Now verifying vertex cover")
        ver = verifyVertexCover(res[1], edges)
        print("Vertex cover result is >>", ver)

# Classic bst
        cm_time_sta = time.time()
        res = bst(graph, [], k)
        cm_time_end = time.time()
        cm_tim = cm_time_end - cm_time_sta

        print("classic Bounded search tree time(sec) = %f" % cm_tim)

        print("Result is >>", res)
        print("Now verifying vertex cover")
        ver = verifyVertexCover(res[1], edges)
        print("Vertex cover result is >>", ver)



testResult()
