class Solution(object):
    def addBinary(self, a, b):
        x=bin(int(a,2)+int(b,2))

        return x[2:]
 
        