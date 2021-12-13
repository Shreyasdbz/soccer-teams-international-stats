import csv
import pandas as pd
import matplotlib

# ############################################
# Helper functions ------------------
# ############################################
def extract_date_to_year(date_str):
    '''
    Extracts from a date string the year
    '''
    date_split = date_str.split('-')
    year = ''
    for val in date_split:
        if(len(val) == 4):
            year = val
    return str(year)



# ############################################
# Main Code
# ############################################

# Step [1] --- Import and store data from csv

raw_data = []
unique_years = []
unique_teams = []

with open('data/results.csv') as results_file:
    reader = csv.reader(results_file)
    next(reader)
    for matchup in reader:
        # matchup[0] : date
        # matchup[1] : home team
        # matchup[2] : away team
        # matchup[3] : home score
        # matchup[4] : away score
        raw_data.append(matchup)
        year = str(extract_date_to_year(matchup[0]))
        if year not in unique_years:
            unique_years.append(year)
        home_team = matchup[1]
        away_team = matchup[2]
        if home_team not in unique_teams:
            unique_teams.append(home_team)
        if away_team not in unique_teams:
            unique_teams.append(away_team)


# Step [2] --- Create and populate a dictionary with inital values

data_dict = {}
# Create an empty dict of dicts to be filled
empty_teams_list = {}
for team in unique_teams:
    empty_teams_list[team] = 0
for y in unique_years: 
    data_dict[y] = empty_teams_list
# Fill the dictionary by using the raw data
for match in raw_data:
    home_team = ''
    away_team = ''
    home_score = 0
    away_score = 0
    if((match[3]).upper() == 'NA' or (match[4]).upper() == 'NA'):
        continue
    else:
        home_team = match[1]
        away_team = match[2]
        home_score = int(match[3])
        away_score = int(match[4])
    # Home Team Win
    if home_score > away_score:
        year = str(extract_date_to_year(match[0]))
        data_dict[year][home_team] += 1        
    # Away Team Win
    elif home_score < away_score:
        year = str(extract_date_to_year(match[0]))
        data_dict[year][away_team] += 1        
    # Draw
    elif home_score == away_score:
        # noOp
        pass
    else:
        print('ERROR: Match score unreadable')
# print(data_dict)

# Step [3] --- Import and store data from csv

wins_temp = empty_teams_list
# for year in data_dict:
#     for team in data_dict[year]:
#         data_dict[year][team] += int(wins_temp[team])
#     wins_temp = data_dict[year]
# print(wins_temp)
