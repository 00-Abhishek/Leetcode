from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MODI= 10**9 +7
        dp={(0,0):1}

        for num in nums:
            new_dp=dp.copy()
            for (gcd1,gcd2), count in dp.items():
                # Put num in seq1
                new_gcd1 = gcd(gcd1, num)

                new_dp[(new_gcd1, gcd2)] = (
                    new_dp.get((new_gcd1, gcd2), 0) + count
                ) % MODI

                # Put num in seq2
                new_gcd2 = gcd(gcd2, num)

                new_dp[(gcd1, new_gcd2)] = (
                    new_dp.get((gcd1, new_gcd2), 0) + count
                ) % MODI

            dp = new_dp

        answer = 0

        for (gcd1, gcd2), count in dp.items():
            if gcd1 == gcd2 and gcd1 != 0:
                answer = (answer + count) % MODI

        return answer
