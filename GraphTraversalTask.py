import networkx as nx
import matplotlib.pyplot as plt

def bfs(n, graph):
    qe = []
    BFS = []
    qe.append(n)
    while qe:
        s = qe.pop(-1)
        BFS.append(s)
        for nbr in graph[s]:
                qe.append(nbr)
    BFS.reverse()
    return BFS

def draw_graph(inc):
    graph = nx.Graph()

    for i in inc:
        if len(inc[i]) != 0:
            for j in inc[i]:
                add_edge(i, j, graph=graph)

    nx.draw(graph, with_labels=True)
    plt.show()

def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)

def gtt():
    inc = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        3: [],
        4: [],
        5: [],
        6: [],
    }
    print ("\nОбход графа по умолчанию")
    print(bfs(0 , inc))
    draw_graph(inc)