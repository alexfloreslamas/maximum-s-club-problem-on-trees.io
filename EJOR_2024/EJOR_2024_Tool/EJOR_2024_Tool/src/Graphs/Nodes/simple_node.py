# ~/EJOR_2024_Tool/src/Graphs/Nodes/simple_node

from src.Graphs.Enums.enum_node_type import EnumNodeType
from abc import ABC, abstractmethod


class SimpleNode(ABC):
    """
    A class that represents a simple or basic node of a graph.
    """

    def __init__(self, node_id: int):
        """
        Init method for the SimpleNode
        :param node_id (int): The vertex node_id.
        """
        self.node_id = node_id
        self.type_of_node = EnumNodeType.SimpleNode

    def __str__(self):
        """
        String representation of the SimpleNode in the form: "Id: node_id"
        :return:(string) Returns a string representation of the SimpleNode
        """
        return f"Id: {self.node_id}"

    @abstractmethod
    def node_type(self) -> EnumNodeType:
        return EnumNodeType.SimpleNode

    @abstractmethod
    def reset_node(self):
        pass
