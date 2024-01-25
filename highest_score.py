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
new_user = input(str("Enter your 6 letter initials: "))

#function to call settings and score attribute
def update_score_list(settings, score):
    # If the game is not running and the score has not been added to the leaderboard
    if not settings.running and not score.added_to_leaderboard:
        current_score = score.score
        score.added_to_leaderboard = True  # Set a flag so it won't append the score again

        if current_score > existing_highest_score:
            # writes the new user and new score into the file
            f = open("highest_score_file.txt", "w")
            f.write( new_user  + "\n" + str(current_score))

def show_previous_highest_score(settings, screen):
    #  Font settings for "Game Over"  text
     text_color = (255, 255, 255)
     font = pygame.font.SysFont(None,38)
     showgameover = font.render( "Highest Score: " + str(existing_highest_score), True, text_color, settings.bg_color)
     dest=(57,66)
     screen.blit(showgameover,dest)
