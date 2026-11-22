from Bio.Seq import Seq

dna = Seq("ATGCGTACGTTA")

print("DNA sequence:", dna)
print("Sequence length:", len(dna))
print("Complement:", dna.complement())
print("Reverse complement:", dna.reverse_complement())
print("Protein sequence:", dna.translate())
print('GC_conent:' (dna.count('G') + (dna.count('C')/len(dna)*100)

