#Goal 1: ⦁	Convert the provided DNA sequence into a lowercase list of characters.
def convert_dna_to_lowercase_list(dna):
    return list(dna.lower())
# Input
dna = input("Enter a DNA sequence: ")
# Output
print(convert_dna_to_lowercase_list(dna))


# Goal 2: ⦁	Capitalize the exon regions given as start/end index tuples.
def capitalize_exons(dna, exons): # exons is a list of (start, end) tuples
    dna_list = list(dna)    # Convert string to list for mutability
    for start, end in exons:
        for i in range(start, end):
            if 0 <= i < len(dna_list): # Ensure index is within bounds
                dna_list[i] = dna_list[i].upper() # Capitalize exon region
    return ''.join(dna_list) # Convert list back to string
# Input
dna = input("Enter a DNA sequence: ")
exons_input = input("Enter exon regions as start,end pairs separated by spaces (e.g., '2,5 10,12'): ")
exons = [tuple(map(int, pair.split(','))) for pair in exons_input.split()] # Convert input to list of tuples
# Output 
print(capitalize_exons(dna, exons))


#Goal 3: Count how many times each nucleotide (A,T,G,C) occurs in the DNA string
def count_nucleotides(dna): # Returns a dictionary with counts of A, T, G, C
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0} # Initialize counts
    for nucleotide in dna.upper():
        if nucleotide in counts:
            counts[nucleotide] += 1 # Increment count
    return counts
# Input
dna = input("Enter a DNA sequence: ")
# Output
print(count_nucleotides(dna))


#Goal 4: Reverse a DNA sequence and print it.
def reverse_dna(dna): 
    return dna[::-1] # Reverse the string using slicing
# Input
dna = input("Enter a DNA sequence: ")
# Output
print(reverse_dna(dna))

