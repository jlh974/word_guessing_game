correct_word = 'difference'
is_guessed = False
while is_guessed == False:
    guess_word = str(input('Enter a guess: '))
    if guess_word == correct_word:
        print('Congratulations!  You Win!')
        is_guessed = True
    else:
        print('That is not the word.  Try again.')