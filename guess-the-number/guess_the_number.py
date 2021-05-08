import random

def get_random_number():
    return random.randint(1, 10)

def get_input():
    return int(input('Guess a number between 1 and 10: '))

def guessing_game():
    ran_num = get_random_number()
    guesses = 3
    for i in range(0, 3):
        answer = get_input()
        if answer == ran_num:
            print('Congratulations! You won!')
            return
        else:
            if i == 2 :
                break
            else:
                print(answer, 'was not the correct number. You have', (guesses - i - 1), 'guesses left. Try again!')

    print('Sorry, you didn\'t guess correctly! No more guesses left!')

guessing_game()