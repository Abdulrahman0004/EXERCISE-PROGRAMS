str1 = 'swwiiss'
freq = {}

for i in str1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key in freq:
    if freq[key] <= 1:
        print(key)
        break
else:
    print(-1)
