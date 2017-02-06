'''
Towers of Hanoi
YET TO BE COMPLETED
'''

def hanoi(n):
    origin = range(n+1)
    destination = []
    buffer = []
    return moveDisks(n, origin, destination, buffer)

def moveDisks(n, origin, destination, buffer):

# Testing
