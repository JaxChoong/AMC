# import settings

# #opens and reads leaderboard text file
# f = open("Leaderboard.txt", "r")
# LD = f.readlines()
# f.close()

# #cleans up list
# for i in range(len(LD)):
#     LD[i] = int(LD[i].strip())

# # Current List = ['1.', '00000', '2.', '00000', '3.', '00000', '4.', '00000', '5.', '00000']

# #records current score
# def update_score_list(score):
#     current_score = score.score
#     for i in range(len(LD)):
#         if current_score > i:
#             j = len(LD)
#             while j < i:
#                 LD[j] = LD[j-1]
#                 j-=1
#             LD[i] = current_score

