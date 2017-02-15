'''
Intervals
Given intervals in tuples, return the merged list of intervals
'''

def mergeIntervals(intervals):
    ans = []
    intervals.sort()
    print intervals

    for interval in intervals:
        if not ans: ans.append(interval)
        elif ans[-1][1] < interval[0]: ans.append(interval) 
        elif ans[-1][1] < interval[1]:
            temp = ans.pop()
            ans.append((temp[0], interval[1]))

    return ans

intervals = [(4,5), (1,3), (5,9), (6,7), (1,2), (2,14)]
print mergeIntervals(intervals)

    


