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

# Candidate Options
candidate_options = []

# Candidate Votes
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# The file will close when you exit the block
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    # the_header = next(file_reader)
    # a_line_after_header = next(file_reader)
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
    #   print(row)
    #   Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1  


# Print the candidate list.
print(candidate_options)
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the keys of the candidate_votes
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote ({votes:,}).\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# winning_candidate = ("",0)
# for candidate, votes in candidate_votes.items():
#     if votes > winning_candidate[1]:
#         winning_candidate = (candidate,votes)

# print(winning_candidate)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    txt_file.write(f"{winning_candidate_summary}\n")

# Close the file.
# election_data.close()

