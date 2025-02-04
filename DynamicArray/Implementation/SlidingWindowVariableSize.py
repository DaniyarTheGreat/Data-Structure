def slidingWindowVariableSize(nums: list[int]) -> int:
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[R] != nums[L]:
            L = R
        length = max(length, R - L + 1)
    return length

def shortestSubarray(nums: list[int], target: int) -> int:
    length = len(nums) + 1
    total = 0
    L = 0
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(length, R - L + 1)
            total -= nums[L]
            L += 1
    return 0 if length == len(nums) + 1 else length
