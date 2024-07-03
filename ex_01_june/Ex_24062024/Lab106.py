letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# Filter the vowels
# a,e,i,o,u

def filter_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

# result = filter_vowel('a')
# print(result)  # True

filtered_words = filter(filter_vowel, letters)
print(list(filtered_words))