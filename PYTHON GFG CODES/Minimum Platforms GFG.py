arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

arr.sort()   # arr = [900, 940, 950, 1100, 1500, 1800]
dep.sort()   # dep = [910, 1120, 1130, 1200, 1900, 2000]

i = 0
j = 0
platform = 0            #2
max_platform = 0        #3

while i <= len(arr)-1 and j <= len(arr)-1:
    if arr[i] <= dep[j]:
        platform += 1
        if platform > max_platform: 
            max_platform = platform
        i += 1
    else:
        platform -= 1
        j+= 1

print(max_platform)