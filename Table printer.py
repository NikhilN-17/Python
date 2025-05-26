##Table Printer
print("Nikhil N,USN:1AY24AI075,SEC:O")
def print_table(data):
    # data is a list of lists, each inner list is a row
    # Find max width of each column
    cols = len(data[0])
    col_widths = [0] * cols
    for row in data:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))

    # Print rows with padding
    for row in data:
        row_str = " | ".join(str(item).ljust(col_widths[i]) for i, item in enumerate(row))
        print(row_str)
# Example usage:
table_data = [
    ["Name", "Age", "City"],
    ["Alice", "24", "New York"],
    ["Bob", "19", "Los Angeles"],
    ["Charlie", "32", "Chicago"]
]
print_table(table_data)


