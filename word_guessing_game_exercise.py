secretword = 'difference'
correctletters = []

for char in secretword:
    correctletters.append('_')

secretword_list = list(secretword)
guess = str(input('Enter a guess: '))
if guess.isalpha() == True:
        for position in range(len(secretword_list)):
                if secretword_list[position] == guess:
                #print(position)
                #print(correctword_list[position])
                 correctletters[position] = guess
else:
        print('Guess a letter') 

#print(correctword_list)
print(correctletters)

#    word_guessed = False
#    while word_guessed == False:
#        guess_word = str(input('Enter a guess: '))
#        if guess_word == correct_word:
#            print('Congratulations!  You Win!')
#            word_guessed = True
#        else:
#            print('That is not the word.  Try again.')
    
#else:
#    print('You have used all your guesses.  You lose.')