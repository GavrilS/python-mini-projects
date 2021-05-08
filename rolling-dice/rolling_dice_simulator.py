import random

def dice_roll():
    while(True):
        roll_val = random.randint(1, 6)
        print('You just rolled: ', roll_val)
        str = input('Do you want to roll again? Type yes or no: ').lower()
        if(str == 'n' or str == 'no'):
            break

    print('Thank you for playing!')

dice_roll()