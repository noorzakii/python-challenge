#import module
import os 
import csv

#set path to join
election_data_csv = os.path.join(os.path.dirname(__file__),"..", "Resources","election_data.csv")
csvpath= ('/Users/noorzaki/Desktop/Instructions-6/PyPoll/Resources/election_data.csv')

#set the output of the text file
text_path = "output.txt"

Casper_Count = 0
DeGette_Count = 0
Doane_Count = 0
#open csv file
with open(election_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile)
    #print(csvfile)

    for row in csvreader:

#conditional for 3rd row   
        if row[2] == "Casper":
            Casper_Count += 1
        elif row[2] == "DeGette":
            DeGette_Count += 1
        elif row[2] == "Doane":
            Doane_Count += 1
    
            

#set variables
total_votes_count = []
i = 0

#each candidate count 
#dictionary assigning candidatge
Results = {"Casper":Casper_Count, "DeGette":DeGette_Count, "Doane":Doane_Count}

# Calculate percentages and round to 3 decimal places
Casper_Percent = round(Casper_Count / total_votes_count) * 100
DeGette_Percent = round(DeGette_Count / total_votes_count) * 100
Doane_Percent = round(Doane_Count / total_votes_count) * 100

    #find highest value in dictionary
Winner = max(Results, key=Results.get)

#triple quotes lets me have multiple lines to be stored in string value
toprint = f"""Election Results
-----------------------
Total Votes: {total_votes_count} 
-----------------------
Casper: {Casper_Percent}% ({Casper_Count})
DeGette: {DeGette_Percent}% ({DeGette_Count})
Doane: {Doane_Percent}% ({Doane_Count})
-----------------------
Winner: {Winner} 
-----------------------"""

# print to Terminal
print(toprint)

# create txt file, print to it, and close
with open(text_path, 'w') as file:
    file.write(toprint)
    file.close()