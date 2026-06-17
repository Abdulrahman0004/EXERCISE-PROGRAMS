def smallLargeSorted(arr, target):
    small = 0
    large = 0
    for i in arr:
        if i <= target:
            small = small + 1
        if i >= target:
            large = large + 1
    return [small, large]

arr = [1, 2, 8, 12, 12, 12, 19]
print(smallLargeSorted(arr, 12))
