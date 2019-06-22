#election data

#import csv and os module

import csv
import os

#define variables

winner = ""
win_votes = ""
candidate = ""
can_percent = {}
can_votes = {}
total_votes = 0


#add/open file path as write

filepath = ('Resources', './election_data.csv')
with open(filepath,'r', newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

   next(csvreader)

#send each unqique vote to "candidates"

   for row in csvreader:
       total_votes = total_votes + 1
       candidate = row[2]
       if candidate in can_votes:
           can_votes[candidate] = can_votes[candidate] + 1
       else:
           can_votes[candidate] = 1

#calcualting the percentage of unique candidates votes

for unique , total_votes in can_votes.items():
   can_percent[unique] = '{0:.0%}'.format(vote_count / total_votes)
   if vote_count > winner_votes:
       win_votes = vote_count
       winner = unique


#print and send to .txt 

print("Election Results")
print("-------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
for person, vote_count in can_votes.items():
   print(f"{person}: {can_percent[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print("------------------------")


save_file = "results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
   text.write(dashbreak + "\n")
   text.write(f"Total Votes: {total_votes}" + "\n")
   text.write(dashbreak + "\n")
   for person, vote_count in can_votes.items():
       text.write(f"{person}: {can_percent[person]} ({vote_count})" + "\n")
   text.write(dashbreak + "\n")
   text.write(f"Winner: {winner}" + "\n")
   text.write(dashbreak + "\n")