# ~/EJOR_2024_Tool/src/Algorithms/EJOR_2024/Schafer/my_tree_s_club.py

import math

from src.Graphs.Graph.directed_tree import DirectedTree
from src.Graphs.Nodes.TreeNodes.schafers_node import SchafersNode


class MyTreeSClub:
    def __init__(self, T: DirectedTree[SchafersNode], s: int):
        self.T = T  # Works on the same tree
        self.s = s
        self.dict_levels = {}
        self.key_list = []
        self.v_root = self.T.getNode(self.T.root_id)
        self.sizeS_sol = 0
        self.sizeS = 0
        self.u_sol_id = None
        self.v_ordered_list = []
        self.identify_vertices_by_levels()
        self._get_vertices_2_process_by_level()
        # [node_id, row, cardinality]
        self.best_solution = []

    def identify_vertices_by_levels(self):
        """
        Computes h(v), l(v), dist(v, v_root), local lowest leaf: i.e., in T_v
        :return: None
        """

        self.dict_levels.clear()
        # Initialises the dictionary with empty lists
        for i in range(0, self.v_root.level + 1):
            self.dict_levels[i] = []

        # Identifies the vertices in each level; in [0: l(r)]
        # Note that we are computing for all levels

        for v_id in self.T.nodes:
            v = self.T.getNode(v_id)
            self.dict_levels[v.level].append(v_id)

        self.key_list = list(self.dict_levels.keys())
        self.key_list.sort(reverse=False)

    def _get_vertices_2_process_by_level(self):

        for level in range(0, self.v_root.level + 1):
            for v_id in self.dict_levels[level]:
                self.v_ordered_list.append(v_id)

    def _base_case(self):
        """
        Lines 4 to 6
        :return: None
        """

        for v_id in list(self.T.nodes):
            v = self.T.getNode(v_id)
            v.table[0][0] = 1

    def _filling_initial_values(self):
        """
        Lines 7 to 12
        :return: None
        """
        for o in range(1, self.v_root.level + 1):
            for v_id in self.dict_levels[o]:
                v = self.T.getNode(v_id)
                Cv = self.T.get_children(v_id)
                for d in range(1, min(o, self.s) + 1):
                    ans = 0
                    for u_id in Cv:  # This is the sum in Line 10 of Pseudocode
                        u = self.T.getNode(u_id)
                        ans += u.table[d - 1][0]
                    v.table[d][0] = ans

    def _outer_repeat(self):
        # while len(self.v_ordered_list) > 0:

        while len(list(self.T.nodes)) > 0:
            v0_id = self.v_ordered_list.pop(0)
            # print(v0_id)
            # self._printer("")

            P = self.T.get_path_towards_root(v0_id, self.s)  # get me a path of length at most s that starts at v0
            next_index = self._upper_half(P)
            self._lower_half(P, next_index)

            if self.sizeS >= self.sizeS_sol:
                self.sizeS_sol = self.sizeS
                self.u_sol_id = v0_id

            self.T.removeNode(v0_id)

            for i in range(1, len(P)):
                vi_id = P[i]
                vi = self.T.getNode(vi_id)
                vi.table[i][0] = vi.table[i][0] - 1

    def _upper_half(self, P: list):  # Original without jumping
        self.sizeS = 0
        i = len(P) - 1

        while i > math.floor(self.s / 2):
            depth = self.s - i
            v = self.T.getNode(P[i])
            u = self.T.getNode(P[i - 1])
            for j in range(0, depth + 1):
                self.sizeS += v.table[j][0]
                if j > 0:
                    self.sizeS -= u.table[j - 1][0]

            i -= 1
        return i
    # def _upper_half(self, P: list):
    #     # This is the code with the 'jumping technique' of Schäfers, yet it does not work properly
    #     # since it does not count all the vertices that belong to the set, see my notes for an example
    #
    #     self.sizeS = 0
    #     i = len(P) - 1
    #
    #     print(f"{len(P) = }")
    #     print(f"{i = }\n>>>>>>>>>>>>>")
    #
    #     while i > math.floor(self.s / 2):
    #         print(f"\tcurrent i {i = }\n\tEntering: {self.sizeS = }")
    #
    #         depth = self.s - i
    #         print(f"\t{self.s} - {i} = {depth = }")
    #
    #         v = self.T.getNode(P[i])
    #         for j in range(0, depth + 1):
    #             self.sizeS += v.table[j][0]
    #             print(f"\t\t{v.table[j][0]}")
    #
    #         print(f"\tCurrent {self.sizeS = }")
    #
    #         if depth == 0:
    #             print(f"\tInside depth = 0")
    #             i -= 1
    #         else:
    #             print(f"\tInside depth > 0")
    #             self.sizeS -= 1
    #             i -= depth
    #
    #         print(f"\tNew {self.sizeS = }")
    #         print(f"\tNext i{i = }")
    #
    #     print("<<<<<<<<<<<<<<<<<<<<")
    #
    #     print(f"Final {i = }\n{self.sizeS = }")
    #     return i
        # if i >= 0: # returns the next index in P to be processed
        #     return i
        # else:
        #     # Do I ever enter here? I don't think so...
        #     # If I don't, then I don't even require the if
        #     return 0

    def _lower_half(self, P, i):
        # if len(P) == 1: # i.e., P = {v_root}
        #     depth = math.floor(self.s / 2)
        # else:
        #     depth = self.s - i

        # Since I have been removing processed vertices and updating v's table I no longer require the above.
        # depth = self.s - i
        depth = (math.floor(self.s / 2))

        v_id = P[i]
        v = self.T.getNode(v_id)
        depth = min(depth, v.level)  # this line is new and correct
        for j in range(0, depth + 1):
            self.sizeS += v.table[j][0]

    def compute_tables(self):
        # I'm going to be talking about "Lines". When I do so I mean lines in Schäfer's pseudocode.
        # T's copy is already in AbstractTreeSClub's init method, nope, HERE

        # Lines 4 to 6
        self._base_case()

        # Lines 7 to 12
        self._filling_initial_values()

        # Lines 13 to 30
        self._outer_repeat()

        # uncomment these lines to see the results
        # print(f"self.s: {self.s}")
        # print(f"sizeS_sol: {self.sizeS_sol}")
        # print(f"u_sol_id: {self.u_sol_id}\n")

        self.best_solution.append(self.u_sol_id)
        self.best_solution.append(float("nan"))
        self.best_solution.append(self.sizeS_sol)
        return self.best_solution

    def __str__(self):
        return f"[node_id, row, |S|] = {self.best_solution}"
