
# **********************************
# This file is written by Calvin
# **********************************

import pygame.font

# Opens and reads leaderboard text file
f = open("highest_score_file.txt", "r")
LB = f.readlines()
f.close()

# Cleans up list
for i in range(len(LB)):
    LB[i] = LB[i].strip()

#reads previous recorded highscore and user
existing_highscore_user = LB[0]
existing_highest_score = int(LB[1])

#takes an input through terminal for new user session
new_user = input("**************************************************\n" +
                 "       _           ____   ____       _______ \n" +
                 "     / _ \        |  _ \_/ _  |     /  _____|\n" +
                 "    / /_\ \       | | \   / | |    /  /      \n" +
                 "   / _____ \      | |  \_/  | |    |  |      \n" +
                 "  / /     \ \     | |       | |    \  \_____ \n" +
                 " /_/       \_\    |_|       |_|     \_______|\n" +
                 "                                             \n" +
                 "**************************************************\n" +
                 "Enter your name: ")

    #function to call settings and score attribute
def update_score_list(settings, score):
    # If the game is not running and the score has not been added to the leaderboard
    if not settings.running and not score.added_to_leaderboard:
        current_score = score.score
        score.added_to_leaderboard = True  # Set a flag so it won't append the score again
        #compares the current score to the previous highscore
        if current_score > existing_highest_score:
            # writes the new user and new score into the file
            f = open("highest_score_file.txt", "w")
            f.write( new_user  + "\n" + str(current_score))

#this function is an iteration of the show_game_over function
def show_previous_highest_score(settings, screen):
    #  Font settings
    text_color = (255, 255, 255)
    font = pygame.font.SysFont(None,27)
    showgameover = font.render( "Prev Highest by " + existing_highscore_user + ": " + str(existing_highest_score), True, text_color, settings.bg_color)
    dest=(63,66)
    screen.blit(showgameover,dest)
