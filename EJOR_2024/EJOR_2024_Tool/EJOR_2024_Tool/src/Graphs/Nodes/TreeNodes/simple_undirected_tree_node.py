# ~/EJOR_2024_Tool/src/Graphs/Nodes/TreeNodes/simple_undirected_tree_node.py
from src.Graphs.Nodes.simple_node import SimpleNode
from src.Graphs.Enums.enum_node_type import EnumNodeType


class SimpleUndirectedTreeNode(SimpleNode):
    """
    A class that represents a simple undirected tree node.
    """
    def __init__(self, node_id: int):
        """
        Init method for SimpleUndirectedTreeNode
        :param node_id: (int) The vertex node_id
        """
        super().__init__(node_id)
        self.is_leaf = False

    def __str__(self) -> str:
        text = f"{super().__str__()}\n"
        text += f"\tis leaf: {self.is_leaf}"
        return text

    def reset_node(self) -> None:
        self.is_leaf = False

    def node_type(self) -> EnumNodeType:
        return EnumNodeType.SimpleUndirectedTreeNode


if __name__ == "__main__":
    node = SimpleUndirectedTreeNode(11)
    print(node)
