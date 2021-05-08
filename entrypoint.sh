#!/bin/bash

pick_game() {
    echo "Games: Adventure -> 1, Guess the number -> 2, Hangman -> 3, Mad-Libs -> 4, Dice -> 5"
    read -p "Please choose which game you want to play by typing the number of the game or type 0 to exit: " val

    if  [ $val -eq 1 ] 
    then
        python adventure_game.py
    elif  [ $val -eq 2 ] 
    then
        python guess_the_number.py
    elif  [ $val -eq 3 ]
    then
        python hangman.py
    elif [ $val -eq 4 ] 
    then
        python mad_libs_generator.py
    elif [ $val -eq 5 ] 
    then
        python rolling_dice_simulator.py
    elif [ $val -eq 0 ] 
    then
        echo "Thank you for playing!"
        return
    else
        echo "Please choose one of the expected numbers!"
    fi
    pick_game
}

pick_game
