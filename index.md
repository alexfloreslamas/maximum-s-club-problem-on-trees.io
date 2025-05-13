<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

# 'A dynamic programming algorithm for the maximum $s$-club problem on trees'

**Authors:** [José Alberto Fernández-Zepeda](https://dblp.org/pid/13/7045), [Alejandro Flores-Lamas](https://alexfloreslamas.github.io/), [Matthew Hague](https://www.cs.rhul.ac.uk/home/uxac009/), [Joel Antonio Trejo-Sánchez](https://www.cimat.mx/~joel.trejo).

---

## Abstract

Computing cliques in an undirected graph $G = (V_G, E_G)$ is a fundamental problem in social network analysis. However, in some cases, the strict definition of a clique (a subset of vertices pairwise adjacent in $G$) often limits its applicability in real-world settings. To address this issue, we study the $s$-club: a clique relaxation that induces a subgraph of diameter at most $s$. Note that a clique is simply a $1$-club. Computing a maximum $s$-club is a computationally challenging problem, as it is NP-hard for any for any positive integer $s$ in arbitrary graphs. Thus, this paper presents a simple dynamic programming algorithm that efficiently computes a maximum $s$-club on an $n$-vertex tree in $O(s \cdot n)$ time. This algorithm outperforms existing algorithms for trees in theory and practice. This approach is a stepping stone towards computing maximum $s$-clubs on tree-like graphs.

**Keywords:** Maximum $s$-club, Clique relaxations, Dynamic programming, Tree graphs, Graph algorithms

---

- A dynamic programming algorithm for the maximum $s$-club problem on trees: 
  - [Artifact page](./EJOR_2024/Artifact.md)
  - [Database page](./EJOR_2024/Database.md)
  - [Reproducibility of results](./EJOR_2024/Experiments.md)
- [License](./license)
- [European Journal of Operational Research](https://www.sciencedirect.com/journal/european-journal-of-operational-research).

---

[//]: # Style  for tables and paragraph

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

