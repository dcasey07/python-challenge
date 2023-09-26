# Import the modules
import os
import csv

# Create a path for the csv file from the Resources directory
electioncsv = os.path.join("Resources", "election_data.csv")

# Create lists to store the data from the election_data csv
voter_id = []
county = []
candidate = []

# Create a list for the unique candidates to be pulled from the candidate list
unique_candidate = []

# Create a dictionary to store the vote count keyed against the unique candidates
vote_count = {}

# Open the election_data csv file
with open(electioncsv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

# Pass by the header so the code only works with the raw data
    csvheader = next(csvfile)
    # Append the column data into their specific lists
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Initialize a dynamic value for the total number of votes cast based on the number of voter IDs in the dataset
totalvotes = len(voter_id)

# Create a loop to identify each candidate in the dataset and add them to a new list
for name in candidate:
    if name not in unique_candidate:
        unique_candidate.append(name)

# Create another loop that increments the votes for each candidate in a dictionary
for name in candidate:
    if name in vote_count:
        vote_count[name] += 1
    # Sets their vote count to 1 if they appear for the first time in the dictionary
    else:
        vote_count[name] = 1

# Initialize the winner of the election by pulling the highest vote count value from the dictionary
winner = max(vote_count, key = vote_count.get)

# Print the Election Results to the terminal
print("\n")
print("Election Results\n")
print("----------------------------\n")
print(f"Total Votes: {totalvotes}\n")
print("----------------------------\n")

# Create a loop to calculate the vote percentages using the total votes
for name in unique_candidate:
    percentage_votes = (vote_count[name] / totalvotes) * 100
    # Format the calculation to 3 decimal places
    formatted_pct_votes = round(percentage_votes, 3)
    # Print each result
    print(f"{name}: {formatted_pct_votes}% ({vote_count[name]})")

# Print the winner of the election
print("\n----------------------------\n")
print(f"Winner: {winner}\n")
print("----------------------------")

# Open and generate a text file to print the Election Results to the Analysis folder
with open(os.path.join("Analysis", "Election_Results.txt"), "w") as txt:
    # Transpose all of the print lines into the file so it updates with every new entry of future election results
    txt.write("\n")
    txt.write("Election Results\n")
    txt.write("\n")
    txt.write("----------------------------\n")
    txt.write("\n")
    txt.write(f"Total Votes: {totalvotes}\n")
    txt.write("\n")
    txt.write("----------------------------\n")
    txt.write("\n")
    for name in unique_candidate:
        percentage_votes = (vote_count[name] / totalvotes) * 100
        formatted_pct_votes = round(percentage_votes, 3)
        txt.write(f"{name}: {formatted_pct_votes}% ({vote_count[name]})\n")
    txt.write("\n----------------------------\n")
    txt.write("\n")
    txt.write(f"Winner: {winner}\n")
    txt.write("\n")
    txt.write("----------------------------")
    txt.close()