# ~/EJOR_2024_Tool/Tests/Testers/tree_s_club_s_club_tester.py

from Tests.Testers.abstract_benchmark_tester import AbstractBenchMarkTester

import src.Utils.utils as utils
import time


class Tester(AbstractBenchMarkTester):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def test(self, root_node=None):
        if root_node is None:
            print("Just a little error: an initial root_id must be provided as root node")
        else:
            self.outer_loop_tester(root_node)

    def heart(self, T, file, root_node, diameter):
        if self.verbose:    # note: change it for a decorator that measures execution time.
            print(f"\tPreparing enhanced tree\r")
            begin_enhanced_time = time.time()
            ET = utils.prepare_directed_tree(T, root_node, self.nodeType, **{'diameter': diameter})
            end_enhanced_time = time.time()
            print(f"\t\tPreparation time: {end_enhanced_time - begin_enhanced_time}\r")

            print(f"\tRunning the main algorithm\r")
            cardinality, elapsed_time = self._compute_club_size(ET, diameter)
            print(f"\t\tRunning time: {elapsed_time}\n{'---'*22}\n")
        else:
            ET = utils.prepare_directed_tree(T, root_node, self.nodeType, **{'diameter': diameter})
            cardinality, elapsed_time = self._compute_club_size(ET, diameter)

        self.resultsList.append([file, diameter, cardinality, elapsed_time])

    def __str__(self):
        return super().__str__()

    def _compute_club_size(self, ET, diameter):
        TheAlgorithm = utils.algo_settings(self.algorithm)[0]
        algo = TheAlgorithm(ET, diameter, self.identify_vertices)

        start = time.time() if self.measure_time else 0

        algo.compute()

        end = time.time() if self.measure_time else 0
        # Recall: best_solution = [node_id, row, cardinality].
        return algo.best_solution[2], end - start
