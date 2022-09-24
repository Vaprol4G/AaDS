import networkx as nx
import matplotlib.pyplot as plt
import json


def add_edge(f_item, s_item, d_item, graph=None):
    graph.add_edge(f_item, s_item, weight = d_item)
    graph.add_edge(s_item, f_item, weight = d_item)

def gct():
    print("\nПостроение графа на основе json файлов\n")
    d_raid = {}
    file_in = open("railways.json", "r", encoding="utf-8")
    data = json.load(file_in)
    for node in data["data"]:
        d_raid[node["code"]] = node["name"]

    graph = nx.Graph()

    file_in2 = open("routes.json", "r", encoding="utf-8")
    data2 = json.load(file_in2)
    for node in data2:
        add_edge(d_raid[node["from"]], d_raid[node["to"]], node["duration"], graph=graph)


    nx.draw(graph, with_labels=True)

    plt.show()