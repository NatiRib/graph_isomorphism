'''
caso de teste


1 2 3 4 5
1 2 1 3 2 5 2 1 3 1 3 4 4 3 4 5 5 4 5 1
6 7 8 9 10
6 7 6 8 7 10 7 6 8 6 8 9 9 8 9 10 10 9 10 6
'''


import networkx as nx
import matplotlib.pyplot as plt


#functions
def plot_graphs(node_of_graph, graph):
    colors = []
    sizes = []
    labels = {}
    for i in range(0, len(node_of_graph)):
        colors.append('r')
        sizes.append(300)
        labels.update({i + node_of_graph[0]: str(i + node_of_graph[0])})

    nx.draw_networkx(graph, pos=nx.spring_layout(graph), arrows=False, with_labels=True, node_color=colors,
                     labels=labels, node_size=sizes)


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


###graph 1
G1 = nx.Graph()
nodes1 = [int(x) for x in input().split()]
G1.add_nodes_from(nodes1)
paths1 = [int(z) for z in input().split()]
G1.add_path(paths1)
A1 = nx.to_numpy_matrix(G1, G1.nodes(), int)

###graph 2
G2 = nx.Graph()
nodes2 = [int(y) for y in input().split()]
G2.add_nodes_from(nodes2)
paths2 = [int(w) for w in input().split()]
G2.add_path(paths2)
A2 = nx.to_numpy_matrix(G2, G2.nodes(), int)


#check isomorphism

print('G1 e G2 sao isomorfos? ' + str(nx.is_isomorphic(G1, G2)))

#print(is_isomorphic1(repr(A11), repr(A22)))


#plot graphs
plot_graphs(nodes1, G1)
plt.figure()
plot_graphs(nodes2, G2)
plt.show()










