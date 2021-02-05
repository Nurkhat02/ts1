class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        ans =0
        ans1=0
        ans2=1
        for i in range(len(s)):
            ans1 +=int(s[i])
            ans2 *=int(s[i])
        ans = ans2 - ans1
        return ans