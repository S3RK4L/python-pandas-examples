# Title:        Google Doc with Pandas
# Description:  This script takes in a published google doc as a parameter, reads in a table with characters and their respective coordinates, and 
#               uses these coordinates to place the characters in a 2D array where it is then printed to the console to form a shape. In the case of
#               this example, a google doc with the coordinates for a letter K is printed to the screen. 
# Last Edited:  25/09/2024

import requests
import pandas as pd
from io import StringIO

def decode(url):
    # retrieves the html of the google doc
    html = requests.get(url).text

    # converts any tables found in the html into a list of panda dataframe objects
    tables = pd.read_html(StringIO(html))

    # retrieve the first and only table from the list converted from an object to a dataframe
    df = pd.DataFrame(tables[0])

    # remove the first row containing the table headers, and get the coordinate columns converted to integers to retrieve the maximum coordinate both both the height and width of the 2d grid
    width = int( pd.to_numeric(df.iloc[1:].iloc[:, 0]).max() )
    height = int( pd.to_numeric(df.iloc[1:].iloc[:, 2]).max() )

    # define the initial 2d array with space characters (1 is added to width and height to ensure its in array format)
    grid_2d = [[" " for x in range(width+1)] for y in range(height+1)] 

    # only populate the coordinates of the grid used in the html table, with the character from the html table (leaving space characters where coordinate characters are not specified)
    for index, row in df.iterrows():
        if index != 0:
            grid_2d[int(row[2])][int(row[0])] = row[1]

    # we print the grid reversed as we want the bottom left to be 0,0 (not the top left)
    for row in reversed(grid_2d):
        for letter in row:
            print(letter, end="")
        print()

decode("https://docs.google.com/document/d/1_N6eAQkawtTyDGFPEV3TyOCs2zeZz6dM8Sxodl8fN8c/pub")