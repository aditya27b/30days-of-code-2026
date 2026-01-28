 def numberOfSubarrays(self, nums: List[int], k: int) -> int: # type: ignore
    i = 0
    count =  0
    res = 0
    for num in nums:
        if num % 2 == 1:
            k -= 1
            count = 0
        while k == 0:
            k += nums[i] % 2
            i += 1
            count += 1
        res += count
    return res