# Opens and reads leaderboard text file
f = open("Leaderboard.txt", "r")
LD = f.readlines()

# Cleans up list
for i in range(len(LD)):
    LD[i] = LD[i].strip()

# Current List = ['00000', '00000', '00000', '00000', '00000']
def update_score_list(score):
    current_score = score.score
    for i in range(len(LD)):
        if current_score > LD[i]:
            j = len(LD) - 1
            while j > i:
                LD[j] = LD[j - 1]
                j -= 1
            LD[i] = current_score
            break  # Exit the loop
# Records current score

f = open("Leaderboard.txt", "w")
for item in LD:
    f.write(item + "\n")