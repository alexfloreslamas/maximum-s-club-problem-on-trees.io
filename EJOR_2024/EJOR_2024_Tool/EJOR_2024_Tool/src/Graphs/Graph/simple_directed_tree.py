# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Graphs/Graph/simple_directed_tree.py

import networkx as nx

from typing import TypeVar
from src.Graphs.Graph.simple_undirected_tree import SimpleUndirectedTree
from src.Graphs.Nodes.TreeNodes.simple_directed_tree_node import SimpleDirectedTreeNode

NodeType = TypeVar('NodeType')


class SimpleDirectedTree(nx.DiGraph, SimpleUndirectedTree[NodeType]):
    """
    A basic class of a directed tree T = (V_T, E_T), where the root node is the one with no incoming edges.
    I try to follow the next semantics:
        - node_id: int denotes the id of some vertex; usually, I will use it in a method's signature. Nonetheless, I
                    might also use something like v0_id when the context requires it.
        - v_id: int is also an id of some vertex v in V_T. I will use it inside the body of a method.
        - v: object is a vertex with all its attributes and methods.
    """

    def __init__(self):
        super(SimpleDirectedTree, self).__init__()
        self.UT = nx.Graph()
        self.root_id = None
        self.postorder = []
        self.preorder = []

    def set_root(self, node_id: int) -> None:
        """
        Must be the last method to be called
        :param node_id:
        :return:
        """
        self.root_id = node_id
        v = self.getNode(self.root_id)
        v.is_root = True
        self.need_to_reset_nodes = True

    def get_postorder(self) -> list[int]:
        return list(nx.dfs_postorder_nodes(self, source=self.root_id))

    def get_preorder(self) -> list[int]:
        return list(nx.dfs_preorder_nodes(self, source=self.root_id))

    def update_tree(self) -> None:
        if self.need_to_reset_nodes:
            self.resetNodes()
        self._set_leaves()
        self.need_to_reset_nodes = False

        self._root_tree()  # leaves are set in the parent class
        self.postorder = self.get_postorder()
        self.preorder = self.get_preorder()
        # self.need_to_reset_nodes = False this is set in the parent class

    def _root_tree(self) -> None:
        if len(self.nodes) == 1:
            v = self.getNode(self.root_id)
            v.is_root = True
            v.is_leaf = True
        else:
            self._build_shallow_undirected_tree()
            DT = nx.bfs_tree(self.UT, self.root_id)
            edges = list(self.edges)
            for u_id, v_id in edges:
                self.remove_edge(u_id, v_id)
            self.add_edges_from(DT.edges)
            v = self.getNode(self.root_id)
            v.is_root = True
            v.is_leaf = False

    def _build_shallow_undirected_tree(self) -> None:
        self.UT.clear()

        for node_id in self.nodes:
            self.UT.add_node(node_id)

        for u_id, v_id in self.edges:
            self.UT.add_edge(u_id, v_id)

    def _set_leaves(self) -> None:
        # Since the tree is directed, we can do this to check if v is a leaf or not
        for v_id in self.nodes:
            v = self.getNode(v_id)
            Cv = len(list(self.successors(v_id))) + len(list(self.predecessors(v_id)))  # vertex v has only one edge
            if Cv == 1:  # v is a leaf vertex
                v.is_leaf = True

    def get_children(self, node_id) -> list:
        return list(self.successors(node_id))

    def get_parent(self, node_id):
        # Since we are working with directed trees, there's at most one ancestor; i.e., its parent
        ancestors = list(self.predecessors(node_id))
        if len(ancestors) == 0:
            return None
        else:
            return ancestors[0]

    def removeNode(self, v_id: int) -> None:
        # Since we are working with directed trees, there's only one ancestor
        # Let vertex p =  parent(v)
        # print(f"removing: {v_id}")
        p_id = self.get_parent(v_id)
        self.remove_node(v_id)
        if p_id is not None:
            Cp = self.get_children(p_id)
            if len(Cp) == 0:  # if p does not have any children, that means that p is now a leaf
                p = self.getNode(p_id)
                p.is_leaf = True
        else:

            if v_id == self.root_id:  # It might be the case that we already deleted v_root in the lines above
                pass
            else:
                # When v0_id does not have a parent it means that v0_id = v_root.
                # That also means that v_root is the only vertex in the graph -this comes from the way we are processing
                # the tree. Thus, v_root is a leaf.
                v_root = self.getNode(self.root_id)
                v_root.is_leaf = True
        self.need_to_reset_nodes = True

    def __str__(self) -> str:
        text = f"Nodes: {self.nodes}\n"
        text += f"Edges: {self.edges}\n"

        inverse_postorder = self.get_postorder()
        inverse_postorder.reverse()
        for v_id in inverse_postorder:
            v = self.getNode(v_id)
            text += f"{v}\n"

        return text


def config1() -> None:
    nodeType = SimpleDirectedTreeNode

    grafo: SimpleDirectedTree[nodeType] = SimpleDirectedTree[nodeType]()

    for i in range(0, 5):
        node = nodeType(i)
        grafo.addNode(i, node)

    for i in range(0, 3):
        grafo.addEdge(i, i + 1)

    grafo.addEdge(1, 4)
    print(grafo.nodes)
    print(grafo.edges)

    print("Root the tree")
    grafo.set_root(0)
    grafo.update_tree()
    print(grafo)

    print("removing vertex 3")
    grafo.removeNode(3)
    grafo.update_tree()
    print(grafo.nodes)
    print(grafo.edges)

    print(grafo)
    print(grafo.has_edge(1, 0))
    print(grafo.has_edge(0, 1))

    print("Adding vertex 3 again")
    node = nodeType(3)
    grafo.addNode(3, node)
    grafo.addEdge(3, 2)
    grafo.update_tree()
    print(grafo)
    print(f"{grafo.has_edge(2, 3) = }")
    print(f"{grafo.has_edge(3, 2) = }")
    print("---" * 22)
    for v_id in grafo.nodes:
        print(f"\nChanging the root to {v_id}\n")
        print(f"{grafo.is_directed() = }")
        grafo.set_root(v_id)
        grafo.update_tree()
        print(grafo)
    print(nx.is_directed(grafo))


if __name__ == "__main__":
    config1()
