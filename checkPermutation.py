'''
Cracking the coding interview
Question 1-2
p. 90
'''

def checkPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

print checkPermutation('ali', 'ali')
print checkPermutation('ali', 'lia')
print checkPermutation('ali', 'lik')
