<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

# 'A dynamic programming algorithm for a maximum $s$-club set on trees'

**Authors:** [José Alberto Fernández-Zepeda](https://dblp.org/pid/13/7045), [Alejandro Flores-Lamas](https://alexfloreslamas.github.io/), [Matthew Hague](https://www.cs.rhul.ac.uk/home/uxac009/), [Joel Antonio Trejo-Sánchez](https://www.cimat.mx/~joel.trejo).

---

## Abstract

Finding clubs in an undirected graph $G = (V_G, E_G)$ is a fundamental problem in social network analysis. However, in some cases, the strict definition of a club (a complete subgraph of $G$) can be too restrictive to model some social concepts. To address this issue, we study a relaxed version of the club, known as the $s$-club. An $s$-club is a maximal subgraph of $G$ in which the distance in $G$ between any pair of vertices of the subgraph is less than or equal to some positive integer $s$ (where a club is simply a $1$-club). Finding the maximum $s$-club in a graph is a computationally challenging problem, as it is NP-hard for any $s$ in arbitrary graphs. To overcome this challenge, we present a simple dynamic programming algorithm that efficiently solves the maximum $s$-club problem on an $n$-vertex tree in $O(s \cdot n)$ time for $s \geq 2$. This algorithm outperforms existing algorithms in theory and practice. This approach is a stepping stone to finding a maximum $s$-club in less restrictive graphs.

**Keywords:** Distance $s$-club, Graph algorithms, Trees, Dynamic programming, $s$-club.

---

- A dynamic programming algorithm for a maximum $s$-club set on trees: 
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

