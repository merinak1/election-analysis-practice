# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import csv
import os

##Method 1 : DIRECT PATH
#  file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()

##Method 2 : INDIRECT PATH
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read and print the header row.
    headers = next(file_reader)
    print(headers)

   # Print each row in the CSV file.
    for row in file_reader:
         # 2. Add to the total vote count.
        total_votes += 1

    # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
        # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_options)

# Print the candidate vote dictionary.
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

# 3. Print the total votes.
print(total_votes)

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# with open(file_to_save, "w") as txt_file:
#       #To do: perform analysis.
#      print(election_data)

 # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

# # Write three counties to the file.
#      txt_file.write("Counties in the Election\n")
#      txt_file.write("------------\n")
#      txt_file.write("Arapahoe\nDenver\nJefferson")


# Close the file
#outfile.close()