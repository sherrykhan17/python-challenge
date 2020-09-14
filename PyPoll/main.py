import os
import csv

election_data_csv = os.path.join("./", "Resources", "election_data.csv")
election_data_csv_output = os.path.join("./", "analysis", "election_data.txt")
candidates = {}

with open(election_data_csv) as csvelectiondata:
    reader = csv.DictReader(csvelectiondata)

    for row in reader:
        if candidates.get(row["Candidate"]) is None:
            candidates[row["Candidate"]] = [row["Voter ID"]]
        else:
            candidates[row["Candidate"]].append(row["Voter ID"])

# Get the winner
winner = ["", 0]

# Calculate total votes
total_votes = 0
for candidate in candidates.keys():
    votes = len(candidates[candidate])
    total_votes += votes

    # check winner's votes
    if votes > winner[1]:
        winner = [candidate, votes]

output = "Election Results \n"
output += "---------------------------- \n"
output += f'Total votes: {total_votes} \n'
output += "---------------------------- \n"

for candidate in candidates.keys():
    votes = len(candidates[candidate])
    output += f'{candidate}: {round(( votes / total_votes ) * 100, 3)}% ({votes}) \n'

output += "---------------------------- \n"
output += f'Winner: {winner[0]} \n'
output += "----------------------------"
print(output)

# Write to the file
txt_file = open(election_data_csv_output, "w")
txt_file.write(output)
txt_file.close()