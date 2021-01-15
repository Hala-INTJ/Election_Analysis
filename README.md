# Election_Analysis
## Overview of Election Audit:
This application was written for the election commission. It audits the results of a recent local congressional election. The solution expects the election results to be in a CSV file named "election_results.csv" in the "Resources" folder, with the following columns:
Ballot ID, County, Candidate. 
## Election-Audit Results:
The election results can be found in this text file:
<center>
| [election_analysis.txt](https://github.com/Hala-INTJ/Election_Analysis/blob/main/analysis/election_analysis.txt) |
| ---------------- |
| ![](https://github.com/Hala-INTJ/Election_Analysis/blob/main/analysis/Election%20Results%20Image.png) |
</center>

* There were 369,711 votes cast in the election.
* Breakdown of the number of votes and the percentage of total votes for each county:
  | County                  | Votes       | Percentage |
  | :---------------------- | ----------: | ----------:|
  | Jefferson | 38,855 | 10.5% |
  | Denver | 306,055 | 82.8% |
  | Arapahoe| 24,801 | 6.7% |
<br>

* Denver county received the largest number of votes. 
* Breakdown of the the number of votes and the percentage of the total votes each candidate received:
  | Candidate               | Votes       | Percentage |
  | :---------------------- | ----------: | ----------:|
  | Charles Casper Stockham | 85,213 | 23.1% |
  | Diana DeGette | 272,892 | 73.8% |  
  | Raymon Anthony Doane| 11,606 | 3.1% |
<br>

* Candidate Diana DeGette won the election with 73.8% of the vote and 272,892 votes.

## Election-Audit Summary:
The script serves as a prototype for analyzing the election results for a single election. For improved reusability and flexiblility, I propose the following script modifications to the election commission:
* Prompt the user for the input file or folder
* Prompt the user for the output file or base the output file name on the input file name
* Inspect the CSV headers to determine the presence and order of the "County" and "Candidate" columns
* Scan a folder with multiple CSV election files and process each one to analyze the results of multiple elections