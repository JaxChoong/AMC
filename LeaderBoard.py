










#leaderboard 
f = open("Leaderboard.txt", "r")
LD = f.readlines()
f.close()

for i in range(len(LD)):
    LD[i] = LD[i].strip()

print(LD)