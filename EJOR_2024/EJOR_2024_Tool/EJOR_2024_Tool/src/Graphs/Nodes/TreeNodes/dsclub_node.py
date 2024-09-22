# ~/EJOR_2024_Tool/src/Graphs/Nodes/TreeNodes/dsclub_node.py

from src.Graphs.Nodes.TreeNodes.directed_tree_node import DirectedTreeNode
from src.Graphs.Enums.enum_node_type import EnumNodeType


class DSClubNode(DirectedTreeNode):
    """
    A class representing a node to compute a maximum s-club, MsC, on a tree graph.
    """

    def __init__(self, node_id: int, **kwargs):
        """
        Init method for the Distance-s club Node.
        :param node_id(int): The node node_id.
        """
        super().__init__(node_id)
        if "k" in kwargs:
            self.k = kwargs['k']
        else:
            self.k = kwargs['diameter']
        # This table has k+1 rows and 2 columns.
        self.table = [[0 for _ in range(2)] for _ in range(self.k + 1)]

        # This will contain the node_id with the set of maximum cardinality, the row in which such set waf found, and
        # the cardinality of the maximum s-club, MsC,. The syntax is as follows:
        # max_solution = [node_id, row, cardinality].
        self.max_solution = [-1, -1, -1]

    def __str__(self) -> str:
        """
        String representation of the SimpleTreeNode + DSClubNode
        :return:(string) Returns a string representation of the SimpleTreeNode + DSClubNode
        """

        text = super().__str__()
        text += f"\tdistance k: {self.k}\t\tTable: {self.table}\t{self.max_solution}"
        return text

    def find_max_solution(self) -> None:
        """
        Finds the local maximum solution for the distance-s club from the node table.
        :return:(list) A list of the form: [node_id, row, cardinality].
        """

        # for row in range(0, self.k + 1):
        depth = min(self.k, self.height)
        for row in range(0, depth + 1):
            # if current answer is better than max_solution: update the max_solution.
            # recall that: max_solution = [node_id, row, cardinality].
            if self.table[row][0] > self.max_solution[2]:
                self.max_solution = [self.node_id, row, self.table[row][0]]

    def reset_node(self):
        """
        Resets all information in the node
        :return: None
        """
        super().reset_node()
        self.table = [[0 for _ in range(2)] for _ in range(self.k + 1)]

    def node_type(self) -> EnumNodeType:
        return EnumNodeType.DSClubNode


if __name__ == "__main__":
    node_id = 11
    diameter = k = s = 3
    kwargs = {"k": k, "s": s, "diameter": diameter}
    node = DSClubNode(node_id, **kwargs)
    print(node)
