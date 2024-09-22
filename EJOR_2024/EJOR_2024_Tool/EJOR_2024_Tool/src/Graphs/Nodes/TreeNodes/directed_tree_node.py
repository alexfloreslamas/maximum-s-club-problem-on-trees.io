# ~/EJOR_2024_Tool/src/Graphs/Nodes/TreeNodes/directed_tree_node.py

from src.Graphs.Nodes.TreeNodes.simple_directed_tree_node import SimpleDirectedTreeNode
from src.Graphs.Enums.enum_node_type import EnumNodeType


class DirectedTreeNode(SimpleDirectedTreeNode):
    """
    A class that represents more elaborated tree node.
    """
    def __init__(self, node_id: int):
        """
        Init method for SimpleTreeNode
        :param node_id: (int) The vertex node_id
        """
        super().__init__(node_id)
        self.local_lowest_leaf_id = -4  # This is 'a' lowest leaf in T_v; see Schäfer's algorithm
        self.height = -100
        self.level = -1
        self.distance_to_root = -3

    def reset_h_l_d_ll(self) -> None:
        """
        Resets h(v), l(v), dist(v, v_root), local lowest leaf: i.e., in T_v
        :return: None
        """
        self.local_lowest_leaf_id = -4
        self.height = -100
        self.level = -1
        self.distance_to_root = -3

    def __str__(self) -> str:
        """
        String representation of a DirectedTreeNode in the form:
            Id: node_id: int
                is root: True/False,    is leaf: True/False
                dist to root: int,    local lowest leaf: node_id: int
                height: int,    level: int

        :return: (string) a string representation of SimpleTreeNode
        """
        text = f"{super().__str__()}"
        text += f"\tdist to root: {self.distance_to_root},\tLowest leaf in Tv: {self.local_lowest_leaf_id}\n"
        text += f"\tHeight: {self.height},\t\t\tLevel: {self.level}\n"
        return text

    def reset_node(self) -> None:
        """
        Resets all information in the node
        :return: None
        """
        super().reset_node()
        self.reset_h_l_d_ll()

    def node_type(self) -> EnumNodeType:
        return EnumNodeType.DirectedTreeNode


if __name__ == "__main__":
    node = DirectedTreeNode(11)
    print(node)
