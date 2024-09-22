# ~/EJOR_2024_Tool/Tests/Testers/abstract_benchmark_tester.py

import time
from abc import ABC, abstractmethod
import src.Utils.input_handler as reader
import src.Utils.output_handler as writer


class AbstractBenchMarkTester(ABC):
    def __init__(self, **kwargs):
        self.algorithm = kwargs['the_algorithm']
        self.nodeType = kwargs['nodeType']
        self.diameters: list = kwargs["diameters"]
        self.benchmark_dir = kwargs["benchmark_dir"]
        self.output_logs_dir = kwargs["output_logs_dir"]
        self.results_log = f"{kwargs['log_name']}-results.tsv"
        self.resultsList: list = []  # It contains the file_name with solution size.
        # self.ok_log, self.bad_log, self.time_log = self._get_log_names(kwargs['log_name'])
        # self.error_dictionary = {}  # It will contain as key the filename, as value the root node that causes the
        # answer to differ
        self.identify_vertices = kwargs["identify_vertices"]
        self.resultsList.append(kwargs["header"])
        self.measure_time = kwargs['measure_time']
        self.verbose = kwargs['verbose']

        print(f"Running ---> {type(self).__name__}")

    # def _get_log_names(self, log_name):
    #     return f"{log_name}-results.tsv", f"{log_name}-exemptions.tsv", f"{log_name}-time.tsv"

    @abstractmethod
    def test(self, root_node=None):
        """
        This method must call the heart class (also defined in the child method)
        :param root_node:
        :return:
        """
        pass

    @abstractmethod
    def __str__(self):
        text = f"Execution summary for the graphs in{self.benchmark_dir}\n"
        text += f"Running {type(self).__name__}:\n"
        text += "Log file(s):\n"
        text += f"\t{self.output_logs_dir}/{self.results_log}\n"
        return text

    @abstractmethod
    def heart(self, T, file, root_node, diameter):
        pass

    def outer_loop_tester(self, root_node):
        graph_list = reader.gml_file_list(self.benchmark_dir)
        counter = 1
        for file in graph_list:
            if self.verbose:
                print(f"Current graph: {file}")

            for diameter in self.diameters:
                if self.verbose:  # note: change it for a decorator that measures execution time.
                    print(f"Reading the graph:\r")
                    begin_read_time = time.time()
                    T = reader.gml_2_graph_from_path("int", file)
                    end_read_time = time.time()
                    print(f"\tReading time: {end_read_time - begin_read_time}, file: {counter}/{len(graph_list)}, diameter: {diameter}; {root_node = },\r")
                else:
                    T = reader.gml_2_graph_from_path("int", file)

                if self.verbose:
                    print(f"Processing file: {counter}/{len(graph_list)} for diameter: {diameter}; {root_node = }\r")
                else:
                    print(f"Processing file: {counter}/{len(graph_list)} for diameter: {diameter}; {root_node = }", end="\r")
                # heart MUST be implemented by children classes
                self.heart(T, file, root_node, diameter)
            counter += 1

        print("\n")
        # self.resultsList > 0 has he following meanings:
        # If True, it means that I am running a DP tester, so all results are already in a dictionary
        # If False, it means I am running, perhaps, an exhaustive tester, so I have been saving results one by one in
        # its heart method.

        if len(self.resultsList) > 0:
            writer.save_2_tsv(self.resultsList, f"{self.output_logs_dir}/{self.results_log}")
        print(self)
