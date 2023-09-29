with open('enable2k/WORD.LST', 'r') as file:
    wordlist = file.readlines() 

wordlist = [line.strip() for line in wordlist]
print(wordlist[:20])

vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels)

#words_of_length = [word for word in wordlist if len(word) > 4]
#print(words_of_length[:20])

vowel_words = [word for word in wordlist if any(vowel in word for vowel in vowels)]
print(vowel_words[:20])

e_words = [word for word in vowel_words if 'e' in word]
print(e_words[:10])

print(f'The length of my e_words list is {len(e_words)} words.')

# Writing a function

def filter_words(word_list, central_letter):
    filtered_list = [word for word in word_list if any(vowel in word for vowel in vowels) and central_letter in word]
    return filtered_list
    
central_letter = input("Please enter the central letter: ")

filtered_results = filter_words(wordlist, central_letter)

print(filtered_results[:10])