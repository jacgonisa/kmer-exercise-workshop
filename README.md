# kmer-exercise-workshop
Anexercise for the K-mer Workshop for Biodiversity Genomics (Wellcome Genome Campus, Hinxton)


This short, hands-on exercise is designed to explore how **k-mers** reflect genome properties like **ploidy**, **heterozygosity**, and **repetitiveness**, using simulated reads and k-mer counting tools. The workshop is structured into three phases and should take ~75 minutes in total.

---

## 🗂️ Overview

1. [Prepare data (10 min)](#1--prepare-the-data)
2. [Simulate reads (20 min)](#2--simulate-the-reads)
3. [Count k-mers (45 min)](#3--count-k-mers)
4. [Discussion (35 min)](#4--discussion)


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

##Illumina
python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads_coveragex10/genomeA_illumina --length 180 --num 2595000 --error 0.001

##ONT

python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads_coveragex10/genomeA_ONT --length 20000 --num 23000 --error 0.1

##PacBio
python scripts/simulate_reads.py data/genomeA.fasta results/simulated_reads_coveragex10/genomeA_pacbio --length 10000 --num 47000 --error 0.005






# Genome B

##Illumina
python scripts/simulate_reads.py data/genomeB.fasta results/simulated_reads_coveragex10/genomeB_illumina --length 180 --num 2595000 --error 0.001

##ont
python scripts/simulate_reads.py data/genomeB.fasta results/simulated_reads_coveragex10/genomeB_ONT --length 20000 --num 23000 --error 0.1

##PacBio

python scripts/simulate_reads.py data/genomeB.fasta results/simulated_reads_coveragex10/genomeA_pacbio --length 10000 --num 47000 --error 0.005







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



You can automatize better with

```
for file in results/simulated_reads/*.fq; do for k in 11 21 101; do python scripts/kmer_counter_from_fastq.py "$file" "$k" > results/kmer_counts/$(basename "${file%.fq}")_k${k}.tsv; done; done
```
This can take quite memory space!






### 3.1 Make histogram for Genomescope

Once you've counted k-mers (from .tsv files like genomeA_longreads_k21.tsv), you can summarize how often each count appears by converting it into a histogram file. This will allow you to analyze the frequency distribution of k-mers.

```bash
python scripts/kmercount_to_histogram.py <input_kmer_counts.tsv> <output_histogram.histo>

```

For instance,

```bash
python scripts/kmercount_to_histogram.py results/kmer_counts/genomeA_longreads_1k_acc90_k21.tsv results/hi
stograms/genomeA_longreads_1k_acc90_k21.histo
```

We can automatize with

```bash
for f in results/kmer_counts/*.tsv; do
  out="results/histograms/$(basename "$f" .tsv).histo"
  python scripts/kmercount_to_histogram.py "$f" "$out"
done
```


---


## 4. 🧠 Discussion

Now that you have simulated reads and counted k-mers across multiple genome types and sequencing conditions, take some time to reflect and discuss the following:

### 🔬 Biological Interpretation

- What differences do you observe in k-mer spectra between **Genome A** and **Genome B**?
- Can you infer **repetitive content** from the k-mer profiles?
- Do the k-mer distributions reveal anything about **genome size** or **ploidy**?

### 🧪 Simulation Parameters

- How do **read length** and **error rate** affect the k-mer spectra?
- Compare perfect reads (100% accuracy) with those containing 90% accuracy.
  - What kinds of artifacts or noise do you observe in the spectra?

### 🛠️ Technical Questions

- What is the impact of the **k-mer size** (for instance, `k=11` vs `k=101`) on the spectrum?
- Which k-mer size is best for identifying low-copy vs. high-copy sequences?
- How do very short vs. very long k-mers behave in terms of uniqueness and information content?

### 💭 Open Questions

- Can you think of how this type of analysis could be useful for:
  - **Detecting contamination?**
  - **Estimating genome size without assembly?**
  - **Comparing species in biodiversity genomics?**




### What You Learned

By the end of this exercise, you’ll be able to:
- Simulate sequencing reads from genomic data.
- Count and interpret k-mers using various `k` values.
- Use k-mer histograms to infer genome features such as ploidy and repeat structure.
- Work as a group to **uncover the identity** of Genome A and Genome B.

---



