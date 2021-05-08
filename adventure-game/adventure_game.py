import random

rooms = {
    0: {'n': 1, 'e': 7, 's': 13, 'w': 15},
    1: {'n': 2, 'e': 6, 's': 0},
    2: {'e': 3, 's': 1},
    3: {'e': 4, 's': 6, 'w': 2},
    4: {'s': 5, 'w': 3},
    5: {'n': 4, 'w': 6},
    6: {'n': 3, 'e': 5, 's': 7, 'w': 1},
    7: {'n': 6, 'e': 8, 'w': 0},
    8: {'s': 9, 'w': 7},
    9: {'n': 8, 's': 10, 'w': 12},
    10: {'n': 9, 'w': 11},
    11: {'n': 12, 'e': 10, 'w': 13},
    12: {'e': 9, 's': 11},
    13: {'n': 0, 'e': 11, 'w': 14},
    14: {'n': 15, 'e': 13},
    15: {'e': 0, 's': 14}
}

room_state = ['monsters', 'empty', 'treasure chest']

story1 = "You are walking on a deserted road in the middle of the night when you meet a person wearing a huge hat and " \
         "a mantle. He salutes you and asks if you would like to play a little game. You decide to take a break from your " \
         "walk and say 'Sure, why not'. He tosses you a golden coin and before you know what's happening you are engulfed " \
         "in a warm blue light. The next moment you are inside a huge room, wearing an armor and holding a huge sword " \
         "in one hand and the golden coin in the other. You hear the voice of the stranger coming from the coin saying: " \
         "Find the exit and you win, fail and you lose!"
origin_stories = [story1]

def get_random_list_element(list):
    return random.randint(0, (len(list) - 1))

def get_directions(arg):
    switcher = {
        'n': 'To go North enter n',
        'e': 'To go East enter e',
        's': 'To go South enter s',
        'w': 'To go West enter w'
    }
    return switcher.get(arg, 'To quit enter q')

def get_fight_results(arg):
    switcher = {
        1: 'You are pierced by the monsters huge horns. This is the end of the line for you! As the light fades away, you '
           'hear the monster laughing at you.',
        2: 'You and the monster start exchanging blows. In the end you win, but you are badly wounded. Fortunately for '
           'you there is a bottle of medicine on the floor. You take it and you start to feel a little better. After a '
           'little nap, you should be all better and ready to continue.',
        3: 'You have a fierce fight with the monster in front of you. It is a tough opponent indeed, but in the end '
           'you manage to somehow beat it(lucky you). You need to rest before you can continue!',
        4: 'You and the monster glare at each other, then you charge. The monster dodges you and tries to counter-attack '
           'you, but you are too swift for such nonsense. You go like this for a while, until you are both tired. You '
           'cry at the monster: \'Come to daddy!\', and you charge one more time. It suddenly looses it\'s sh*t and charges '
           'back at you. You clash, but your armor is pretty sturdy so you manage to knock the beast down. It was a good '
           'opponent, so you decide to spare it\'s life!',
        5: 'You come upon a ravenous beast and you say: \'You feel lucky, punk?\' It charges at you, but you are '
           'too good for it. In the end it succumbs to your awesome fighting skills!',
        6: 'You see the monster in front of you, but you don\'t even waver for a moment. An adventurer with your experience '
           'and skills has already seen it all. In fact you are so cool-headed that you simply stare at it with eyes that say: '
           '\'You are sh*t out of luck, mate!\' The monster is affected by your stare. It starts to tremble uncontrollably '
           'and in a moment it is engulfed by a fierce fire. In a mere blink of an eye it is gone!'
    }
    return switcher.get(arg)

def play_adventure():
    story = origin_stories[get_random_list_element(origin_stories)]
    print(story)
    victory_room = random.randint(1, (len(rooms) - 1))
    # print(victory_room)
    room = rooms[0]
    while(True):
        print('*********************************')
        print("You are inside a room with ", len(room), " doors!")
        for key in room.keys():
            print('Options: ' + get_directions(key))
        print('Options: To quit enter q')
        choice = input('Please make your choice: ').lower()
        if choice[0] == 'q':
            break
        elif choice[0] == 'n' or choice[0] == 'e' or choice[0] == 's' or choice[0] == 'w':
            room_num = room[choice[0]]
            room = rooms[room_num]
            print('You enter a new room!')
            print('You enter room number ', room_num)
            print('*********************************')
            if room_num == victory_room:
                print('In the center of the room you see a huge golden cup. Congratulations, you have won the contest!')
                break
        else:
            print('Invalid input!')
            continue

        room_st_num = get_random_list_element(room_state)
        room_st = room_state[room_st_num]
        if room_st == 'empty':
            print('The room is empty')
        elif room_st == 'treasure chest':
            print('Wohoooo you find a treasure chest. You are rich, now you just need to get out of this maze. Good for you!')
        else:
            courage = input('You see a huge monster sleeping in the center of the room! Do you want to fight it? Type yes or no: ').lower()
            if courage == 'no':
                print('You see that you can be no match for such a fierce demonic beast so you try to be very quite '
                      'while you take a look around the room! A little cowardly, but hey, in the end of the day, no reason '
                      'to go picking fights just for fun right?')
            elif courage == 'yes':
                print('You are a courageous person, so of course, you decide to fight it out with the monster. You let out '
                      'a battle cry, that can make even the bravest fellows piss their pants. The monster wakes up. '
                      'It\'s go time.')
                print('*********************************')
                fight_result = random.randint(1, 6)
                print(get_fight_results(fight_result))
                if fight_result == 1:
                    break
            else:
                print('The monster suddenly opens it\'s eyes and sees you. Then it gets up, looks at you with contempt and '
                      'leaves the room. Apparently it cannot stand people who break the rules. Next time type either yes '
                      'or no, please!')

    print('Thank you for playing!')


play_adventure()