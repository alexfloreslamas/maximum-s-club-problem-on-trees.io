# ~/EJOR_2024_Tool/src/Graphs/Enums/enum_node_type.py

import enum


class EnumNodeType(enum.Enum):
    """
    This Enum shall contain and be updated with all the nodes that we require
    """

    # Simplest custom node
    SimpleNode = 1

    # Tree nodes, do not confuse with bags / nodes for tree decompositions
    SimpleUndirectedTreeNode = 2
    SimpleDirectedTreeNode = 3
    DirectedTreeNode = 4
    DSClubNode = 5
    SchafersNode = 6

    # it is a simple graph, but I want colors in it
    SimpleColoured = 10


if __name__ == "__main__":
    node0:  EnumNodeType = EnumNodeType.DSClubNode
    node1:  EnumNodeType = EnumNodeType.SchafersNode

    print(node0)
    print(node1)

    print("Equals" if node0 == node1 else "Different")
