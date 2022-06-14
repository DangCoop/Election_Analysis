# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#import datetime as dt
#now = dt.datetime.now()
#print("The time right now is", now)

import csv
import os



# load_file = './Resources/election_results.csv'
# file_open = open(load_file, 'r')
# csv_reader = csv.reader(file_open)
# for row in csv_reader:
#         print(row)
# file_open.close()

#with open(load_file) as file_open:
 #   print(file_open)

#<_io.TextIOWrapper name='Resources/election_results.csv' mode='r' encoding= 'UTF-8'>

load_file = os.path.join("Resources", "election_results.csv")  #add var with file name, which ссылается на путь к исходному файлу
with open(load_file) as file_open:
   print(file_open) 


file_save = os.path.join("analysis", "election_analysis.txt")
# file_save = './analysis/election_analusis.txt'
outfile = open(file_save, "w")
outfile.write('Hello World')
outfile.close

# всё что работает после 3.4.2

# # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#file_to_open = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

 # Печатаем все ряды все столбцы
 # Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigh a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
          # Print each row in the CSV file.
     for row in file_reader:
         print(row)

 #Печатаем содержание первого столбца/всех рядов
 # Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigh a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
          # Print each row in the CSV file.
     for row in file_reader:
        print(row[0])

#Печатаем заголовок
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigh a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     # Read and print the header row.
     headers = next(file_reader)
     print(headers)

#Печатаем общее кол-во голосов(голосующих)
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assigh a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     # Read and print the header row.
     headers = next(file_reader)
     #Print each row in the CSV file.
     for row in file_reader:
         # 2. Add to the total vote count.
            total_votes +=  1
            print(total_votes)

# Печатаем в ряд фамилии кандидатов
# Assign a variable to load a file from a path.
file_to_load = '/Users/dang/Desktop/Analysis Projects/Election_Analysis/Resources/election_results.csv' #'./Resources/election_results.csv'   #os.path.join("Resources", "election_results.csv")
# Assigh a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
#Candidate options and  candidate votes
candidate_options = []
#1. Declare an empty dictionary
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     # Read and print the header row.
     headers = next(file_reader)
     #Print each row in the CSV file.
     for row in file_reader:
         # 2. Add to the total vote count.
            total_votes +=  1
          # Print the candidate name from each row.
            candidate_name = row[2]
            # Add the candidate name to the candidate list. If candidate does not match any existing candidate...
            if candidate_name not in candidate_options:
                #Add candidate to the list of them.
                candidate_options.append(candidate_name) 
                #pirnt the candidate list.  
                print(candidate_options)
