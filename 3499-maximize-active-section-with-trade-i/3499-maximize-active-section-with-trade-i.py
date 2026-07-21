class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')

        t = "1" + s + "1"

        # Run-length encoding
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best_gain = 0

        # Check every removable 1-block
        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == '1'
                and runs[i - 1][0] == '0'
                and runs[i + 1][0] == '0'
            ):
                gain = runs[i - 1][1] + runs[i + 1][1]
                best_gain = max(best_gain, gain)

        return initial_ones + best_gain