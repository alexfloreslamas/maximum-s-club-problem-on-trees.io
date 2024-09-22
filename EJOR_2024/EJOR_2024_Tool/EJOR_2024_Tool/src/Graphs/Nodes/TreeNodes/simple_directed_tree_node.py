# ~/EJOR_2024_Tool/src/Graphs/Nodes/TreeNodes/simple_directed_tree_node.py
from src.Graphs.Enums.enum_node_type import EnumNodeType
from src.Graphs.Nodes.TreeNodes.simple_undirected_tree_node import SimpleUndirectedTreeNode


class SimpleDirectedTreeNode(SimpleUndirectedTreeNode):
    """
    A class that represents a simple or basic tree node.
    """
    def __init__(self, node_id: int):
        """
        Init method for SimpleDirectedTreeNode
        :param node_id: (int) The vertex node_id
        """
        super().__init__(node_id)

        self.is_root = False

    def __str__(self) -> str:
        # It will be something like:
        # Id: 11
        #   is leaf: False		is root: False
        text = f"{super().__str__()}"
        text += f"\t\tis root: {self.is_root}\n"

        return text

    def reset_node(self) -> None:
        super().reset_node()
        self.is_root = False

    def node_type(self) -> EnumNodeType:
        return EnumNodeType.SimpleDirectedTreeNode


if __name__ == "__main__":
    node = SimpleDirectedTreeNode(11)
    print(node)
