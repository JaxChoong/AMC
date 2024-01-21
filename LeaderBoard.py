import settings

#opens and reads leaderboard text file
f = open("Leaderboard.txt", "r")
LD = f.readlines()
f.close()

#cleans up list
for i in range(len(LD)):
    LD[i] = LD[i].strip()

#records current score
def show_current_score(score):
    current_score = score.score
#     if not settings.running:
#         if current_score :
#             print("ligmaballschibai")
