import csv
import pandas


filename = "MOCK_DATA_SORTED.csv"


# Accepts a .csv file and returns a .csv file with Porshe removed and Honda added
def add_honda(column):
    with open(filename, 'r') as csvfile:
        # Csv reader object
        csvreader = csv.reader(csvfile)

