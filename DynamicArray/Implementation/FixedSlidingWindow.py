"""
    Fixed window solution, in place
    O(kn)

"""
def fixedSlidingWindow(nums, k):
    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False

"""
    Fixed window solution, extra memory uses set
    O(n)
"""

def fixedSlidingWindowSetSolution(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False

