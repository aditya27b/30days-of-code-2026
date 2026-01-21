def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: # type: ignore
        d = {}
        s = []
        for x in nums2:
            while s and x > s[-1]:
                d[s.pop()] = x
            s.append(x)
        return [d.get(x, -1) for x in nums1]