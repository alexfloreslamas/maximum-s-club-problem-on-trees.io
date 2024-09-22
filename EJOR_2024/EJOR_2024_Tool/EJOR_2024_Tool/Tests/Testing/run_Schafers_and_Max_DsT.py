# ~/EJOR_2024_Tool/Tests/Testing/run_Schafers_and_Max_DsT.py

import os
import glob
import pandas as pd

from src.Graphs.Enums.enum_node_type import EnumNodeType
from Tests.Testers.tree_s_club_s_club_tester import Tester
from src.Algorithms.Enums.enum_algorithms import EnumAlgorithms


def merge_result_files(output_logs_dir: str) -> None:
    # >>> This part reads the TSV files saved before and merges into just one file<<<
    # >>> Supposition: all files have the same entries <<<
    all_files = glob.glob(os.path.join(output_logs_dir, "*.tsv"))
    df_from_each_file = (pd.read_csv(f, sep='\t', index_col='File') for f in all_files)
    df_merged = pd.concat(df_from_each_file, axis=1)
    df_merged.to_csv(f"{output_logs_dir}/merged.tsv", sep='\t')

    print(f"You can find individual results and a merged file with results in: {output_logs_dir}\n")


def execute(config: dict):
    # Scripts to run and identify_vertices
    run_Max_DsT = config['run_Max_DsT']
    run_Schafers = config['run_Schafers']
    merge_files = config['merge_files']

    # This part does the following:
    #   1. reads the input trees
    #   2. computes the cardinality |^S| of a solution for each graph (note: it does not identify the vertices in ^S)
    #   3. saves |^S| in TSV files.

    if run_Max_DsT:
        config["log_name"] = config["msc_log_name"]
        config['header'] = ['File', 'Diameter', 'Max_DsT_|S|', 'Max_DsT_time']
        config['nodeType'] = EnumNodeType.DSClubNode
        config['the_algorithm'] = EnumAlgorithms.DP_MsC_T

        msc_tester = Tester(**config)
        msc_tester.test(config['initial_root_node'])
        print("\n")

    if run_Schafers:
        # Note: this will run my implementation of the Schäfer's algorithm
        config["log_name"] = config["s_club_log_name"]
        config['header'] = ['File', 'Diameter', 'Schäfer_|S|', 'Schäfer_time']
        config['nodeType'] = EnumNodeType.SchafersNode
        config['the_algorithm'] = EnumAlgorithms.S_CLUB

        tree_s_club_tester = Tester(**config)
        tree_s_club_tester.test(config['initial_root_node'])
        print("\n")

    # >>> This part reads the TSV files saved above and merges into just one file<<<
    # >>> Supposition: all files have the same entries <<<
    if merge_files:
        merge_result_files(config["output_logs_dir"])
    else:
        print(f"You can find individual results in: {config['output_logs_dir']}\n")
