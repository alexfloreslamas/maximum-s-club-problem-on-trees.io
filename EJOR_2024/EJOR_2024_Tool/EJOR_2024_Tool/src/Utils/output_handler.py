# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Utils/output_handler.py

import os
import re
import csv
import networkx as nx
import src.Utils.utils as utils
from pyvis.network import Network
from src.Graphs.Enums.enum_node_type import EnumNodeType


def _simple_graph_coloured(G: nx.Graph, use_ascii_rep: bool = False, **kwargs) -> nx.Graph:
    H:                          nx.Graph = nx.Graph()

    if kwargs:
        edge_colour:            str
        edge_width:             int = 2

        for node_id in G.nodes:
            node_colour: str = kwargs['covered_vertex_colour'] if node_id in kwargs['S'] else kwargs['default_vertex_colour']
            node_label:  str = G.nodes[node_id]['label']
            H.add_node(node_id, color=node_colour, label=node_label)

        for u_id, v_id in G.edges:
            end_points_colours: tuple[str, str] = (H.nodes[u_id]['color'], H.nodes[v_id]['color'])

            if all(v_colour == kwargs['spine_vertex_colour'] for v_colour in end_points_colours):
                edge_colour = kwargs['spine_edge_colour']

            elif all(v_colour in (
                    kwargs['spine_vertex_colour'], kwargs['covered_vertex_colour'], kwargs['pivot_vertex_colour']
            ) for v_colour in end_points_colours):
                edge_colour = kwargs['covered_edge_colour']
            else:
                edge_colour = kwargs['default_edge_colour']

            H.add_edge(u_id, v_id, color=edge_colour, width=edge_width)
    else:
        for node_id in G.nodes:
            H.add_node(node_id, label=utils.format_stuff(node_id, use_ascii_rep))
        H.add_edges_from(G.edges)

    return H


def graph_2_file(G, output_dir, file_name, extension, use_ascii_rep=False, enum_node_type=None, **kwargs):
    """
    Saves a simple networkx graph to either gml/html files
    :param enum_node_type:
    :param kwargs:
    :param use_ascii_rep:
    :param G:
    :param output_dir:
    :param file_name:
    :param extension: gml / html
    :return:
    """

    full_name = _get_file_full_name(output_dir, file_name, extension)

    if enum_node_type == EnumNodeType.SimpleColoured:
        H: nx.Graph = _simple_graph_coloured(G, use_ascii_rep, **kwargs)
    else:
        if 'data' in G.nodes[0]:  # This is a tree decomposition or a special graph
            H = _relabel_graph(G, use_ascii_rep=use_ascii_rep)
        else:  # These are simple graphs
            if use_ascii_rep:
                H = _relabel_simple_graph(G)
            else:
                H = G.copy()

    _save_graph(H, full_name, extension)


def _relabel_simple_graph(G):
    H = nx.DiGraph() if nx.is_directed(G) else nx.Graph()

    for v_id in G.nodes:
        H.add_node(v_id, label=utils.int_2_ascii_rep(v_id))

    for u, v in G.edges:
        H.add_edge(u, v)

    return H


def _relabel_graph(G, use_ascii_rep=False):
    if nx.is_directed(G):
        H = nx.DiGraph()
    else:
        H = nx.Graph()

    mapping = dict()
    regex = r"\{.*?\}"

    data_type = type(G.nodes[0]['data'])

    for node_id in G.nodes:
        if data_type == frozenset:
            if use_ascii_rep:
                txt = utils.fset_2_ascii_rep(G.nodes[node_id]['data'])
            else:
                txt = str(G.nodes[node_id]['data'])
        else:  # Todo: I need to change this to something like: data_type == BagNode:
            if use_ascii_rep:
                txt = utils.fset_2_ascii_rep(G.nodes[node_id]['data'].vertex_set)
            else:
                txt = str(G.nodes[node_id]['data'].vertex_set)
                # txt = str(G.nodes[node_id]['data'].vertex_set)

        matches = re.findall(regex, txt)
        new_id = f"{node_id}: "

        if matches:
            new_id += f"{matches[0]}"
        else:
            new_id += "{}"

        H.add_node(new_id)
        mapping[node_id] = new_id

    for u, v in list(G.edges):
        H.add_edge(mapping[u], mapping[v])

    return H


def _get_file_full_name(output_dir, file_name, extension, counter=None):
    # gets the name without the extension from filename (it works even without file name having extension)
    temp_name = os.path.splitext(file_name)[0]  # e.g., file_name = "tree" or "tree.gml" --> temp_name = "tree"
    if counter is not None:  # G is a list of graphs
        temp_name += f"_{counter}{extension}"  # e.g. tree_11.gml
    else:  # G is only one graph
        temp_name += f"{extension}"  # e.g., tree.gml

    return f"{output_dir}/{temp_name}"  # e.g., /Output/tree_11.gml


def _save_graph(graph, full_name, extension):
    if extension == '.gml':
        nx.write_gml(graph, full_name)
    else:  # extension = '.html'

        nt = Network("900px", "1200px")
        nt.from_nx(graph)
        nt.repulsion(spring_length=16)
        # nt.show_buttons(filter_=['physics', 'nodes', 'edges'])
        nt.show_buttons(filter_=['physics'])
        nt.save_graph(full_name)


def save_2_tsv(row_list, destination):
    # 'a' Opens a file for appending. The file pointer is at the end of the file if the file exists.
    # That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
    with open(destination, 'a') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for row in row_list:
            tsv_writer.writerow(row)
