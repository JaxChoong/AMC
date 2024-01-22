# Opens and reads leaderboard text file
f = open("Leaderboard.txt", "r")
LD = f.readlines()

# Cleans up list
for i in range(len(LD)):
    LD[i] = int(LD[i].strip())

# Current List = ['00000', '00000', '00000', '00000', '00000']

# Records current score

f = open("Leaderboard.txt", "w")
f.write(str(LD) + "\n")