import settings

# Opens and reads leaderboard text file
f = open("Leaderboard.txt", "r")
LD = f.readlines()
f.close()

# Cleans up list
for i in range(len(LD)):
    LD[i] = LD[i].strip()

# Current List = [0, 0, 0, 0, 0]

#function to call settings and score attribute
def update_score_list(settings, score):
    current_score = 0

    #if the game not running it will record the score as string
    if not settings.running:
        current_score = score.score

# if 10 >= int(LD[4]):
#     print("nah")

# writes the score into the file
f = open("Leaderboard.txt", "w")
for line in LD:
    f.writelines(f"{line}\n")