# Coding Exercise: Decoding a Secret Message
# In this exercise, you will write code to solve a problem. Your code must be in either Python or JavaScript—solutions in other 
# languages will not be accepted! You can write your code using any IDE you want.

# Problem
# You are given a Google Doc like this one that contains a list of Unicode characters and their positions in a 2D grid. 
# Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in 
# the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a 
# graphic showing a sequence of uppercase letters, which is the secret message.
# The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.
# The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.
# Any positions in the grid that do not have a specified character should be filled with a space character.
# You can assume the document will always have the same format as the example document linked above.

# For example, the simplified example document linked above draws out the letter 'F':

# █▀▀▀
# █▀▀ 
# █   
# Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x- and y-coordinates increase.

# Specifications
# Your code must be written in Python (preferred) or JavaScript.
# You may use external libraries.
# You may write helper functions, but there should be one function that:
# 1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND
# 2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.
import requests
import pandas as pd
import lxml

def process_google_doc(url):
    try:
        # response = requests.get(url)
        # response.raise_for_status()

        # #Start with getting the content, then printing the contents
        # content = response.text
        # print("Document content:")
        # print(content)

        df = pd.read_html(url, encoding='utf-8')
        print(df[0])

    except requests.exceptions.RequestException as ex:
        print(f"An error with the request has occurred: {ex}")
        return None


# Example usage
document_id = "2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq"
simple_google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
process_google_doc(simple_google_doc_url)