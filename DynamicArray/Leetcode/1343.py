class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        currSum = sum(arr[:k-1])
        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1]
            if currSum / k >= threshold:
                count += 1
            currSum -= arr[L]
        return count