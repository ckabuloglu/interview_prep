'''
Cracking the coding interview
8.4
p. 135

Return all subsets of a given set.
'''

# Define the function
def findSubsets(arr):
    subsets = [[]]
    for n in arr:
        temp = list(subsets)
        for subset in temp:
            newSubset = list(subset)
            newSubset.append(n)
            subsets.append(newSubset)
    return subsets

print findSubsets([1])
print findSubsets([1, 2])
print findSubsets([1, 2, 3])
print findSubsets(range(20))