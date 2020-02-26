import os
import csv

budget_data_csv = os.path.join("Resources", "election_data.csv")

candidate_list = []
candidate_vote = []

with open(budget_data_csv) as csvfileread:
    csvreader = csv.reader(csvfileread, delimiter=",")
    csv_header = next(csvreader)

    totalvote = 0
    maxvote = 0

    for row in csvreader:

        totalvote += 1

        candidate = row[2]

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_vote.append(0)

        vote = candidate_list.index(row[2])

        candidate_vote[vote] += 1

    print("================================")
    print("Election Results")
    print("================================")
    print(f"Total Votes: {totalvote}")
    print("================================")

    for candidate_index in range(len(candidate_list)):
        candidate_name = str(candidate_list[candidate_index])
        vote_count = str(candidate_vote[candidate_index])
        vote_percentage = round((int(vote_count)/totalvote)*100,3)

        if int(vote_count) > maxvote:
            maxvote = int(vote_count)
            topcandidate = str(candidate_name)

        print(f"{candidate_name}: {vote_percentage}% ({vote_count})")
    
    print("================================")
    print(f"Winner: {topcandidate}")
    print("================================")

output = os.path.join("poll_summary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output, 'w') as textfile:


    
    textfile.write("================================" + "\n")
    textfile.write("Election Results" + "\n")
    textfile.write("================================" + "\n")       
    textfile.write(f"Total Votes: {totalvote}" + "\n")
    textfile.write("================================" + "\n")

    for candidate_index in range(len(candidate_list)):
        candidate_name = str(candidate_list[candidate_index])
        vote_count = str(candidate_vote[candidate_index])
        vote_percentage = round((int(vote_count)/totalvote)*100,3)
    
        textfile.write(f"{candidate_name}: {vote_percentage}% ({vote_count})" + "\n")
    textfile.write("================================" + "\n")
    textfile.write(f"Winner: {topcandidate}" + "\n")
    textfile.write("================================" + "\n")






