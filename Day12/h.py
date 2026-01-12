def searchRange(self, nums: List[int], target: int) -> List[int]: # type: ignore
        ret =[-1,-1]
        for i in nums:
            if i == target and ret == [-1,-1]:
                ret[0] = (nums.index(i))
                ret[1] = (nums.index(i))
            elif i == target:
                ret[1] += 1
            elif i > target:
                if ret is None: return [-1,-1]
                else: return ret
        return ret