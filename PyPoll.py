import os
import csv

#Some Variables
votes = 0
candidate_votes = []
candidates = []
candict ={}
count = 0

#Open file
with open(os.path.join("Resources", "election_data.csv"), newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)


#   * The total number of votes cast
    for row in csvreader:
        votes+=1

# * A complete list of candidates who received votes#   
# * The total number of votes each candidate won.   
        recipient = row[2]
        if recipient in candict:
            candict[recipient] += 1
        else: 
            candict[recipient] = 1

#I initially did this whole thing with lists, but kept having ONE STRAY VOTE...
        # if votes == 1:
        #     candidates = [recipient]
        #     candidate_votes = [1]
        #     continue

        # for entry in candidates:
            # if recipient == candidates[count]:
            #     candidate_votes[count] += 1
            #     count=0
            #     break
            # elif len(candidates)-1 == count: 
            #     candidates.append(recipient)
            #     candidate_votes.append(1) 
            # count +=1
                # When a second candidate is added, 
                # they receive an extra vote. This is not the case for candidates 3 or 4.
                # Similarly, 2 of Khan's votes are appearing under a second Khan entry
                # It is, of course, spelled exactly the same
#List Check
        # if votes == 20:
        #     print(votes)
        #     break
        # elif votes <20:
        #     print(candidates)
        #     print(candidate_votes)
        #     print(votes)
        #     print("")

#   * The percentage of votes each candidate won and the winner based on popular vote
candidates=candict.keys()
candidate_votes=candict.values()
perc_won = [round(x/votes*100,3) for x in candidate_votes]
perc_won, candidate_votes, candidates = zip(*sorted(zip(perc_won, candidate_votes, candidates),reverse=True))
winner = candidates[0]

#check
    # print(winner)
    # print(candidates)
    # print(perc_won)
    # print(candidate_votes)
    # print(votes)
#Model
    #   Election Results
    #   -------------------------
    #   Total Votes: 3521001
    #   -------------------------
    #   Khan: 63.000% (2218231)
    #   Correy: 20.000% (704200)
    #   Li: 14.000% (492940)
    #   O'Tooley: 3.000% (105630)
    #   -------------------------
    #   Winner: Khan
    #   -------------------------
    #   ```
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

file = open("PyPoll_Results.txt", "w") 
file.write("Election Results")
file.write("\n----------------")
file.write(f"\nTotal Votes: {votes}")
file.write("\n----------------")

for recipient in candidates:
    file.write(f"\n{candidates[count]} {perc_won[count]}% ({candidate_votes[count]})")
    count+=1

file.write("\n----------------")
file.write(f"\nWinner: {winner}")
file.write("\n----------------")
file.close()

print(open("PyPoll_Results.txt", "r").read())
file.close()