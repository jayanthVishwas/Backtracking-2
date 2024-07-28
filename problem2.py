class Solution:
    def checkPali(self, s):
        l,r = 0, len(s)-1
        while(l<=r):
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        #method1: partition string using recursion and check if the partitioned string is a palindrome

        res = []
        
        def recursion(start, subset):
            if start==len(s):
                res.append(subset.copy())
                return
            
            for i in range(start, len(s)):
                if self.checkPali(s[start:i+1]):
                    subset.append(s[start:i+1])
                    recursion(i+1, subset)
                    subset.pop()

        recursion(0, [])
        return res

        # time - O(n*2**n)
        # space - O(n)


        