import requests
import pandas as pd

def decode(url):
    html = requests.get(url).text

    tables = pd.read_html(html)

    df = pd.DataFrame(tables[0])

    # remove the first row containing the headers, and get the coordinate columns converted to integers to retrieve the maximum coordinate
    width = int( pd.to_numeric(df.iloc[1:].iloc[:, 0]).max() )
    height = int( pd.to_numeric(df.iloc[1:].iloc[:, 2]).max() )

    # 1 is added to width and height to ensure its in array format
    grid_2d = [[" " for x in range(width+1)] for y in range(height+1)] 

    for index, row in df.iterrows():
        if index != 0:
            grid_2d[int(row[2])][int(row[0])] = row[1]

    for row in reversed(grid_2d):
        for letter in row:
            print(letter, end="")
        print()

decode("https://docs.google.com/document/d/1_N6eAQkawtTyDGFPEV3TyOCs2zeZz6dM8Sxodl8fN8c/pub")