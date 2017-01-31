'''
Cracking the coding interview
Question 1-4
p. 91
'''

def palPer(st):
    st = st.lower()
    st = sorted(st)
    oddFound = False
    last = st[0]
    i = 0
    while i + 1 < len(st):
        if st[i] == st[i+1]: i += 2
        elif not oddFound:
            i += 1
            oddFound = True
        else: return False
    return True

print palPer('TactCoa')
print palPer('TacoCat')
print palPer('tactcoapapa')