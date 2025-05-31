from collections import Counter
import sys

def make_kmer_histogram(tsv_file, output_file):
    # Step 1: Read k-mer counts
    freqs = []
    with open(tsv_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                _, count = parts
                freqs.append(int(count))

    # Step 2: Count how many k-mers have each frequency
    freq_counter = Counter(freqs)

    # Step 3: Write histogram to output file
    with open(output_file, 'w') as out:
        for freq in sorted(freq_counter):
            out.write(f"{freq}\t{freq_counter[freq]}\n")

# Example usage:
# make_kmer_histogram("genomeA_longreads_1k_acc90_k21.tsv", "genomeA_longreads_1k_acc90_k21.histo")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_histogram.py <input.tsv> <output.histo>")
        sys.exit(1)
    make_kmer_histogram(sys.argv[1], sys.argv[2])

