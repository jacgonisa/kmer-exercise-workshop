#!/usr/bin/env python3
import sys
from collections import defaultdict

def read_fastq(file_path):
    with open(file_path, 'r') as f:
        while True:
            try:
                _ = next(f)  # header
                seq = next(f).strip()
                _ = next(f)  # plus
                _ = next(f)  # quality
                yield seq
            except StopIteration:
                break

def count_kmers(file_path, k):
    kmers = defaultdict(int)
    for seq in read_fastq(file_path):
        for i in range(len(seq) - k + 1):
            mer = seq[i:i+k]
            kmers[mer] += 1
    return kmers

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python kmer_counter.py <input.fastq> <k>")
        sys.exit(1)

    input_file = sys.argv[1]
    k = int(sys.argv[2])
    kmers = count_kmers(input_file, k)

    for mer in sorted(kmers):
        print(f"{mer}\t{kmers[mer]}")

