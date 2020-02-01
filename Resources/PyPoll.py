# Step 1 Data we need to retrieve from CSV file
# Modules
import os
import csv
file_to_load= os.path.join("..","RESOURCES","election_results.csv")

with open(file_to_load, newline='') as election_data:
    csvreader=csv.reader(election_data,delimiter=',')
    # To do: perform analysis 
    print(csvreader)
    print(election_data)
    #for row in csvreader:
    # print(row)
    headers=next(csvreader)
    print(headers)
    
#   Create a file name variable for output
    #file_to_save=os.path.join("..",analysis","election_analysis.txt")
    #outfile=open(file_to_save,"w")
    #outfile.write("Hello World")
    #Outfile.close()



# Step p2 Total # of Votes Cast
# Step 3  List of Candidates who recieved votes
# Step 4 Calculate % of votes for each candidate won
# Step 5 Total Number of Votes for each candidate won
# Step 6 The winner based on popular vote
# Close the file.
