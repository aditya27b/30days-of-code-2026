class Solution:
    def intersection(self,a, b):
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        res = []
        
        while i < n and j < m:
            if i > 0 and a[i] == a[i-1]:
                i += 1
                continue
            
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                res.append(a[i])
                i += 1
                j += 1
                
        return res