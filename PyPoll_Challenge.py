#In this project, our final Python script will need to be able to deliver the following:

#1-Total number of votes cast
#2-Total votes by county and the %
#3-The county with the largest turnout 

#4-A complete list of candidates who received votes
#5-Total number of votes each candidate received
#6-Percentage of votes each candidate won
#7-The winner of the election based on popular vote


# Add dependencies
import csv
import os

# --------------------------------------------------------------------change these to relative paths, so they run anyware
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {} 


countyList =[]  #**************************************************************************Challenge instructions #2
countyVotes = {} #*************************************************************************Challenge instructions #3

# Track the winning candidate, vote count, percentage and largest vote count.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largestVoteCount = "" #***Challenge instructions #4

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #**********************************************************************************Challenge instructions #5
        # Get the county name from each row
        county_name = row[1]
        #add county name if it doesn't match another in the list
        if county_name not in countyList:
            # Add the county name to the county list.
            countyList.append(county_name)
            # And begin tracking that county's voter count.
            countyVotes[county_name] = 0
        # Add a vote to that county's count.
        countyVotes[county_name] += 1


# Save the results to text file which we created in the analysis folder.
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

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    #*********************************************************************************************END For

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
