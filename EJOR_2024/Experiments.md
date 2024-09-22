<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

# **Experiments:** 'A dynamic programming algorithm for a maximum $s$-club set on trees'

- [Home Page](../index.md)
- [Artifact Page](./Artifact.md)
- [Database Page](./Database.md)



**Authors:** [José Alberto Fernández-Zepeda](https://dblp.org/pid/13/7045), [Alejandro Flores-Lamas](https://alexfloreslamas.github.io/), [Matthew Hague](https://www.cs.rhul.ac.uk/home/uxac009/), [Joel Antonio Trejo-Sánchez](https://www.cimat.mx/~joel.trejo).

---

## Description 

Experiments in the article "A dynamic programming algorithm for a maximum $s$-club set on trees" were done using [EJOR\_2024\_Tool (artifact)](./Artifact.md) and the files in this [database](./Database.md).

## Using the EJOR\_2024\_Tool

There's no installation procedure for the EJOR_2024_Tool, please download the project and install the packages listed in the *Software Dependencies* section of the [artifact web page](./Artifact.md).

## Input format

EJOR\_2024\_Tool accepts Graph Modeling Language[^1] (GML) files as input; however, it can be easily modified to support other input files by changing the file `/EJOR_2024_Tool/EJOR_2024_Tool/src/Utils/input_handler.py`.

## Configuration files
EJOR\_2024\_Tool uses [YAML](https://yaml.org/) as a configuration file. Configuration files are stored in `/EJOR_2024_Tool/Settings`.


## Experiments

Follow these steps to evaluate the cases of studies mentioned in **Section 6, Implementation and experiments** of the paper submitted to [European Journal of Operational Research](https://www.sciencedirect.com/journal/european-journal-of-operational-research). 

1. Download the GML files from the [database web page](./Database.md).
2. Unzip the file and place the unziped folder in the location: `/EJOR_2024_Tool/Input`.
3. Open a command-line interpreter and navigate to the 'EJOR_2024_Tool' folder.
    - Type the following command: 

        ```bash
            $ python main.py Settings/<case_of_study_config_file>.yaml
        ```
    - where \<case_of_study_config_file\> takes any of the folowing names: **T_22_16**, **T_B**, **T_D**, **T_eta**, **T_L**, **T_Ph**.


### Notes

#### *On the output files:* 
- Results of the execution of the EJOR\_2024\_Tool will be placed in the folder `/EJOR_2024_Tool/Output/`.

#### *On the execution of $T_{\eta\mathrm{e}{6}}$:*

- Experimentation on this case of study will require several hours; please modify the file `/EJOR_2024_Tool/Settings/T_eta.yaml` or remove graphs as needed from the $T_{\eta\mathrm{e}{6}}$ (T_eta.zip file) case of study to suit your needs; in particular, you will need:

    1. Proceed as in the steps **1** and **2** from the [Experiments](#experiments) section.
    2. In the file `/EJOR_2024_Tool/Settings/T_eta.yaml`
        - On line 36 `diameters: []` add the values of $s$ that you want to test; for example, `diameters: [10, 100, 500]`.
    3. Proceed as in step **3** from the [Experiments](#experiments).

---

[^1]:  Himsolt, M., 1997. GML: A portable graph file format. Technical report, Universitat Passau.

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
