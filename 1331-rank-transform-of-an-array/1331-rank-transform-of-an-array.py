class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Shift all values to make them non-negative
        minimum = min(arr)
        nums = [num - minimum for num in arr]

        # Radix sort
        sorted_nums = nums[:]
        exp = 1
        maximum = max(sorted_nums)

        while maximum // exp > 0:
            count = [0] * 10
            output = [0] * len(sorted_nums)

            # Count digits
            for num in sorted_nums:
                digit = (num // exp) % 10
                count[digit] += 1

            # Convert counts into positions
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the sorted array
            for i in range(len(sorted_nums) - 1, -1, -1):
                digit = (sorted_nums[i] // exp) % 10
                output[count[digit] - 1] = sorted_nums[i]
                count[digit] -= 1

            sorted_nums = output
            exp *= 10

        # Assign ranks to unique values
        rank = {}
        current_rank = 0
        previous = None

        for num in sorted_nums:
            if previous is None or num != previous:
                current_rank += 1
                rank[num] = current_rank
                previous = num

        # Replace each value with its rank
        return [rank[num] for num in nums]