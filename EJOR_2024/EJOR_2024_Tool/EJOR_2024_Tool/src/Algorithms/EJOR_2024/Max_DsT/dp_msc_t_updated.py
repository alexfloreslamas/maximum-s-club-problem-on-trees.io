# ~/EJOR_2024_Tool/src/Algorithms/EJOR_2024/Max_DsT/dp_msc_t_updated.py

from src.Graphs.Graph.directed_tree import DirectedTree
from src.Graphs.Nodes.TreeNodes.dsclub_node import DSClubNode
from src.Algorithms.EJOR_2024.Max_DsT.downward_sweep import DownwardSweep
from src.Algorithms.EJOR_2024.Max_DsT.upward_sweep_updated import UpwardSweepUpdated


class DPMsCT_UPDATED:
    """
    A class with an algorithm to find a maximum distance-k club set in a tree graph.
    Version submitted to EJOR_2024.

    Objective: Computes a MsC in a rooted tree of order n in O(kn) time.

    Notes:
        MsC: maximum s-club, MsC,
    Modified:
        08.Jun.2022
    """

    def __init__(self, T: DirectedTree[DSClubNode], k: int, execute_downward_sweep: bool):
        self.T = T
        self.k = k
        self.execute_downward_sweep = execute_downward_sweep
        # [node_id, row, cardinality]
        self.best_solution = [-1, -1, -1]
        self.S = []

    def compute(self):
        """
        This is the main body of the DP-MsC-T algorithm
        :return: None
        """
        upward_sweep = UpwardSweepUpdated(self.T, self.k)
        self.best_solution = upward_sweep.compute_tables()
        # print(self.best_solution) # Uncomment this line to see the results
        if self.execute_downward_sweep:
            self.identify_vertices_in_S()

    def identify_vertices_in_S(self):
        # print("About to execute DownwardSweep")
        v = self.best_solution[0]
        r = self.best_solution[1]
        downward_sweep = DownwardSweep(self.T, self.k, v, r)
        self.S = downward_sweep.S.copy()
        # print(f"|S|: {len(self.S)},\tS: {self.S}")

    def __str__(self):
        text = f"For k = {self.k}:\n"
        text += f"[node_id, row, |S|] = {self.best_solution}"
        if self.execute_downward_sweep:
            text += f"\nS: {self.S}"
        return text
