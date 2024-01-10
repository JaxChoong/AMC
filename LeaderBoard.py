f = open("Leaderboard.txt", "r")
scores = f.readlines()
f.close()

for i in range(len(scores)):
    scores[i] = scores[i].strip()

print(scores)