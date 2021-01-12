# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
# Hardcoded Path
# Path could be absolute or relative to the directory running python 'python3'
# file_to_load = 'Resources/election_results.csv'

# Constructed Path
# Running Python from Home Directory, the relative path would be:
# file_to_load = os.path.join("Desktop","Class Work","Module 3 - PyPoll with Python","Election_Analysis","Resources", "election_results.csv")

# Running Python from Election_Anlaysis folder, the relative path would be:
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file using a constructed path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# Initialize a total vote counter.
total_votes = 0

# The file will close when you exit the block
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    # the_header = next(file_reader)
    # a_line_after_header = next(file_reader)
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
    #   print(row)
    #   Add to the total vote count.
        total_votes += 1

    # Print the total votes.
    print(total_votes)    

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    #Write a header
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    # Write three counties to the file on three lines using '\n' newline
    txt_file.write("Arapahoe\nDenver\nJefferson")

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Close the file.
# election_data.close()

