# ~/EJOR_2024_Tool/src/Algorithms/EJOR_2024/Max_DsT/upward_sweep_updated.py

import math

from src.Graphs.Graph.directed_tree import DirectedTree
from src.Graphs.Nodes.TreeNodes.dsclub_node import DSClubNode


class UpwardSweepUpdated:
    """
    A class with an algorithm to find a maximum distance-k club set in a tree graph.
    Version submitted to EJOR_2024.
    UpwardSweep:
        Objective: Computes the order of tree ^T_v[r] for each v in T.

    Notes:
        MsC: maximum s-club, MsC,
    Modified:
        08.Jun.2022
    """

    def __init__(self, T: DirectedTree[DSClubNode], k: int):
        """
        Init method for UpwardSweep
        :param T: nx.Digraph(), A tree T = (V_T, E_T) rooted at some vertex v_root in V_T
        :param k: int, Diameter for the MsC
        """

        # self.T = T.copy()
        self.T = T  # Works on the same tree
        self.k = k
        # This structure will contain:
        #   node_id: the id of the vertex where the MsC has been found
        #   r: the row in which such set was found
        #   cardinality: the cardinality of the MsC
        #
        # Syntax is as follows:
        #   best_solution = [node_id, r, cardinality].
        #
        # In the pseudocode, for (\hat v, r)
        #   \hat v = node_id; i.e., best_solution[0]
        #   r = r; i.e., best_solution[1]
        self.best_solution = [-1, -1, -1]
        # print(self.T.postorder)
        # print(self.T)

    def compute_tables(self):
        """
        Let v in V_T, this method fills v's table following a postorder traversal on the tree. There are two cases:
            v is a leaf
            v is an internal vertex.

        Notes:
            v_id = v's identifier
        :return: The list best_solution = [node_id, r, cardinality]
        """
        postorder = self.T.postorder.copy()
        for v_id in postorder:
            v = self.T.getNode(v_id)
            if v.is_leaf:
                self.fill_leaf_vertex(v)
                v.max_solution = [v_id, 0, 1]
            else:
                Cv = self.T.get_children(v.node_id).copy()
                self.case_0(v)
                self.case_1(v, Cv)
                self.case_2(v, Cv)
                self.case_3(v, Cv)
                self.optimal_solution_check(v)
                # Finds the maximum solution for T_v. From v's table, it keeps the row r with smallest number
                v.find_max_solution()
        self._find_best_solution()
        return self.best_solution

    def fill_leaf_vertex(self, v:DSClubNode):
        """
        Fills v's table when v is a leaf.
        Suppose that we are interested in a distance 2-club, then its table
        looks like:

        col=0|  col=1
        --------------
        | 1 |  v.id  |   <- Only possible club at the moment; i.e., node v
        --------------
        | 1 |  v.id  |   <- Club considering the subtree rooted at v and ending at distance 1
        --------------
        | 1 |  v.id  |   <- Club considering the subtree rooted at v and ending at distance 2
        --------------

        :param v: The leaf vertex to fill its table.
        :return: None
        """
        v.table[0][0] = 1
        v.table[0][1] = v.node_id
        # # old
        # for r in range(self.k + 1):  # Recall that v's table has k+1 rows and 2 columns
        #     v.table[r][0] = 1
        #     v.table[r][1] = v.node_id

    def case_0(self, v: DSClubNode):
        """
        Case 0: Fills in v.table[0][c]
        :param v: Current internal vertex
        :return: None
        """
        v.table[0][0] = 1
        v.table[0][1] = v.node_id

    def case_1(self, v: DSClubNode, Cv: list):
        """
        Case 1:
            Fills in v.table[r][c] for 1 <= r <= floor(k/2)
            Note: Bellow I changed floor(k/2) to floor(k/2) + 1; it is because of the range() usage in Python.
        :param v: Current internal vertex
        :param Cv: List containing the id of v's children
        :return: None
        """
        depth = min(math.floor(self.k / 2), v.height)
        for r in range(1, depth + 1):
            summation = 0
            for u_id in Cv:
                u = self.T.getNode(u_id)
                l = min(r-1, u.height)
                summation += u.table[l][0]
            v.table[r][0] = 1 + summation
            v.table[r][1] = float("nan")

    def case_2(self, v: DSClubNode, Cv: list):
        """
        Case 2:
            Fills in v.table[r][c] for floor(k/2) < r <= k-1
            Note: Bellow I changed k+1 to k; it is because of the range() usage in Python.
        :param v: Current internal vertex
        :param Cv: List containing the id of v's children
        :return: None
        """
        depth = min(self.k-1, v.height)
        for r in range(math.floor(self.k / 2) + 1, depth + 1):
            alpha = 0
            for u_id in Cv:
                u = self.T.getNode(u_id)
                u_sbr = min(self.k-r-1, u.height)
                alpha += u.table[u_sbr][0]

            ans = 0
            u_star_id = None
            for u_id in Cv:
                u = self.T.getNode(u_id)
                u_sbr = min(self.k-r-1, u.height)
                r_lbr = min(r-1, u.height)
                if (alpha - u.table[u_sbr][0] + u.table[r_lbr][0]) > ans:
                    u_star_id = u.node_id
                    ans = alpha - u.table[u_sbr][0] + u.table[r_lbr][0]

            v.table[r][0] = 1 + ans
            v.table[r][1] = u_star_id

    def case_3(self, v: DSClubNode, Cv: list):
        """
        Case 3:
            Fills in v.table[k][c]
        :param v: Current internal vertex
        :param Cv: List containing the id of v's children
        :return:
        """

        if v.height >= self.k:
            ans = 0
            u_star_id = None
            for u_id in Cv:
                u = self.T.getNode(u_id)
                depth = min(self.k-1, u.height)
                if u.table[depth][0] > ans:
                    u_star_id = u.node_id
                    ans = u.table[depth][0]
            v.table[self.k][0] = 1 + ans
            v.table[self.k][1] = u_star_id

    def optimal_solution_check(self, v: DSClubNode):
        """
        Optimal solution check
            Updates v.table[r][c] with the values of v.table[r-1][c] if the later has a larger set
        :param v:
        :return:
        """

        depth = min(self.k, v.height)
        for r in range(1, depth + 1):
            if v.table[r][0] < v.table[r - 1][0]:
                v.table[r][0] = v.table[r - 1][0]
                v.table[r][1] = v.table[r - 1][1]

    def _find_best_solution(self):
        """
        Follows a postorder traversal in T to find the vertex v with the table that contains a MsC set.
        Once v is found, it is stored in the structure best_solution = [node_id, r, cardinality].
        The criteria to update this structure is:
            1. v has the largest postorder number
            2. r is the row with smallest number in v's table (this part is computed in v.find_max_solution())
        :return: None
        """

        # if the answer in the current node is is better than max_solution: update the max_solution.
        # recall that: best_solution = [node_id, r, cardinality].
        postorder = self.T.postorder.copy()
        for v_id in postorder:
            v = self.T.getNode(v_id)
            # Here the >= is to ensure that we keep the vertex with largest postorder number.
            if v.max_solution[2] >= self.best_solution[2]:
                self.best_solution = v.max_solution.copy()
