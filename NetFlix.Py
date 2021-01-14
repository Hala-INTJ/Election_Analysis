# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
file_to_load = os.path.join("/Users","hala","Desktop","Class Work","Module 3 - PyPoll with Python", "netflix_ratings.csv")

# Open the CSV
with open(file_to_load) as netflix_ratings:

    file_reader = csv.reader(netflix_ratings)
    next(file_reader)
    video_found = False

    # Loop through looking for the video
    for row in file_reader:
        if video == row[0]:
            print(f"{row[0]} is rated {row[1]} with a rating {row[5]}")
            video_found = True
            break

if not(video_found):
    print("Sorry about this, we don't seem to have what you are looking for!")
