# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Graphs/Graph/simple_undirected_tree.py

import networkx as nx

from typing import TypeVar, Generic
from src.Graphs.Graph.simple_graph import SimpleGraph
from src.Graphs.Nodes.TreeNodes.simple_undirected_tree_node import SimpleUndirectedTreeNode

NodeType = TypeVar('NodeType')


class SimpleUndirectedTree(SimpleGraph, Generic[NodeType]):

    def __init__(self):
        super(SimpleUndirectedTree, self).__init__()
        self.need_to_reset_nodes = False

    def _set_leaves(self) -> None:
        # Since the tree is undirected, we can just check the degree of the vertex
        for v_id in self.nodes:
            if self.degree[v_id] == 1:
                v = self.getNode(v_id)
                v.is_leaf = True

    def resetNodes(self) -> None:
        for v_id in self.nodes:
            v = self.getNode(v_id)
            v.reset_node()
        self.need_to_reset_nodes = False

    def update_tree(self) -> None:
        if self.need_to_reset_nodes:
            self.resetNodes()
        self._set_leaves()
        self.need_to_reset_nodes = False


def config1() -> None:
    nodeType = SimpleUndirectedTreeNode

    grafo: SimpleUndirectedTree[nodeType] = SimpleUndirectedTree[nodeType]()

    for i in range(0, 5):
        node = nodeType(i)
        grafo.addNode(i, node)

    for i in range(0, 3):
        grafo.addEdge(i, i + 1)

    grafo.addEdge(1, 4)
    print(grafo.nodes)
    print(grafo.edges)

    grafo.update_tree()
    print(grafo)
    print(grafo.has_edge(1, 0))
    print(grafo.has_edge(0, 1))

    print("removing vertex 3")
    grafo.removeNode(3)
    grafo.update_tree()
    print(grafo.nodes)
    print(grafo.edges)

    print(grafo)
    print(grafo.has_edge(1, 0))

    print("Adding vertex 3 again")
    node = nodeType(3)
    grafo.addNode(3, node)
    grafo.addEdge(3, 2)
    grafo.update_tree()
    print(grafo)
    print(nx.is_directed(grafo))

    print("---" * 22)


if __name__ == "__main__":
    config1()
