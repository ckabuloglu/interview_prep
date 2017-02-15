'''
Group Anagrams
Given a list of strings (words), group them into their anagrams
'''
from collections import defaultdict

def groupAnagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join([s for s in sorted(word)])
        groups[key].append(word)
    return groups.values()

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(words)