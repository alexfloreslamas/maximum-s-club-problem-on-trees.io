# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Utils/utils.py

import src.Graphs.Graph.directed_tree as dt

from networkx import Graph
from src.Graphs.Nodes.simple_node import SimpleNode
from src.Graphs.Enums.enum_node_type import EnumNodeType
from src.Algorithms.Enums.enum_algorithms import EnumAlgorithms
from src.Graphs.Nodes.TreeNodes.dsclub_node import DSClubNode
from src.Graphs.Nodes.TreeNodes.schafers_node import SchafersNode
from src.Graphs.Nodes.TreeNodes.directed_tree_node import DirectedTreeNode
from src.Algorithms.EJOR_2024.Max_DsT.dp_msc_t_updated import DPMsCT_UPDATED
from src.Algorithms.EJOR_2024.Schafer.tree_s_club_updated import TreeSClubUPDATED


def prepare_node(node_id: int, enumNodeType: EnumNodeType, **kwargs: dict):
    """
    Returns a node of the type specified by enumNodeType with all methods and attributes in such node
    :param node_id: id for the node
    :param enumNodeType: Type of node that we require
    :param kwargs: dictionary containing specific properties for the node
    :return: A node specified as above.
    """
    node = get_nodeType(enumNodeType)

    if enumNodeType in [EnumNodeType.SimpleNode, EnumNodeType.DirectedTreeNode]:
        return node(node_id)
    elif enumNodeType == EnumNodeType.DSClubNode or enumNodeType == EnumNodeType.SchafersNode:
        return node(node_id, **kwargs)
    else:
        print(f"{enumNodeType} is not supported yet...")


def get_nodeType(enumNodeType: EnumNodeType):
    if enumNodeType == EnumNodeType.SimpleNode:
        return SimpleNode
    elif enumNodeType == EnumNodeType.DirectedTreeNode:
        return DirectedTreeNode
    elif enumNodeType == EnumNodeType.DSClubNode:
        return DSClubNode
    elif enumNodeType == EnumNodeType.SchafersNode:
        return SchafersNode
    else:
        print(f"{enumNodeType} is not supported")


def prepare_directed_tree(T: Graph, root_id, enumNodeType: EnumNodeType, **kwargs):
    nodeType = get_nodeType(enumNodeType)
    ET: dt.DirectedTree[nodeType] = dt.DirectedTree[nodeType]()

    for v_id in T.nodes:
        node = prepare_node(v_id, enumNodeType, **kwargs)
        ET.addNode(v_id, node)

    ET.add_edges_from(T.edges)
    ET.set_root(root_id)
    ET.update_tree()

    return ET


def is_iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False


def _format_dict(some_input: dict, l_del: str, r_del: str, **kwargs) -> str:
    format_by_key = kwargs['format_by_key']
    format_values = kwargs['format_values']
    pairs_list: list[list] = []

    for key in some_input:
        pairs_list.append([key, some_input[key]])

    for entry in pairs_list:
        if format_by_key:
            entry[0] = format_stuff(entry[0], True)
        if format_values:
            entry[1] = format_stuff(entry[1], True, '[', ']', **kwargs)

    text = l_del
    for entry in pairs_list:
        text += f"{entry[0]}: {entry[1]}, "

    if text != l_del:  # i.e., there is something after the l_del, e.g text = [x,
        text = text[:-2]
    text += r_del

    return text


def _format_list_keeps_order(some_input: list, l_del: str, r_del: str) -> str:
    text = l_del
    for entry in some_input:
        if is_iterable(entry):
            text += f"{_to_ascii(frozenset(entry))}, "
        else:
            text += f"{_to_ascii(frozenset({entry}))}, "
    if text != l_del:
        text = text[:-2]
    text += r_del

    return text


def _to_ascii(a_set: frozenset) -> str:
    text = ""

    if a_set == frozenset({}):
        text += f"{chr(8709)}"
    else:
        for e in a_set:
            if type(e) == int:
                if 0 <= e <= 25:
                    text += f"{chr(e + 97)},"
                else:
                    text += f"{e},"
            else:
                text += f"{e},"
        text = f"{text[:-1]}"

    return text


def int_2_ascii_rep(an_int: int):
    if 0 <= an_int <= 25:
        return f"{chr(an_int + 97)}"
    return f"{an_int}"


def format_stuff(some_input, use_ascii_rep: bool, l_del: str = "", r_del: str = "", **kwargs) -> str:
    if use_ascii_rep:
        if is_iterable(some_input):
            if type(some_input) == dict:
                text = _format_dict(some_input, l_del, r_del, **kwargs)

            elif type(some_input) == list and kwargs['list_keep_order']:
                text = _format_list_keeps_order(some_input, l_del, r_del)
            else:
                text = l_del + _to_ascii(frozenset(some_input)) + r_del
        else:
            text = l_del + _to_ascii(frozenset({some_input})) + r_del
    else:
        text = f"{some_input}"

    return text


def fset_2_ascii_rep(a_set: frozenset) -> str:
    """
    This method returns a string representation of a frozenset of int. Let a_frozenset be the input frozen set. Then:
    - Input: a_frozenset = {}, output: {∅}
    - Input: a_frozenset = {i}, for i in [25], output: its representation in ascii code.
    - Input: a_frozenset = {i}, for i not in [25], output: the number i
    - Example: a_frozenset = {0, 1, 2, 26} returns {a, b, c, 26}
    :param a_set:
    :return:
    """
    if a_set == frozenset({}):
        return f"{{{chr(8709)}}}"
    else:
        element_list = []
        text = ''
        for e in a_set:
            element_list.append(e)

        for e in element_list:
            if type(e) == int:
                if 0 <= e <= 25:
                    text += f"{chr(e + 97)},"
                else:
                    text += f"{e},"
            else:
                text += f"{e},"
        text = f"{{{text[:-1]}}}"
        return text


def algo_settings(enumAlgorithm: EnumAlgorithms):
    if enumAlgorithm == EnumAlgorithms.DP_MsC_T:
        return DPMsCT_UPDATED, EnumNodeType.DSClubNode

    if enumAlgorithm == EnumAlgorithms.S_CLUB:
        return TreeSClubUPDATED, EnumNodeType.SchafersNode
