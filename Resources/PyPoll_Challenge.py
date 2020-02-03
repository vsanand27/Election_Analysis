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
# Create Candidate and County to obtain unique candidate names in for loops
candidate_options=[]
County_options=[]
# Create Votes dictionary to store votes by candidate and county
candidate_votes={}
county_votes={}
# Winning Candidate and Winning Count Tracker and county tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_county_turnout = ""
largest_county_vote = 0


#1d Open the file
with open(file_to_load, newline='') as election_data:
    csvreader=csv.reader(election_data,delimiter=',')
    # 1e Open analysis file to write`
    with open(file_to_save,"w") as election_analysis:
        next(csvreader)
        # Step 2 Total # of Votes Cast
        for row in csvreader:
            total_votes=total_votes+1
            
            #2a Add to the total vote count by candidate and County
            # Step 2a1 Calculate County Count Votes
            county_name=row[1]
            if county_name not in County_options:
                County_options.append(county_name)

                # Calculaculate count of votes by counties
                county_votes[county_name]=0
                # Add Vote Count
            county_votes[county_name]+=1
            
            # Step 2b  List of Candidates who recieved votes
            candidate_name= row[2]
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)

                candidate_votes[candidate_name]=0
                # Add vote count
            candidate_votes[candidate_name]+=1
        #Step 3 output to display and text file - top header lines
        Election_Summary =(
            f"-------------------------\n"
            f"Election Results          \n"
            f"-------------------------\n"
            f"Total_Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"                          \n"
            f"County Votes:             \n")
        print(Election_Summary)
        election_analysis.write(Election_Summary)
        
    # Step 4 Calculate % of votes for each county and each candidate
        # Step 4a Calculate votes for each county percentage
        for county in county_votes:
            c_votes=county_votes[county]
            C_vote_percentage=float(c_votes)/float(total_votes)*100
            print(f'{county}:{C_vote_percentage:.1f}% ({county_votes[county]:,})')
            election_analysis.write(f'{county}:{C_vote_percentage:.1f}% ({county_votes[county]:,})\n')
            
            if(c_votes>largest_county_vote):
                largest_county_vote=c_votes
                largest_county_turnout=county
        #Output to program and file
        print(f'\n----------------------')     
        print(f'Largest County Turnout: {largest_county_turnout}')
        print(f'----------------------')     
        election_analysis.write(f'\n----------------------\n')
        election_analysis.write(f'Largest County Turnout: {largest_county_turnout} \n')
        election_analysis.write(f'----------------------\n')
        # Step 4b Calculate for each candidate percentage
        for candidate in candidate_votes:
            votes=candidate_votes[candidate]
            vote_percentage=float(votes)/float(total_votes)*100
            print(f'{candidate}: {vote_percentage:.1f}% ({candidate_votes[candidate]:,}) ')
            election_analysis.write(f'{candidate}: {vote_percentage:.1f}% ({candidate_votes[candidate]:,})\n')

        # Step 4b.2 Total Number of Votes for candidate won
            if(votes>winning_count) and (vote_percentage>winning_percentage):
                winning_candidate=candidate
                winning_count=votes
                winning_percentage=vote_percentage

        # Step 5 The winner based on popular vote - write output to display and file
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        election_analysis.write(winning_candidate_summary)
#End of the Program

