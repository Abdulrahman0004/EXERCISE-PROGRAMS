def FindMedian():
    length = len(merged_list)
    middle = length // 2
    if length % 2 == 0:
        return (merged_list[middle - 1] + merged_list[middle]) / 2
    else:
        return merged_list[middle]
nums1 = [1, 3]
nums2 = [2, 4]
merged_list = nums1 + nums2
merged_list.sort()
print(FindMedian())