<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

# **Artifact page:** 'A dynamic programming algorithm for a maximum $s$-club set on trees'

- [Home Page](../index.md)
- [Database Page](Database.md)
- [Reproducibility of results](Experiments.md)


**Authors:** [José Alberto Fernández-Zepeda](https://dblp.org/pid/13/7045), [Alejandro Flores-Lamas](https://alexfloreslamas.github.io/), [Matthew Hague](https://www.cs.rhul.ac.uk/home/uxac009/), [Joel Antonio Trejo-Sánchez](https://www.cimat.mx/~joel.trejo).

---


## Description

Experiments in the article "A dynamic programming algorithm for a maximum $s$-club set on trees" were done using the code in this page. This artifact contrains source code (in Python) for the implementations of the Schäfer’s[^1] and Max-D*s*T[^2] algorithms.


## Assets

**Artifact** The tool we used for the experiments for the paper submitted to [European Journal of Operational Research](https://www.sciencedirect.com/journal/european-journal-of-operational-research)

- [Download as a zip file](./EJOR_2024_Tool/EJOR_2024_Tool.zip)
- [Check it on GitHub](https://github.com/alexfloreslamas/EJOR_2024_Tool)

**Reproducibility of results**

- Please see this [web page](./Database.md) for information related to the database.

- Instructions to reproduce the experiments: [experimental web page](Experiments.md).


## Instructions

### General Installation

- There's no installation procedure; please [download the zip file](./EJOR_2024_Tool/EJOR_2024_Tool.zip) or [clone the project](https://github.com/alexfloreslamas/maximum-s-club-set-on-trees.io).

#### Software Dependencies

- EJOR_2024_Tool is written in Python 3.10, yet it can be run on version 3.9x or later.

- EJOR_2024_Tool also requires the following packages:
  - [NetworkX](https://networkx.org/)
  - [YAML](https://yaml.org/)
  - [pandas](https://pandas.pydata.org/)
  - [pyvis](https://pyvis.readthedocs.io/en/latest/index.html)


#### Selected contents

See [Script files and folder structure](#script-files-and-folder-structure) for the entire contents of the artifact.

*Main file:*

- `/EJOR_2024_Tool/main.py`

*Schäfer's implementation:*

- `/EJOR_2024_Tool/src/Algorithms/EJOR_2024/Schafer`

*DPsC implementation:*

- `/EJOR_2024_Tool/src/Algorithms/EJOR_2024/DPsC`

*I / O folders:*

- Input: `/EJOR_2024_Tool/Input/`
- Output: `/EJOR_2024_Tool/Output/`

*Configuration file:*

 * `/EJOR_2024_Tool/Settings`
    * `EJOR_2024_small_example.yaml` <-- Configuration file to execute Schäfer's and Max-D*s*T on three 'small-size' trees stored the path: `/EJOR_2024_Tool/Input/Small`; result files will be stored in `/EJOR_2024_Tool/Output/Small`.

    * `EJOR_2024_medium_example.yaml` <-- Configuration file to execute both Schäfer's and Max-D*s*T on one 'medium-size' tree stored the path: `/EJOR_2024_Tool/Input/Medium`; result files will be stored in `/EJOR_2024_Tool/Output/Medium`.


### Other instructions and example of execution

After unpacking the artifact, EJOR_2024_Tool can be run as follows:

- Open a command-line interpreter and navigate to the 'EJOR_2024_Tool' folder.
- Type the following command: 

```bash
$ python main.py Settings/EJOR_2024_small_example.yaml
```

In the above example, we call the `main.py` file with the parameters of `EJOR_2024_small_example.yaml`. In particular this example proceeds as follows:


1. EJOR_2024_Tool reads the GML files in `/EJOR_2024_Tool/Input/Small`.
2. EJOR_2024_Tool transforms each file into a tree with the attributes required by the algorithms.
3. EJOR_2024_Tool executes Max-D*s*T and Schäfer's algorithms sequentially with the parameters specified in the YAML file.
4. EJOR_2024_Tool saves in TSV files (`EJOR_2024_Tool/Output/Small`) the outcome of the execution of the algorithms.

### Experimental Installation

- Instructions for repeating the experiments are provided on the [experimental web page](Experiments.md).


## Script files and folder structure

```
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
    |       |-- run_Schafers_and_DPsC.py
    |-- src
        |-- Algorithms
        |   |-- EJOR_2024
        |   |   |-- DPsC
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
```

---


[^1]: Schäfer, A.: Exact algorithms for *s*-club finding and related problems. Ph.D. thesis, Friedrich-Schiller-University Jena (2009).
[^2]: Our dynamic programming algorithm that finds a maximum *s*-club on trees.

[//]: # Style for tables and paragraph

<style>
  table {
    border-collapse: collapse;
  }

  td, th {
    border: 1px solid #999;
    padding: 0.5rem;
    text-align: center;
  }

  p {
    text-align: justify;
  }
</style>
