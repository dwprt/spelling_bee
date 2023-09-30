with open('enable2k/WORD.LST', 'r') as file:
    wordlist = file.readlines() 

wordlist = [line.strip() for line in wordlist]

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_words = [word for word in wordlist if any(vowel in word for vowel in vowels)]
length_words = [word for word in vowel_words if len(word) >= 4 and len(word) <= 8]

#todays_letters = set(['n', 'x', 'd', 'g', 'i', 'e'])

#print(f'The length of my e_words list is {len(e_words)} words.')

# Writing a function

#def filter_words(word_list, central_letter):
#    filtered_list = [word for word in word_list if any(letter in word for letter in todays_letters) and central_letter in word]
#    return filtered_list

def filter_words(word_list, central_letter):
    filtered_list = [word for word in word_list if central_letter in word and any(letter in word for letter in vowels)]
    return filtered_list
   
central_letter = input("Please enter the central letter: ")

filtered_results = filter_words(wordlist, central_letter)

print(filtered_results[:10])

lambda_results = filter(lambda word: any(vowel in word for vowel in vowels) and central_letter in word, wordlist)

lambda_results_list = list(lambda_results)

print(lambda_results_list[:10])

print(filtered_results == lambda_results_list)

