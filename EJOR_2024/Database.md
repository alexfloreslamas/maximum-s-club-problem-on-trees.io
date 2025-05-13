<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

# **Database page:** 'A dynamic programming algorithm for the maximum $s$-club problem on trees'

- [Home Page](../index.md)
- [Artifact Page](Artifact.md)
- [Reproducibility of results](Experiments.md)


**Authors:** [José Alberto Fernández-Zepeda](https://dblp.org/pid/13/7045), [Alejandro Flores-Lamas](https://alexfloreslamas.github.io/), [Matthew Hague](https://www.cs.rhul.ac.uk/home/uxac009/), [Joel Antonio Trejo-Sánchez](https://www.cimat.mx/~joel.trejo).

---

## Description

This webpage contains the dataset for the experiments in the article "A dynamic programming algorithm for the maximum $s$-club problem on trees". This paper is currently under consideration for acceptance to [European Journal of Operational Research](https://www.sciencedirect.com/journal/european-journal-of-operational-research).

---

## Data documentation

The data set consists of:


- The ${\cal T}_{22-16}$ subset from [Professor Brendan McKay](https://users.cecs.anu.edu.au/~bdm/). We chose the ['tree22.16.txt'](https://users.cecs.anu.edu.au/~bdm/data/trees.html) dataset containing $12\,761$ trees; each graph has $22$ vertices and a diameter of $16$. The experiments used values of $s \in$ {{"{$8, 9, \ldots, 16$"}}}. The cumulative execution time of such a set under each algorithm appears in Table **2**, Row **1**.

- ${\cal T}_{Ph}$ is a subset of phylogenetic trees chosen from the [PhylomeDB](http://phylomedb.org/) catalogue. The chosen source file ['phylomones/phylomone_0003/ best\_trees.txt.gz'](http://phylomedb.org/download) contains $5\,722$ phylogenetic trees (S. cerevisiae phylome made from 60 completely sequenced fungal specie), the largest tree having $297$ vertices, and diameters ranging from $2$ to $64$. The experiments used this set with values of $s$ from the set {{"{$2, 3, 4, 7, 8, 13, 16, 25, 32, 49, 64$"}}}. The cumulative execution time of such a set under each algorithm appears in Table **2**, Row **14**.

- $T_D$ is [a doubly logarithmic tree](https://en.wikipedia.org/wiki/Doubly_logarithmic_tree) with height 5 ($\vert V_{T_D}\vert = 119\,041$). The experiments used this graph with values of $s =$ {{"{$4, 5$"}}}. See Table **2**, Rows **2** and **3**.

- $T_L$ is a linear tree with $10\,000$ vertices. We could think of $T_L$ as an 'opposite' of $T_D$ since $T_L$ is a tall tree and each level has precisely one vertex. The experiments used this graph with values of $s$ from the set {{"{$10, 100, 1\,000, 10\,000$"}}}. See Table **2**, Rows **4** to **7**.

- $T_B$ is a full-balanced binary tree with $2^{16}$ leaves. The experiments used this tree with values of $s =$ {{"{$5, 10, 15, 20, 25, 30$"}}}. See Table **2**, Rows **8** to **13**.

- The $T_{\eta\mathrm{e}{6}}$ trees, for $\eta \in$ {{"{$0.3, 0.5, 0.75, 1$"}}} and $\mathrm{e}{6} = 10^6$, have $0.3\times 10^6$, $0.5 \times 10^6$, $0.75 \times 10^6$, and $1\times 10^6 $ vertices, respectively. We built these trees with the instruction 'nx.random\_tree(...)' from [NetworkX](https://networkx.org/documentation/stable/reference/generated/networkx.generators.trees.random_tree.html#networkx.generators.trees.random_tree). We used the following values of $s =$ {{"{$10, 100, 500$"}}} for each tree. See Table **2**, Rows **15** to **26**.

<br><br>
**Table 1.** Dataset's source files (in GML format); files are zipped.

| Case of study             | File                                          | Case of study             | File                        |
| ------------------------- | --------------------------------------------- | ------------------------- | --------------------------- |
| ${\cal T}_{22-16}$       | [T_22_16.zip](./DB/Prof_Brendan/T_22_16.zip)   | $T_L$                     | [T_L.zip](./DB/T_L.zip)     |
| ${\cal T}_{Ph}$           | [T_Ph.zip](./DB/Phylogenetic_trees/T_Ph.zip)  | $T_B$                     | [T_B.zip](./DB/T_B.zip)     |
| $T_D$                     | [T_D.zip](./DB/T_D.zip)                       | $T_{\eta\mathrm{e}{6}}$.  | [Part 1](./DB/T_eta/T_eta__part1.zip) |
| $T_{\eta\mathrm{e}{6}}$.  | [Part 2](./DB/T_eta/T_eta__part2.zip)         |                           |                            |

---

## Evaluation metrics

We  measured the wall-clock running time  of both Schäfer's[^1] and Max-D*s*T[^2] implementations.  Our focus was on the time taken to compute the size of the M*s*C[^3] for each input graph, exluding the time for operations such as reading/writing files,   initialising data structures, and identifying the vertices in M*s*C. Since both algorithms are correct, we did not  evaluate the size of the M*s*C.

---

## Computing environment

We implemented both algorithms in Python[^4] 3.10 and the Python package NetworkX[^5] version 2.8. The input graphs are in GML[^6]. The experiments ran on a 2012 MacBook Pro  with 2.3 GHz Quad-Core Intel Core i7 processor, running a 64 bit macOS Catalina version 10.15.7 with a total memory of 8 GB (1600 MHz DDR3). This computer executed each algorithm implementation on each input graph sequentially without any resource allocation.

---

## Experimental results

**Table 2.** Wall-clock running time of Schäfer's implementation and Max-D*s*T on the six cases of studies. We denote 'timeouts' and 'not applicable' by '---' and 'n/a', respectively.


|           |                                       | Running time                  | in seconds                    |                                                               |
| --------- | ------------------------------------- | ----------------------------- | ----------------------------- | ------------------------------------------------------------- |
| *Row*     | *Graph*                               | $t_{\text{Schäfer}}$          | $t_{\text{DP}s\text{C}}$  | $\frac{t_{\text{Schäfer}}}{t_{\text{DP}s\text{C}}}$       |
| 1         | ${\cal T}_{22-16}$                   | $132.4492$                    | $60.8545$                     | $2.1$                                                         |
| 2         | $T_D,\; k = 4$                        | $109.9832$                    | $1.8577$                      | $59.2$                                                        |
| 3         | $T_D,\; k = 5$                        | $116.5945$                    | $1.5734$                      | $74.1$                                                        |
| 4         | $T_L, \; k = 10$                      | $1.5289$                      | $0.5584$                      | $2.7$                                                         |
| 5         | $T_L, \; k = 100$                     | $12.6688$                     | $4.8969$                      | $2.5$                                                         |
| 6         | $T_L, \; k = 1\,000$                  | $602.9626$                    | $45.2492$                     | $13.3$                                                        |
| 7         | $T_L, \; k = 10\,000$                 | $19\,859.2017$                | $241.7339$                    | $82.1$                                                        |
| 8         | $T_B, \; k = 5$                       | $117.9299$                    | $2.0445$                      | $57.6$                                                        |
| 9         | $T_B, \; k = 10$                      | $121.7708$                    | $1.9870$                      | $61.2$                                                        |
| 10        | $T_B, \; k = 15$                      | $125.8261$                    | $1.9811$                      | $63.5$                                                        |
| 11        | $T_B, \; k = 20$                      | $125.4565$                    | $1.9592$                      | $64.0$                                                        |
| 12        | $T_B, \; k = 25$                      | $126.7537$                    | $1.9809$                      | $63.9$                                                        |
| 13        | $T_B, \; k = 30$                      | $148.4265$                    | $1.9831$                      | $74.8$                                                        |
| 14        | ${\cal T}_{Ph}$                       | $719.4773$                    | $185.4435$                    | $3.8$                                                         |
| 15        | $T_{0.3\mathrm{e}{6}},\; k = 10$      | $1\,022.6843$                 | $9.4978$                      | $107.7$                                                       |
| 16        | $T_{0.3\mathrm{e}{6}},\; k = 100$     | $1\,439.42$                   | $17.3046$                     | $83.1$                                                        |
| 17        | $T_{0.3\mathrm{e}{6}},\; k = 500$     | $5\,989.8246$                 | $74.7689$                     | $80.1$                                                        |
| 18        | $T_{0.5\mathrm{e}{6}},\; k = 10$      | $2\,945.4381$                 | $15.6059$                     | $188.7$                                                       |
| 19        | $T_{0.5\mathrm{e}{6}},\; k = 100$     | $3\,654.6010$                 | $44.1117$                     | $82.8$                                                        |
| 20        | $T_{0.5\mathrm{e}{6}},\; k = 500$     | ---                           | $2\,661.9666$                 | n/a                                                           |
| 21        | $T_{0.75\mathrm{e}{6}},\; k = 10$     | $6\,436.4398$                 | $22.7611$                     | $282.7$                                                       |
| 22        | $T_{0.75\mathrm{e}{6}},\; k = 100$    | $7\,807.3684$                 | $94.7391$                     | $82.4$                                                        |
| 23        | $T_{0.75\mathrm{e}{6}},\; k = 500$    | ---                           | $5\,657.6981$                 | n/a                                                           |
| 24        | $T_{1\mathrm{e}{6}},\; k = 10$        | $11\,529.7250$                | $31.8786$                     | $361.6$                                                       |
| 25        | $T_{1\mathrm{e}{6}},\; k = 100$       | $14\,167.638$                 | $198.9311$                    | $71.2$                                                        |
| 26        | $T_{1\mathrm{e}{6}},\; k = 500$       | ---                           | $11\,422.2738$                | n/a                                                           |

<br>
<br>

**Table 3.** Additional information and raw data. 


|Case of study        | File                                  | Case of study             | File                                  |
| ------------------- | ------------------------------------- | ------------------------- | ------------------------------------- |
| ${\cal T}_{22-16}$ | [T_22_16.tsv](./Results/T_22_16.tsv)  | $T_L$                     | [T_L.tsv](./Results/T_L.tsv)          |
| ${\cal T}_{Ph}$     | [T_Ph.tsv](./Results/T_Ph.tsv)        | $T_B$                     | [T_L.tsv](./Results/T_B.tsv)          |
| $T_D$               | [T_D.tsv](./Results/T_D.tsv)          | $T_{\eta\mathrm{e}{6}}$   | [Random.tsv](./Results/Random.tsv)    |

*Note:* In the `.tsv files`, the column labelled as 'Diameter' represents the value for the integer $s$.

---

[^1]: Schäfer, A.: Exact algorithms for s-club finding and related problems. Ph.D. thesis, Friedrich-Schiller-University Jena (2009).
[^2]: Our dynamic programming algorithm for a maximum distance $s$-club set on trees.
[^3]: A maximum distance $s$-club on trees.
[^4]: Van Rossum, G., Drake, F.L.: Python 3 Reference Manual. CreateSpace, Scotts Valley, CA (2009)
[^5]: Hagberg, A., Swart, P., S Chult, D.: Exploring network structure, dynamics, and function using networkx. Tech. rep., Los Alamos National Lab.(LANL), Los Alamos, NM (United States) (2008)
[^6]: Himsolt, M., 1997. GML: A portable graph file format. Technical report, Universitat Passau.

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
