'''
Cracking the coding interview
8.9
'''

def paranthesis(pair):
    return paran([], '', pair, pair)

def paran(arr, st, left, right):
    if left < 0 or left > right: return
    elif left == 0 and right == 0: arr.append(st)
    else:
        paran(arr, st+'(', left - 1, right)
        paran(arr, st+')', left, right - 1)
    return arr

# Testing
print paranthesis(1)
print paranthesis(2)
print paranthesis(3)
print paranthesis(5)
