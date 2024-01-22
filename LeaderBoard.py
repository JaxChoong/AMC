# import settings
# import gamefunctions

# # Opens and reads leaderboard text file
# f = open("Leaderboard.txt", "r")
# LD = f.readlines()

# # Cleans up list
# for i in range(len(LD)):
#     LD[i] = int(LD[i].strip())

# # Current List = ['00000', '00000', '00000', '00000', '00000']

# # Records current score
# def update_score_list(score):
#     current_score = score
#     for i in range(len(LD)):
#         if current_score > LD[i]:
#             j = len(LD) - 1
#             while j > i:
#                 LD[j] = LD[j - 1]
#                 j -= 1
#             LD[i] = current_score
#             break  # Exit the loop

# # Example usage:
# new_score = current_score(score)
# update_score_list(new_score)

# f = open("Leaderboard.txt", "w")
# for score in LD:
#         f.write(str(score) + "\n")