class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max =0
        sum = 0
        for i in range(len(gain)):
            sum +=gain[i]
            if sum>max:
                max = sum
        return max