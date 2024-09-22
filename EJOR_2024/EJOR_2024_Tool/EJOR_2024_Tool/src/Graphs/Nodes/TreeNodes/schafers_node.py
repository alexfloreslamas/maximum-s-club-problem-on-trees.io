# ~/EJOR_2024_Tool/src/Graphs/Nodes/TreeNodes/schafers_node.py

from src.Graphs.Nodes.TreeNodes.directed_tree_node import DirectedTreeNode
from src.Graphs.Enums.enum_node_type import EnumNodeType


class SchafersNode(DirectedTreeNode):
    """
    A class with basic attributes and methods required by the Schäfer's algorithm to compute a maximum distance k-club
    in tree graphs.

    Notes:
        These come from Schäfer's thesis "Schäfer, A., 2009. Exact algorithms for s-club finding and related problems
        (Doctoral dissertation, Friedrich-Schiller-University Jena."
            - Schäfer's work uses the term s-club:
                - Let G be a graph with G = (V, E), then an s-club is a subset of vertices S ⊆ V such that the diameter
                of G[S] is at most s.
            - Schäfer's work does not demand the maximality with respect to inclusion. See p.12

            - s-club problem as in Schäfer's work:
                - Input: An undirected graph G = (V, E) with integers s, k ≥ 2.
                - Question: Is there a set of vertices S ⊆ V of size at least k such that G[S] has diameter at most s?

        Particularities:
            - For tree graphs (and for us) s-club == distance-s club.
            - Since we are looking for a maximum set, we omit the part of "S ⊆ V of size at least k"
            - Schäfer's algorithm finds a maximum s-Club on trees in O(n · s^2) time.
    """

    def __init__(self, node_id: int, **kwargs):
        super().__init__(node_id)
        if "s" in kwargs:
            self.s = kwargs['s']
        else:
            self.s = kwargs['diameter']

        self.table = [[0 for _ in range(2)] for _ in range(self.s + 1)]

    def __str__(self) -> str:
        text = super().__str__()
        text += f"\tdistance s: {self.s}\t\tTable: {self.table}\n"
        return text

    def reset_node(self):
        """
        Resets all information in the node
        :return: None
        """
        super().reset_node()
        self.table = [[0 for _ in range(2)] for _ in range(self.s + 1)]

    def node_type(self) -> EnumNodeType:
        return EnumNodeType.SchafersNode


if __name__ == "__main__":
    node_id = 11
    diameter = k = s = 3
    kwargs = {"k": k, "s": s, "diameter": diameter}
    node = SchafersNode(node_id, **kwargs)
    print(node)
