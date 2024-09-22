# ~/EJOR_2024_Tool/src/Algorithms/EJOR_2024/Schafer/tree_s_club_updated.py

import networkx as nx

from src.Graphs.Graph.directed_tree import DirectedTree
from src.Graphs.Nodes.TreeNodes.schafers_node import SchafersNode
from src.Algorithms.EJOR_2024.Schafer.my_tree_s_club import MyTreeSClub


class TreeSClubUPDATED:
    def __init__(self, T: DirectedTree[SchafersNode], s: int, identify_vertices: bool):
        self.T = T
        self.T_copy = T.copy()
        self.s = s
        self.identify_vertices = identify_vertices
        # [node_id, row, cardinality]
        self.best_solution = [-1, -1, -1]
        self.S = []

    def compute(self):
        myTreeSClub = MyTreeSClub(self.T, self.s)
        self.best_solution = myTreeSClub.compute_tables()
        if self.identify_vertices:
            self.identify_vertices_in_S()

    def identify_vertices_in_S(self):
        u_sol = self.best_solution[0]

        candidates = nx.bfs_tree(self.T.UT, source=u_sol, depth_limit=self.s)
        u_sol_level = self.T_copy.getNode(u_sol).level

        for v_id in candidates:
            v_level = self.T_copy.getNode(v_id).level
            if u_sol_level <= v_level:
                self.S.append(v_id)

    def __str__(self):
        text = f"For s = {self.s}:\n"
        text += f"[node_id, row, |S|] = {self.best_solution}"
        if self.identify_vertices:
            text += f"\nS: {self.S}"
        return text
