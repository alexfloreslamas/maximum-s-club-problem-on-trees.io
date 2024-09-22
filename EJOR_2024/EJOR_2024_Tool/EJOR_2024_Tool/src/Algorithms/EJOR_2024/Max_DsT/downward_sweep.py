# ~/EJOR_2024_Tool/src/Algorithms/EJOR_2024/Max_DsT/downward_sweep.py

import math

from src.Graphs.Graph.directed_tree import DirectedTree
from src.Graphs.Nodes.TreeNodes.dsclub_node import DSClubNode


class DownwardSweep:
    """
        A class with an algorithm to find a maximum distance-k club set in a tree graph.
        Version submitted to EJOR_2024.
        DownwardSweep:
            Objective: identify the subset ^S that denotes a MsC

        Notes:
            MsC: maximum s-club, MsC,
    Modified:
        08.Jun.2022
    """

    def __init__(self, T: DirectedTree[DSClubNode], k: int, v_id: int, r: int):
        self.T = T
        self.k = k
        self.S = []
        self._find_selected_nodes(v_id, r)

    def _find_selected_nodes(self, v_id: int, r: int):
        self.S.append(v_id)
        v = self.T.getNode(v_id)
        Cv = self.T.get_children(v.node_id)

        if v.is_leaf: return

        # Case 0, r = 0

        if r == 0: return

        # Case 1, r = from 1 to floor(k/2)

        if 1 <= r <= math.floor(self.k / 2):
            for u_id in Cv:
                self._find_selected_nodes(u_id, r - 1)

        # Case 2, r = floor(k/2) + 1 to k-1

        if math.floor(self.k / 2) < r <= self.k - 1:
            Cv.remove(v.table[r][1])
            u_star_id = v.table[r][1]
            self._find_selected_nodes(u_star_id, r - 1)

            for u_id in Cv:
                self._find_selected_nodes(u_id, self.k - r - 1)

        # Case 3, r = k

        if r == self.k:
            u_star_id = v.table[r][1]
            self._find_selected_nodes(u_star_id, r - 1)
