|-- EJOR_2024_Tool
    |-- main.py
    |-- Input
    |   |-- Medium
    |   |   |-- random_30_000.gml
    |   |-- Small
    |       |-- input_graph_0.gml
    |       |-- input_graph_1.gml
    |       |-- input_graph_2.gml
    |-- Output
    |   |-- Medium
    |   |-- Small
    |   |-- T_22_16
    |   |-- T_B
    |   |-- T_D
    |   |-- T_L
    |   |-- T_Ph
    |   |-- T_eta
    |-- Settings
    |   |-- EJOR_2024_medium_example.yaml
    |   |-- EJOR_2024_small_example.yaml
    |   |-- T_22_16.yaml
    |   |-- T_B.yaml
    |   |-- T_D.yaml
    |   |-- T_L.yaml
    |   |-- T_Ph.yaml
    |   |-- T_eta.yaml
    |-- Tests
    |   |-- Testers
    |   |   |-- abstract_benchmark_tester.py
    |   |   |-- tree_s_club_s_club_tester.py
    |   |-- Testing
    |       |-- run_Schafers_and_Max_DsT.py
    |-- src
        |-- Algorithms
        |   |-- EJOR_2024
        |   |   |-- Max_DsT
        |   |   |   |-- downward_sweep.py
        |   |   |   |-- dp_msc_t_updated.py
        |   |   |   |-- upward_sweep_updated.py
        |   |   |-- Schafer
        |   |       |-- my_tree_s_club.py
        |   |       |-- tree_s_club_updated.py
        |   |-- Enums
        |       |-- enum_algorithms.py
        |-- Graphs
        |   |-- Enums
        |   |   |-- enum_node_type.py
        |   |-- Graph
        |   |   |-- directed_tree.py
        |   |   |-- simple_directed_tree.py
        |   |   |-- simple_graph.py
        |   |   |-- simple_undirected_tree.py
        |   |-- Nodes
        |       |-- simple_node.py
        |       |-- TreeNodes
        |           |-- directed_tree_node.py
        |           |-- dsclub_node.py
        |           |-- schafers_node.py
        |           |-- simple_directed_tree_node.py
        |           |-- simple_undirected_tree_node.py
        |-- Utils
            |-- input_handler.py
            |-- output_handler.py
            |-- utils.py
