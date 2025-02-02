"""
219
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
    
def passOrNot(arr, k, threshold):
    count = 0
    for L in range(len(arr)):
        avg = arr[L]
        for R in range(L+1, min(len(arr), L+k)):
            avg += arr[R]
        if avg / k >= threshold:
            count += 1
    return count


arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

print(passOrNot(arr, k, threshold))