# ~/EJOR_2024_Tool/EJOR_2024_Tool/src/Utils/input_handler.py

import os
import networkx as nx
from glob import glob


def gml_2_graph(vertex_id_type, input_dir, file_name=None):
    """
    Reads a graph from a GML file
    :param vertex_id_type: Right now, the only value that it can take is "int". In the future this might change
    :param input_dir: Directory from which to read the graph(s)
    :param file_name: The GML file to read. If no name is given then the all GML files in the input_dir are read
    :return: Either a single undirected networkx graph or a list of undirected networkx graphs
    """
    if file_name is None:
        G = []
        file_list = gml_file_list(input_dir)

        for file in file_list:
            G.append(_load_graph(vertex_id_type, input_dir, os.path.basename(file)))

        return G
    return _load_graph(vertex_id_type, input_dir, file_name)


def gml_file_list(input_dir):
    """
    From the input_dir, it returns a list with all the .gml files in it
    :param input_dir: a directory path.
    :return: a list with all .gml files in the given path. Each entry of the list is in the form: /Dir/.../file.gml
    """
    pattern = f"{input_dir}/*.gml"
    return glob(pattern)


def _load_graph(vertex_id_type, input_dir, file_name):
    """
    Reads the single graph from the specified input_dir and file_name
    :param vertex_id_type: The only value it accepts is "int"
    :param input_dir: Directory from which to read the graph
    :param file_name: The name of the GML file to read.
    :return: An undirected networkx graph.
    """
    full_path = f"{input_dir}/{file_name}"
    if '.gml' not in full_path:
        full_path += ".gml"

    G = nx.read_gml(full_path, label="id")

    if vertex_id_type == "int":
        G = nx.convert_node_labels_to_integers(G, 0)

    return G


def gml_2_graph_from_path(vertex_id_type, path):
    basename = os.path.basename(path)
    input_dir = os.path.dirname(path)
    return gml_2_graph(vertex_id_type, input_dir, basename)
