def minProductSubarray(arr):
    if len(arr) == 0:
        return None

    max_product = arr[0]
    min_product = arr[0]
    answer = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        answer = min(answer, min_product)
    return answer


arr = [2, 3, -2, 4]
print(minProductSubarray(arr))