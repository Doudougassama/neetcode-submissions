class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vu = set()

        for i in nums:
            if i in vu:
                return True
            else:
                vu.add(i)
        return False