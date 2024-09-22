# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Graphs/Graph/simple_graph.py

import networkx as nx

from typing import TypeVar, Generic
from src.Graphs.Nodes.TreeNodes.directed_tree_node import DirectedTreeNode

NodeType = TypeVar('NodeType')


class SimpleGraph(nx.Graph, Generic[NodeType]):

    def __init__(self):
        super(SimpleGraph, self).__init__()
        self.need_to_reset_nodes = False

    def removeNode(self, v_id: int):
        self.remove_node(v_id)
        self.need_to_reset_nodes = True

    def addNode(self, node_id: int, node: NodeType):
        self.add_node(node_id, data=node)
        self.need_to_reset_nodes = True

    def getNode(self, node_id: int) -> NodeType:
        if node_id in self.nodes:
            return self.nodes[node_id]['data']
        else:
            print(f"Missing {node_id}")

    def addEdge(self, u_id: int, v_id: int):
        self.add_edge(u_id, v_id)
        self.need_to_reset_nodes = True

    def __str__(self) -> str:
        text = f"Nodes: {self.nodes}\n"
        text += f"Edges: {self.edges}\n"
        return text

    def resetNodes(self) -> None:
        for v_id in self.nodes:
            v = self.getNode(v_id)
            v.reset_node()
        self.need_to_reset_nodes = False

    def get_open_neighborhood(self, node_id: int):
        return list(self.neighbors(node_id))

    def get_closed_neighborhood(self, node_id):
        neighborhood = self.get_open_neighborhood(node_id).copy()
        neighborhood.append(node_id)
        return neighborhood


def main() -> None:

    # nodeType = BFSLikeNode  # change node accordingly, somehow I created a circular reference?
    nodeType = DirectedTreeNode

    G: SimpleGraph[nodeType] = SimpleGraph[nodeType]()

    for i in range(0, 5):
        node = nodeType(i)
        G.addNode(i, node)

    for i in range(0, 3):
        G.addEdge(i, i + 1)

    G.addEdge(1, 4)
    print(G.nodes)
    print(G.edges)

    print(G)
    print(G.has_edge(1, 0))
    print(G.has_edge(0, 1))

    print("removing vertex 3")
    G.removeNode(3)

    print(G.nodes)
    print(G.edges)

    print(G)
    print(G.has_edge(1, 0))

    print("Adding vertex 3 again")
    node = nodeType(3)
    G.addNode(3, node)
    G.addEdge(3, 2)

    print(G)
    print(nx.is_directed(G))

    print("---" * 22)

    print(G.get_open_neighborhood(3))
    print(G.get_closed_neighborhood(3))


if __name__ == '__main__':
    main()
