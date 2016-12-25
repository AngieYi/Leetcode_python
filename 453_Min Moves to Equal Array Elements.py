class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # think in oppisite way, times of incrementing n - 1 elements by 1 is equal to times of decrementing 1 elements by 1.
        # consider the original state and final state, the difference of sum divide by step is the frequenct times.
        step = 1
        return (sum(nums) - len(nums)* min(nums)) / step