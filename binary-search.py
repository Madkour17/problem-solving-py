def search(nums, target) -> int:

    min = 0
    max = len(nums)-1

    while min <= max:
        mid = min + max
        guess = nums[mid]
        if guess == target:
            return mid
        if guess < target:
            min = mid+1
        if guess > target:
            max = mid-1
    return -1
