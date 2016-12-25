'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

https://leetcode.com/problems/zigzag-conversion/
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = { x: "" for x in range(numRows) }
        
        index, flag = 0, True
        
        for c in s:
            result[index] += c
            if flag:
                if index == numRows - 1:
                    index -= 1 if index > 0 else 0
                    flag = False
                else:
                    index += 1
            else:
                if index == 0:
                    index += 1 if index < numRows - 1 else numRows - 1
                    flag = True
                else:
                    index -= 1
        
        ans = ""
        for i in range(numRows):
            ans += result[i]
        return ans