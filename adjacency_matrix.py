import numpy as np
vertices = [1,2,3,4]
edges = [(1,2),(1,3),(2,3),(3,4)]
n=len(vertices)
adjacency = np.zeros((n,n),dtype=int)
print(adjacency)   #just want to see zero matrix
for u,v in edges:
    adjacency[u-1, v-1]=1 #why we subtact 1 bcz python list indexing start from 0 
    adjacency[v-1, u-1]=1
print("Adjacency matrix", adjacency)  # to see an adjacency matrix
degree = np.sum(adjacency, axis=1)  # axis = 1 is used to summ all rows and axis = 0 is used for sum of all columns. As we want the degree of each vertx
print(degree)  # calculate the degree of each vertex. In adjacency matrix each row represent the vertex 
sum_of_all_vertex_degree = np.sum(degree) # sum of all vertex degree bcz we want to see the handshaking lemma
print("sum of all vertex degree", sum_of_all_vertex_degree)
no_of_edges = len(edges)  # no of edges
print("No of edges", no_of_edges)
if sum_of_all_vertex_degree == 2* no_of_edges:  
    print("hand shaking lemma satisfy")
else:
    print("not satisfy")
degree_matrix = np.diag(degree) # for degree matrix
print("Degree matrix", degree_matrix)
graph_laplacian = degree_matrix - adjacency # for laplacian matrix
print("Graph laplacian", graph_laplacian)
sum_of_each_row_of_laplacian = np.sum(graph_laplacian, axis=1)
print("vector sum of each row of laplacian", sum_of_each_row_of_laplacian)
