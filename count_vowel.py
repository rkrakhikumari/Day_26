def count_vowel(str):
    vowel = "aeiouAEIOU"
    return sum(1 for char in str if char in vowel)

result = count_vowel("satyam")
print(result)


    