def trap(height):
    total = 0
    if not height:
        return total
    nums = len(height)
    leftLev, rightLev = [0, ] * nums, [0, ] * nums
    leftLev[0] = height[0]
    rightLev[-1] = height[-1]
    i, j = 1, -2
    while i < nums:
        leftLev[i] = max(leftLev[i - 1], height[i])
        rightLev[j] = max(rightLev[j + 1], height[j])
        i += 1
        j -= 1
    for k in range(nums):
        total += min(leftLev[k], rightLev[k]) - height[k]
    return total


height
