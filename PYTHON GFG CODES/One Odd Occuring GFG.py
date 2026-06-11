from collections import Counter

def odd_occurance(arr):
    count_arr = Counter(arr)
    for i in count_arr:
        if count_arr[i] % 2 == 1:
            return i
        
arr = [1, 2, 3, 3, 1, 4, 4]
print(odd_occurance(arr))