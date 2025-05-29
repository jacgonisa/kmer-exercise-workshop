# kmer-exercise-workshop
Anexercise for the K-mer Workshop for Biodiversity Genomics (Wellcome Genome Campus, Hinxton)


This short, hands-on exercise is designed to explore how **k-mers** reflect genome properties like **ploidy**, **heterozygosity**, and **repetitiveness**, using simulated reads and k-mer counting tools. The workshop is structured into three phases and should take ~75 minutes in total.

---

## 🗂️ Overview

1. [Prepare data (10 min)](#1-prepare-the-data)
2. [Simulate reads (20 min)](#2-simulate-the-reads)
3. [Count k-mers (45 min)](#3-count-k-mers)
4. 


---

## 1. 🧬 Prepare the Data


We’ve included two **mystery genomes** in the `data/` folder:

- **Genome A** → `data/genomeA.fa`
- **Genome B** → `data/genomeB.fa`

Each genome represents different biological characteristics, such as:

- **Haploidy vs. diploidy**
- **High vs. low heterozygosity**
- **Different levels of repetitiveness**

🔍 **Your task** is to uncover their secrets through k-mer analysis!

---

## 2. 🧪 Simulate the Reads

> 🔄 *This part will be done in groups.*

You will simulate short and long reads from the mystery genomes to reflect different sequencing technologies and error profiles.

### 🔧 Read Types
- **Short reads** (~180 bp) — mimicking Illumina-style reads
- **Long reads** (~10,000 bp) — mimicking Oxford Nanopore or PacBio

### 🛠 Tools & Code
- We’ll use **custom scripts** or read simulators.
- Pre-simulated reads will also be available in the `simulated_reads/` folder.



### 🔧 Requirements

Install dependencies using Python (you need [Biopython](https://biopython.org/)):

```bash
pip install biopython
```


This is how you can run the read simulation:

```bash
python scripts/simulate_reads.py <input_fasta> <output_prefix> --length <read_length> --num <num_reads>
```


We ran something like...
```bash
python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads/genomeA_longreads_1k --length 10000 --num 1000

python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads/genomeA_shortreads_1k --length 180 --num 1000

python scripts/simulate_reads.py data/genomeB.fasta results/simulated_reads/genomeB_longreads_1k --length 10000 --num 1000

python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads/genomeA_shortreads_1k --length 180 --num 1000

```

But it is better to simulate much more reads!
---

## 3. 🔢 Count K-mers



In this step, you'll count k-mers in your simulated reads. This helps reveal patterns like heterozygosity, repetitive content, and ploidy in genomes.

You can analyze the read data with different k-mer lengths:
`k = 11`, `21`, and `101`.

We can write a Python script that slides a window of length `k` across each read to build a k-mer frequency table.




### Tasks:
- Use a provided script to **count k-mers**.
- Create **k-mer histograms** for each genome.
- Analyze patterns using [**GenomeScope**](https://github.com/schatzlab/genomescope) or your own intuition.

💬 **Katie**: Please confirm the k-mer counting tool or function (e.g., Jellyfish, KMC3, custom code).

---

## 🧠 What You'll Learn

By the end of this exercise, you’ll be able to:
- Simulate sequencing reads from genomic data.
- Count and interpret k-mers using various `k` values.
- Use k-mer histograms to infer genome features such as ploidy and repeat structure.
- Work as a group to **uncover the identity** of Genome A and Genome B.

---

## 📁 Repository Layout


