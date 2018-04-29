import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

G1 = nx.Graph()
G2 = nx.Graph()

nodes1 = [int(x) for x in input().split()]
#print(nodes1)
G1.add_nodes_from(nodes1)
#print(G1.nodes())

nodes2 = [int(y) for y in input().split()]
#print(nodes2)
G2.add_nodes_from(nodes2)
#print(G2.nodes())


paths1 = [int(z) for z in input().split()]
G1.add_path(paths1)
A1 = nx.adjacency_matrix(G1)

print(repr(A1))

paths2 = [int(w) for w in input().split()]
G2.add_path(paths2)
A2 = nx.adjacency_matrix(G2)
print(A2.todense())

'''
colors = []
sizes = []
labels = {}
for i in range(0, len(nodes1)):
    colors.append('r')
    sizes.append(300)
    labels.update({i+1: str(i+1)})
'''


#nx.draw_networkx(G1, pos=nx.spring_layout(G1), arrows=False, with_labels=True, node_color=colors, labels=labels,
#                 node_size=sizes)
#plt.show()


def check_bij(g1, g2, v):
    for i in range(len(v)):
        for j in range(len(v)):
            if g1[i][j] != g2[v[i]][v[j]]:
                return False
    return True


def is_isomorphic1(g1, g2, v=[]):
    if not check_bij(g1, g2, v):
        return
    if len(v) == 5:
        return True
    for i in range(5):
        if i in v:
            continue
        if is_isomorphic1(g1, g2, v + [i]):
            return True
    return False


#print(is_isomorphic1(A1, A2))







