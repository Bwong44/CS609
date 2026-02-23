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

string = 'ananaasnaaaaaaaaaana'
fining = 'ana'
def readFasta(filename): #Reads the fasta file and returns the sequence as a string
    """Reads a FASTA file and returns the sequence as a string"""
    #TODO: Biopython
    pass

def suffixArray(s): #s object bcomes the sorted list object
    """Builds a suffix array for the given string s"""
    sa = sorted(range(len(s)), key=lambda i: s[i:]) #Takes index of the string at i and sorts it by the suffix
    return list(sa)



def binarySearchLeft(s, sa, find): 
    """Finds the lower bound of the suffix array
    s: input string
    sa: suffix array of the input string
    find: the string to find in the suffix array"""
    left, right = 0, len(sa)
    m = len(find) #Stores the length of find
    while left < right:
        mid = (left + right) // 2
        i = sa[mid] #Converts sa position to index of genome string
        if s[i:i+m] < find: #Compares the suffix to the find string  and moves right since its sorted by alphabetical order
            left = mid + 1 #Everythign to the left of mid is smaller so if it can't find it we must go right
        else:
            right = mid #Could be at mid or to the left so we still include mid
    return left

def binarySearchRight(s, sa, find):
    """Finds the upper bound of the suffix array
    s: input string
    sa: suffix array of the input string
    find: the string to find in the suffix array"""
    left, right = 0, len(sa)
    m = len(find)
    while left < right:
        mid = (left + right) // 2
        i = sa[mid]
        if s[i:i+m] <= find: #If the suffix is smaller than find we can only go right because everything to the left must be smaller (sorted)
            left = mid + 1   #Even if equal we move right because we want to find the upper bound
        else:
            right = mid #We have already went past so we move left
    return left
    
def main(): #main function to run the read search
    """Runs the read search"""
    sa = suffixArray(string)
    left = binarySearchLeft(string, sa, fining)
    right = binarySearchRight(string, sa, fining)
    print(sorted(sa[left:right])) #indexes the suffix array from left to right and sorts it


if __name__ == "__main__":    
    main()
