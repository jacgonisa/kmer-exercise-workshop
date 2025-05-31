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

| Type         | Length (bp) | Technology Mimicked          |
|--------------|-------------|-------------------------------|
| Short reads  | ~180        | Illumina-style                |
| Long reads   | ~10,000     | Oxford Nanopore / PacBio      |



### 🛠 Tools & Code
- We’ll use **custom scripts** or read simulators.
- Pre-simulated reads will also be available in the `results/simulated_reads/` folder.



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
# Genome A
python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads/genomeA_longreads --length 10000 --num 47000
python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads/genomeA_shortreads --length 180 --num 2595000

# Genome B
python scripts/simulate_reads.py data/genomeB.fasta results/simulated_reads/genomeB_longreads --length 10000 --num 47000
python scripts/simulate_reads.py data/genomeB.fasta results/simulated_reads/genomeB_shortreads --length 180 --num 2595000

```


> 💬 Reflect & Discuss
> **What is the actual sequencing coverage you're achieving with these simulations?**  
> _Hint: Total number of bases simulated ÷ genome size._


---

## 3. 🔢 Count K-mers

```bash
mkdir results/kmer_counts
```


In this step, you'll count k-mers in your simulated reads. This helps reveal patterns like heterozygosity, repetitive content, and ploidy in genomes.

You can analyze the read data with different k-mer lengths:
`k = 11`, `21`, and `101`.

We can write a Python script that slides a window of length `k` across each read to build a k-mer frequency table.

Then, we can run something like

```bash

python scripts/kmer_counter_from_fastq.py results/simulated_reads/genomeA_short_perfect.fq 21 > results/kmer_counts/genomeA_short_perfect_k21.tsv

```
which is a suitable output for  [**GenomeScope**](https://github.com/schatzlab/genomescope).



You can automatize better with

```
for file in results/simulated_reads/*.fq; do for k in 11 21 101; do python scripts/kmer_counter_from_fastq.py "$file" "$k" > results/kmer_counts/$(basename "${file%.fq}")_k${k}.tsv; done; done
```
This can take quite memory space!



---


## 4. 🧠 Discussion

Now that you have simulated reads and counted k-mers across multiple genome types and sequencing conditions, take some time to reflect and discuss the following:

### 🔬 Biological Interpretation

- What differences do you observe in k-mer spectra between **Genome A** and **Genome B**?
- Can you infer **heterozygosity** or **repetitive content** from the k-mer profiles?
- Do the k-mer distributions reveal anything about **genome size** or **ploidy**?

### 🧪 Simulation Parameters

- How do **read length** and **error rate** affect the k-mer spectra?
- Compare perfect reads (100% accuracy) with those containing 90% and 99% sequence identity.
  - What kinds of artifacts or noise do you observe in the spectra?
  - Which error rate most resembles real sequencing data?

### 🛠️ Technical Questions

- What is the impact of the **k-mer size** (`k=11` vs `k=101`) on the spectrum?
- Which k-mer size is best for identifying low-copy vs. high-copy sequences?
- How do very short vs. very long k-mers behave in terms of uniqueness and information content?

### 💭 Open Questions

- Can you think of how this type of analysis could be useful for:
  - **Detecting contamination?**
  - **Estimating genome size without assembly?**
  - **Comparing species in biodiversity genomics?**
- How might this approach differ when applied to:
  - **Metagenomes?**
  - **Polyploid or hybrid genomes?**
  - **Ancient DNA or degraded samples?**



### What You Learned

By the end of this exercise, you’ll be able to:
- Simulate sequencing reads from genomic data.
- Count and interpret k-mers using various `k` values.
- Use k-mer histograms to infer genome features such as ploidy and repeat structure.
- Work as a group to **uncover the identity** of Genome A and Genome B.

---



