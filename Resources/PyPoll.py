# Step 1 Data we need to retrieve from CSV file
# 1a. Modules
import os
import csv
#1b Read the file
file_to_load= os.path.join("..","RESOURCES","election_results.csv")
#1c open the file to save the analysis 
file_to_save=os.path.join("..","analysis","election_analysis.txt")

#1d Create Variable before Opening the file
#Create Counter for Total Votes
total_votes=0
# Create Candidate Options
candidate_options=[]
# Create Candidates Votes dictionary
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#1b. Open the file
with open(file_to_load, newline='') as election_data:
    csvreader=csv.reader(election_data,delimiter=',')
    # To do: perform analysis 
    print(csvreader)
    print(election_data)
    # Print Headers
    headers=next(csvreader)
    print(headers)

    # Step p2 Total # of Votes Cast
    for row in csvreader:
        total_votes=total_votes+1
    
#2. Add to the total vote count
    
        candidate_name= row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

# Step 3  List of Candidates who recieved votes
            candidate_votes[candidate_name]=0
        # Add vote count
        candidate_votes[candidate_name]+=1
# Step 4 Calculate % of votes for each candidate won
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percentage=float(votes)/float(total_votes)*100
        print(f'{candidate} has {vote_percentage:.1f}% Total Votes {candidate_votes[candidate]:,} out of {total_votes:,}\n')
# Step 5 Total Number of Votes for each candidate won
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            winning_candidate=candidate
            winning_count=votes
            winning_percentage=vote_percentage
# Step 6 The winner based on popular vote
winning_candidate_summary = (
    f"-------------------------\pn"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
print(candidate_options)
print(total_votes)
print(candidate_votes)

print(f'{candidate_name} has {vote_percentage} Total Votes {candidate_votes[candidate]} out of {total_votes}')

with open(file_to_save,"w") as election_analysis:
    election_analysis.write(str(total_votes)+"\n")
    election_analysis.write("Hello_Write")
# Close the file.