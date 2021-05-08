import random

word_list = ['monkey', 'ice-cream', 'automobile', 'aeroplane', 'game']


def get_play_word():
    return word_list[random.randint(0, (len(word_list) - 1))]

def guess_the_word():
    word = get_play_word()
    word_in_progress = ''
    guesses_left = 5
    for i in range(0, len(word)):
        if i == 0:
            word_in_progress = word[i]
        elif i == (len(word) - 1):
            word_in_progress += word[i]
        elif word[i] == '-':
            word_in_progress += '-'
        elif word[i] == ' ':
            word_in_progress += ' '
        else:
            word_in_progress += '_'

    print('You are playing Hangman. Rules: Each round you can type a letter to see if it is in the word. If it is not,'
          ' you will have to guess again. Be careful. If you make more than 5 wrong guesses, it is game over. '
          'Alternatively you can try to type the full word, but if it does not match the word fully it will be '
          'counted as a failed attempt. Have fun!')
    print('*************************************')
    print(word_in_progress)
    print('^^^^^^^^^^^^^^^^^^^^^^^^')
    while(True):
        guess = input('What is your guess: ').lower()
        print('#########################')
        if len(guess) == 1:
            if guess in word:
                for i in range(1, (len(word) - 1)):
                    if word[i] == guess:
                        temp_beginning = word_in_progress[:i]
                        temp_ending = word_in_progress[i + 1:]
                        word_in_progress = temp_beginning + guess + temp_ending
                print('The letter you guessed is in the word:')
                print('^^^^^^^^^^^^^^^^^^^^^')
                print('The word is:')
                print(word_in_progress)
                print('^^^^^^^^^^^^^^^^^^^^^')
                if word_in_progress == word:
                    print('Congrats! Your guess was correct!!!')
                    print('===========================')
                    break
            else:
                print('Sorry, your guess was incorrect!')
                print('*********************')
                guesses_left -= 1
                if guesses_left <= 0:
                    print('!!!!!!!!!!!!!!')
                    print('Game over! You are out of guesses! Try again!')
                    print('!!!!!!!!!!!!!!')
                    break
                print('^^^^^^^^^^^^^^^^^^^^^')
                print('Guesses left ' + str(guesses_left))
                print('The word is:')
                print(word_in_progress)
                print('^^^^^^^^^^^^^^^^^^^^^')
        elif guess == word:
            print('Congrats! Your guess was correct!!!')
            print('===========================')
            break
        else:
            print('Sorry, your guess was incorrect!')
            print('*********************')
            guesses_left -= 1
            if guesses_left < 0:
                print('!!!!!!!!!!!!!!')
                print('Game over! You are out of guesses! Try again!')
                print('!!!!!!!!!!!!!!')
                break
            print('^^^^^^^^^^^^^^^^^^^^^')
            print('Guesses left ' + str(guesses_left))
            print('The word is:')
            print(word_in_progress)
            print('^^^^^^^^^^^^^^^^^^^^^')
    print('Thank you for playing!!!')


# def print_incorrect_guess(guesses_left, word_in_progress):
#     print('Sorry, your guess was incorrect!')
#     print('*********************')
#     guesses_left -= 1
#     if guesses_left < 0:
#         print('!!!!!!!!!!!!!!')
#         print('Game over! You are out of guesses! Try again!')
#         print('!!!!!!!!!!!!!!')
#         break
#     print('^^^^^^^^^^^^^^^^^^^^^')
#     print(word_in_progress)
#     print('^^^^^^^^^^^^^^^^^^^^^')


guess_the_word()