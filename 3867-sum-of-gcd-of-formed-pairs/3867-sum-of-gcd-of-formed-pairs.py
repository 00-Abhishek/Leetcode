class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix=[]
        mx=0

        for num in nums:
            mx=max(mx,num)
            prefix.append(gcd(num,mx))
        prefix.sort()

        left,right=0,len(prefix)-1
        ans=0

        while left<right:
            ans+=gcd(prefix[left],prefix[right])
            left+=1
            right-=1
        return ans


        