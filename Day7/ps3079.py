class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int: # type: ignore
        #converting the numbers first to a new list
        nl = []
        for num in nums:
            x = max(list(str(num)))
            nl.append(int(x*len(str(num))))
        return sum(nl)