"""
Assignment 2 - Suffix Array Read Search
Author: Brandon Wong
Date: 2026-02-22

Inputs: fasta file containing ref genome, fasta file containing search read
Output: List of postions where the read is found

1. Build a suffix array
2. Use binary search to find upper and lower blocks of the suffix array since it will be sorted
3. Return the positions of the suffix array that match the read
"""

# Source - https://stackoverflow.com/q/54642311
# Posted by Ayushman Patel
# Retrieved 2026-02-22, License - CC BY-SA 4.0

# Source - https://stackoverflow.com/a/54642406
# Posted by sam46
# Retrieved 2026-02-22, License - CC BY-SA 4.0

s = 'banana'
find = 'ana'
def readFasta(filename): #Reads the fasta file and returns the sequence as a string
    """Reads a FASTA file and returns the sequence as a string."""
    #TODO: Biopython
    pass

def suffixArray(s): #s object bcomes the sorted list object
    """Builds a suffix array for the given string s."""
    sa = sorted(range(len(s)), key=lambda i: s[i:])
    return list(sa)



def binarySearch(s, find):
    sa = suffixArray(s) #Calls suffixArray function
    print(sa[0]) #Prints the sorted list object
    return sa #Returns the second element of the sorted list object

    
def main(): #main function to run the read search
    """Runs the read search."""
    binarySearch(s, find)


if __name__ == "__main__":    
    main()
