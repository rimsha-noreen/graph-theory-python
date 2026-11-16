vertices = [1,2,3,4]
edges = [(1,2),(1,3),(2,3),(3,4)]
total_degree = 0
for v in vertices:
    degree = 0
    for u,w in edges:
        if (v==u or v==w):
            degree+=1
    print("degree of vertex", v, "=", degree)
    total_degree +=degree
no_of_edges = len(edges)
print("Sum of vertex degrees =", total_degree)
print("Twice the number of edges =", 2 * no_of_edges)
if total_degree == 2 * no_of_edges:
    print("Handshaking Lemma verified!")
else:
    print("The calculated values do not match.")
