#!/usr/bin/env python3

import random
from Bio import SeqIO
import argparse
import os

def introduce_errors(seq, error_rate):
    bases = ['A', 'C', 'G', 'T']
    seq = list(seq)
    for i in range(len(seq)):
        if random.random() < error_rate:
            original = seq[i]
            seq[i] = random.choice([b for b in bases if b != original])
    return ''.join(seq)

def simulate_reads(fasta_path, out_prefix, read_length, num_reads, error_rates):
    genome = ""
    for record in SeqIO.parse(fasta_path, "fasta"):
        genome += str(record.seq)

    genome_length = len(genome)
    os.makedirs(os.path.dirname(out_prefix), exist_ok=True)

    for acc, err_rate in error_rates.items():
        out_path = f"{out_prefix}_{acc}.fq"
        with open(out_path, "w") as f:
            for i in range(num_reads):
                start = random.randint(0, genome_length - read_length)
                read = genome[start:start+read_length]
                read_with_errors = introduce_errors(read, err_rate)
                quality = "I" * read_length  # Dummy high quality
                f.write(f"@read_{i}_{acc}\n{read_with_errors}\n+\n{quality}\n")
        print(f"Simulated {num_reads} reads with {acc} accuracy -> {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate sequencing reads with multiple error rates")
    parser.add_argument("fasta", help="Input genome FASTA file")
    parser.add_argument("out_prefix", help="Output file prefix (e.g., simulated_reads/genomeA_short)")
    parser.add_argument("--length", type=int, default=180, help="Read length (default: 180)")
    parser.add_argument("--num", type=int, default=1000, help="Number of reads (default: 1000)")

    args = parser.parse_args()

    error_profiles = {
        "perfect": 0.00,
        "acc90": 0.10
    }

    simulate_reads(args.fasta, args.out_prefix, args.length, args.num, error_profiles)

