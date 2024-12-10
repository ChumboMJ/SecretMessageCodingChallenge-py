import pandas as pd

def process_google_doc(url):
    # Reads the tables in from the given url. header = 0 ensures that the first row is counted as headers
    # and not values
    df = pd.read_html(url, header=0, encoding='utf-8')
    table = df[0]

    # Extract x-coord and y-coord columns from the table
    x_coordinates = table["x-coordinate"]
    y_coordinates = table["y-coordinate"]

    # Determine Grid Size for output
    max_x = x_coordinates.max()
    max_y = y_coordinates.max()

    # Create an empty grid, add 1 to the max_x and ma_y values to take 0 into consideration for coordinates.
    output_grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters in the grid
    for index, row in table.iterrows():
        x, y, char = row["x-coordinate"], row["y-coordinate"], row["Character"]
        output_grid[max_y - y][x] = char

    # Print the grid out row by row joined by nulls
    for row in output_grid:
        print(''.join(row))

# Example usage
simple_google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
print("Process simple google doc with \"F\" arrangement:")
process_google_doc(simple_google_doc_url)
print("Process complex google doc with multi-letterd output:")
process_google_doc(google_doc_url)