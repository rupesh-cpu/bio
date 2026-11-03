
# Input DNA sequence
dna = input("Enter a DNA sequence: ").upper()

print("\nDNA Sequence:", dna)

# 1. Length of DNA
print("Length of sequence:", len(dna))

# 2. Motif searching
motif = input("\nEnter a motif to search: ").upper()

positions = []

for i in range(len(dna) - len(motif) + 1):
    if dna[i:i+len(motif)] == motif:
        positions.append(i)

print("Motif positions:", positions if positions else "Not found")

# 3. GC Content
g = dna.count("G")
c = dna.count("C")

gc_content = ((g + c) / len(dna)) * 100

print(f"GC Content: {gc_content:.2f}%")

# 4. Reverse Complement
complement = ""

for base in dna:
    if base == "A":
        complement = "T" + complement
    elif base == "T":
        complement = "A" + complement
    elif base == "G":
        complement = "C" + complement
    elif base == "C":
        complement = "G" + complement

print("Reverse Complement:", complement)

# 5. Start Codon
start = dna.find("ATG")

if start != -1:
    print("Start codon found at position:", start)
else:
    print("Start codon not found")

# 6. Stop Codons
for stop in ["TAA", "TAG", "TGA"]:
    pos = dna.find(stop)

    if pos != -1:
        print(f"Stop codon {stop} found at position: {pos}")
    else:
        print(f"Stop codon {stop} not found")

