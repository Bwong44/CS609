# Source - https://stackoverflow.com/q/54642311
# Posted by Ayushman Patel
# Retrieved 2026-02-22, License - CC BY-SA 4.0

# Source - https://stackoverflow.com/a/54642406
# Posted by sam46
# Retrieved 2026-02-22, License - CC BY-SA 4.0

s = 'banana'
find = 'ana'

def suffixArray(s): #s object bcomes the sorted list object
    sa = sorted(range(len(s)), key=lambda i: s[i:])
    return list(sa)



def binarySearch(s, find):
    sa = suffixArray(s) #Calls suffixArray function
    begin_index = 0
    end_index = len(sa) - 1
    while begin_index <= end_index:
        midpoint = (begin_index + end_index) // 2
        midpoint_value = sa[midpoint]
        if midpoint_value == find:
            return midpoint
        elif find < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

    
def main(): #main function to run the read search
    search = suffixArray(s)
    print(binarySearch(s, 5))


if __name__ == "__main__":    
    main()
