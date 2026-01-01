# Generate a frequency table for the ratings list which is initialized below.
# Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
#     a.	Start by creating an empty dictionary named content_ratings
#     b.	Loop through the ratings list. For each iteration, complete the following:
#         If the rating is already in content_ratings then increment the frequency
#  of that rating by 1.
#         Else, initialize the rating with a value of 1 inside the content_ratings dictionary.


ratings=['4+','3+','4+','9+']
current_ratings={}

rating=ratings.pop()
current_ratings[rating]=current_ratings.get(rating,0)+1

print(current_ratings)
