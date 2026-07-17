class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # Frequency of each number
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        # divisible_count[d] = numbers divisible by d
        divisible_count = [0] * (max_val + 1)

        for d in range(1, max_val + 1):
            for multiple in range(d, max_val + 1, d):
                divisible_count[d] += freq[multiple]

        # exact_pairs[d] = number of pairs whose gcd is exactly d
        exact_pairs = [0] * (max_val + 1)

        # Inclusion-Exclusion
        for d in range(max_val, 0, -1):
            cnt = divisible_count[d]
            pairs = cnt * (cnt - 1) // 2

            multiple = d * 2
            while multiple <= max_val:
                pairs -= exact_pairs[multiple]
                multiple += d

            exact_pairs[d] = pairs

        # Prefix sums of pair counts
        prefix = []
        running = 0

        for gcd_value in range(1, max_val + 1):
            running += exact_pairs[gcd_value]
            prefix.append(running)

        # Answer queries
        answer = []
        for q in queries:
            # first prefix > q
            idx = bisect_right(prefix, q)
            answer.append(idx + 1)

        return answer