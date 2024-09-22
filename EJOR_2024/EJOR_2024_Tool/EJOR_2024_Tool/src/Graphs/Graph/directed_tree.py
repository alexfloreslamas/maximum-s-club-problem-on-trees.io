# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Graphs/Graph/directed_tree.py

import networkx as nx
import src.Utils.utils as utils

from typing import TypeVar
from src.Graphs.Enums.enum_node_type import EnumNodeType
from src.Graphs.Graph.simple_directed_tree import SimpleDirectedTree
from src.Graphs.Nodes.TreeNodes.directed_tree_node import DirectedTreeNode


MyNodeType = TypeVar('MyNodeType')


class DirectedTree(SimpleDirectedTree[MyNodeType]):
    """
    A basic class of a directed tree T = (V_T, E_T), where the root node is the one with no incoming edges.
    I try to follow the next semantics:
        - node_id: int denotes the id of some vertex; usually, I will use it in a method's signature. Nonetheless, I
                    might also use something like v0_id when the context requires it.
        - v_id: int is also an id of some vertex v in V_T. I will use it inside the body of a method.
        - v: object is a vertex with all its attributes and methods.
    """

    def __init__(self):
        super(DirectedTree, self).__init__()

    def update_tree(self) -> None:
        super(DirectedTree, self).update_tree()
        self._compute_h_l_d_ll()

    def _compute_h_l_d_ll(self) -> None:  # See Schäfers algorithm
        for v_id in self.nodes:
            v: DirectedTreeNode = self.getNode(v_id)
            v.reset_h_l_d_ll()

        dfs_dict = nx.shortest_path_length(self, self.root_id)
        the_lowest_leaf_dist = -4
        # Computes for each v in V_T: dist(v, root) and the overall longest distance to root
        for v_id in list(self.nodes):
            v: DirectedTreeNode = self.getNode(v_id)
            v.distance_to_root = dfs_dict[v_id]

            if the_lowest_leaf_dist < v.distance_to_root:
                the_lowest_leaf_dist = v.distance_to_root

        # Finds: v.lowest_leaf in T_v
        # Computes: v.height and v.level, this is according to Schafer's definition

        for v_id in self.postorder:
            v: DirectedTreeNode = self.getNode(v_id)
            if v.is_leaf:
                v.local_lowest_leaf_id = v.node_id
                v.height = 0
                v.level = the_lowest_leaf_dist - v.distance_to_root
            else:
                Cv = self.get_children(v_id)
                local_lowest_leaf_id = -6
                height = -1
                for u_id in Cv:
                    u: DirectedTreeNode = self.getNode(u_id)
                    if u.height + 1 > height:
                        local_lowest_leaf_id = u.local_lowest_leaf_id
                        height = u.height + 1

                v.local_lowest_leaf_id = local_lowest_leaf_id
                v.height = height
                v.level = the_lowest_leaf_dist - v.distance_to_root

    def get_path_towards_root(self, v0_id: int, path_length: int) -> list[int]:
        """
        Computes a list P with the vertices denoting a path towards the root of T. Note that:
            - |P| <= path_length since the path to the root might not be that long
        :param v0_id: initial vertex of the path
        :param path_length: upper bound of the path's length
        :return: P: list[int]
        """
        P = [v0_id]
        path_length -= 1
        while path_length >= 0:
            parent = self.get_parent(v0_id)
            if parent is None:
                break
            else:
                P.append(parent)
                v0_id = parent
                path_length -= 1
        return P


def config1() -> None:
    nodeType = DirectedTreeNode
    enumNodeType = EnumNodeType.DirectedTreeNode

    graph: DirectedTree[nodeType] = DirectedTree[nodeType]()

    kwargs = {"k": 3}
    for i in range(0, 5):
        node = utils.prepare_node(i, enumNodeType, **kwargs)
        graph.addNode(i, node)

    for i in range(0, 3):
        graph.addEdge(i, i + 1)

    graph.addEdge(4, 1)
    print(graph.nodes)
    print(graph.edges)

    graph.set_root(0)
    graph.update_tree()

    v_id = 3
    for i in range(0, 6):
        print(f"Path from {v_id} to {graph.root_id} of length at most {i}: {graph.get_path_towards_root(v_id, i)}")
    graph.removeNode(3)
    print(graph.nodes)
    print(graph.edges)

    print(graph)
    print(graph.has_edge(1, 0))

    node = utils.prepare_node(3, enumNodeType, **kwargs)
    graph.addNode(3, node)
    graph.addEdge(3, 2)
    print("---" * 22)
    for v_id in graph.nodes:
        graph.set_root(v_id)
        graph.update_tree()
        print(f"changing the root to {v_id}")
        print(graph)
        print("\n")


if __name__ == "__main__":
    config1()
