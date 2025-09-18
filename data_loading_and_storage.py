# %%
# %%
# %%
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 06:53:26 2025

@author: bbatte
"""

# ----------------------------------------------------------
# Lab 5 - Part 1: CSV Data Handling
# Dataset: winequality-red.csv (downloaded from Kaggle)
# Author: [Your Name]
# ----------------------------------------------------------

# Step 1: Import pandas library
# Pandas is a Python library used for data manipulation and analysis.
import pandas as pd

print("Step 1: Pandas library imported successfully.\n")

# Step 2: Load the dataset into a Pandas DataFrame
# Assumes winequality-red.csv is in the same folder as this script.
df = pd.read_csv("winequality-red.csv")

print("Step 2: Dataset loaded into a DataFrame.\n")
print("First 5 rows of the original dataset:\n")
print(df.head())   # Display first 5 rows for verification
print("\nDataset shape (rows, columns):", df.shape)
print("-" * 50, "\n")

# Step 3: Add a new column called 'ID' that assigns a unique number to each row
# We use Python's range() to generate IDs starting from 1 up to the number of rows.
df["ID"] = range(1, len(df) + 1)

print("Step 3: Added 'ID' column with unique values for each row.\n")
print("Check the last 5 rows to confirm IDs were assigned correctly:\n")
print(df.tail())   # Display last 5 rows to confirm IDs increment correctly
print("-" * 50, "\n")

# Step 4: Display the first 10 rows of the updated DataFrame
print("Step 4: Displaying the first 10 rows of the updated DataFrame:\n")
print(df.head(10))   # Show first 10 rows
print("-" * 50, "\n")

# Step 5: Export the updated DataFrame to a new CSV file
# We name the new file "winequality-red-with-id.csv"
# Setting index=False so that Pandas does not write row numbers.
df.to_csv("winequality-red-with-id.csv", index=False)

print("Step 5: Exported the updated DataFrame to 'winequality-red-with-id.csv'.\n")




# ----------------------------------------------------------
# Lab 5 - Part 2: JSON Operations

# ----------------------------------------------------------

# Step 1: Import the json module
# The json library allows us to work with JSON data (JavaScript Object Notation).
import json

print("JSON library imported successfully.\n")

# ----------------------------------------------------------
# Task 7: Convert a sample JSON string into a Python object
# ----------------------------------------------------------

# A sample JSON string (note: keys and string values use double quotes in JSON)
json_string = '{"name": "Ramshe", "age": 30, "city": "West Jordan"}'

# Convert JSON string to Python dictionary using json.loads()
python_obj = json.loads(json_string)

print("Task 7: Converted JSON string into a Python object (dictionary).")
print("Original JSON string:", json_string)
print("Converted Python object:", python_obj)
print("Type of object after conversion:", type(python_obj))
print("-" * 50, "\n")

# ----------------------------------------------------------
# Task 8: Convert a Python object into JSON data
# ----------------------------------------------------------

# Define a Python dictionary
person_dict = {"name": "Winnie", "age": 25, "city": "Salt Lake City"}

# Convert Python dictionary to JSON string using json.dumps()
json_data = json.dumps(person_dict)

print("Task 8: Converted Python object (dictionary) into JSON string.")
print("Original Python dictionary:", person_dict)
print("Converted JSON string:", json_data)
print("Type of object after conversion:", type(json_data))
print("-" * 50, "\n")

# ----------------------------------------------------------
# Task 9: Convert various Python objects into JSON strings
# ----------------------------------------------------------

# Examples of Python objects
data_list = ["Toyota", "Benz", "Jeep"]
data_tuple = ("python", "java", "golang")
data_bool = True
data_int = 100

# Convert each to JSON strings
json_list = json.dumps(data_list)
json_tuple = json.dumps(data_tuple)   # Tuples become JSON arrays
json_bool = json.dumps(data_bool)
json_int = json.dumps(data_int)

print("Task 9: Converted various Python objects into JSON strings.")
print("Python List -> JSON:", json_list)
print("Python Tuple -> JSON:", json_tuple)
print("Python Boolean -> JSON:", json_bool)
print("Python Integer -> JSON:", json_int)
print("-" * 50, "\n")

# ----------------------------------------------------------
# Task 10: Convert a Python dictionary (sorted by keys) into 
#          a formatted JSON string with indent=4
# ----------------------------------------------------------

# Define a Python dictionary
student = {
    "id": 101,
    "name": "Edina",
    "age": 22,
    "major": "Computer Science"
}

# Convert dictionary to JSON string
# - sort_keys=True sorts dictionary by keys
# - indent=4 makes output human-readable
formatted_json = json.dumps(student, sort_keys=True, indent=4)

print("Task 10: Converted Python dictionary into a formatted JSON string.")
print("Original Python dictionary:", student)
print("Formatted JSON string (sorted by keys, indent=4):\n")
print(formatted_json)
print("-" * 50, "\n")




# ----------------------------------------------------------
# Lab 5 - Part 3: Working with NBA API
# ----------------------------------------------------------
# In this section I will:
#   1. Install and import the nba_api package
#   2. Retrieve all NBA players and teams
#   3. Look up LeBron James and Golden State Warriors IDs
#   4. Select a player of our choice (Stephen Curry)
#   5. Download his 2022-23 game logs
#   6. Export the game data to a CSV file
# ----------------------------------------------------------

# Step 1: Import required modules
# nba_api provides access to NBA stats data (players, teams, and game logs)
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd

print("Step 1: Libraries imported successfully.\n")

# ----------------------------------------------------------
# Step 2: Retrieve all NBA players
# get_players() returns a list of dictionaries with player information
# Each dictionary contains: id, full_name, first_name, last_name, etc.
# ----------------------------------------------------------
player_dict = players.get_players()
print("Step 2: Retrieved all NBA players.")
print("Total players retrieved:", len(player_dict))
print("Example player entry:\n", player_dict[0])  # Show first player as sample
print("-" * 50, "\n")

# Example: Find LeBron James and get his ID
# We filter the list of players by full_name == 'LeBron James'
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

print("LeBron James details:", bron)
print("LeBron James ID:", bron_id)
print("-" * 50, "\n")

# ----------------------------------------------------------
# Step 3: Retrieve all NBA teams
# get_teams() returns a list of dictionaries with team information
# Each dictionary contains: id, full_name, abbreviation, nickname, city, state, year_founded
# ----------------------------------------------------------
team_dict = teams.get_teams()
print("Step 3: Retrieved all NBA teams.")
print("Total teams retrieved:", len(team_dict))
print("Example team entry:\n", team_dict[0])  # Show first team as sample
print("-" * 50, "\n")

# Example: Find Golden State Warriors and get their ID
GSW = [team for team in team_dict if team['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

print("Golden State Warriors details:", GSW)
print("Golden State Warriors ID:", GSW_id)
print("-" * 50, "\n")

# ----------------------------------------------------------
# Step 4: Get Game Log Data for a Player of Choice
# In this example, we choose Stephen Curry
# playergamelog.PlayerGameLog allows us to fetch game-level statistics
# We must provide: player_id and season (in format 'YYYY-YY')
# ----------------------------------------------------------
curry = [player for player in player_dict if player['full_name'] == 'Stephen Curry'][0]
curry_id = curry['id']
print("Step 4: Found Stephen Curry in players list.")
print("Stephen Curry Player Dictionary:", curry)
print("Stephen Curry ID:", curry_id)
print("-" * 50, "\n")

# Get Curry's game log for the 2022-23 NBA season
game_log = playergamelog.PlayerGameLog(player_id=curry_id, season='2022-23')

# Convert the game log into a Pandas DataFrame
df_games = game_log.get_data_frames()[0]

print("First 5 rows of Stephen Curry's 2022-23 game data:\n")
print(df_games.head())  # Display top 5 rows
print("Shape of DataFrame (rows, columns):", df_games.shape)
print("Columns available:\n", df_games.columns.tolist())
print("-" * 50, "\n")

# ----------------------------------------------------------
# Step 5: Export the game log to CSV
# We name the file 'stephen_curry_games_2022_23.csv'
# index=False prevents Pandas from writing row numbers into the CSV
# ----------------------------------------------------------
df_games.to_csv("stephen_curry_games_2022_23.csv", index=False)

print("Step 5: Exported Stephen Curry's 2022-23 game log to 'stephen_curry_games_2022_23.csv'.")
print("CSV file created.")
print("-" * 50, "\n")






















# %%

# %%

# %%