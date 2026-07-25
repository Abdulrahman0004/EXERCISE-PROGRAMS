str1 = "Hello wOrld"
vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
vowel_count = 0
consonant_count = 0

for i in str1:
    if i in vowels:
        vowel_count += 1
    elif i.isalpha():
        consonant_count += 1

print("Vowels = ", vowel_count)
print("Consonants = ", consonant_count)