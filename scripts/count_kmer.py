import sys

sequence = "CATCGATGCTCGATACGGTCGATGGGTGTGTGTCATCAT"

#Set k
k=21

def make_kmers(seq):
	#Take sequence and turn it into k-mers 
	#Kmers are saved as the key in a dictionary 
	#The values in the dictionary are the index of the kmer
	#Quickly calculate the count for each kmer based on the length of the index list
	kmers = {}
	for i in range(0,len(seq)-k+1):
		this_mer = seq[i:i+k]
		if this_mer in kmers.keys():
			kmers[this_mer].append(i)
		else:
			kmers[this_mer] = [i]
		kmers[seq[i:i+k]]
	return kmers

kmers = make_kmers(sequence)
for i in kmers.keys():
	print(i + ": " + str(kmers[i]))
