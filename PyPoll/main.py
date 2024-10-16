# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Winning Candidate and Winning Count Tracker
charles_votes = 0
diana_votes = 0
raymon_votes = 0 

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []
candidate_votes = {
    "Charles Casper Stockham" : charles_votes,
    "Diana DeGette" : diana_votes,
    "Raymon Anthony Doane" : raymon_votes
}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="") 

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

        # Add a vote to the candidate's count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1

#Access vote counts from dictionary
charles_votes = candidate_votes["Charles Casper Stockham"]
diana_votes = candidate_votes["Diana DeGette"]
raymon_votes = candidate_votes["Raymon Anthony Doane"]

#Calculate percentages
charles_percent = charles_votes / total_votes * 100
diana_percent = diana_votes / total_votes * 100
raymon_percent = raymon_votes / total_votes * 100

#Determine winning candidate
winning_candidate = max(candidate_votes, key=candidate_votes.get)
winning_count = candidate_votes[winning_candidate]

#Output info
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})\n"
    f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})\n"
    f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})\n"
    "-------------------------\n"
    f"Winner: {winning_candidate}\n"
    "-------------------------\n"
)

# Open a text file to save the output:
with open(file_to_output, "w") as txt_file:
    #Print output to terminal
    print(output)
    txt_file.write(output)