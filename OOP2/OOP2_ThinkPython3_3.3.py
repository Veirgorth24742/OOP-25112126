def draw_grid(cols, rows):
    if cols < 1 or rows < 1:
        raise ValueError("columns and rows must be more than 0!")

    gridRows = "+" + (" -" * 4 + " +") * (cols - 1)
    gridColumns = ("|" + " " * 9) * (cols - 1) + "|"

    print(gridRows)
    for _ in range(rows - 1):
        for _ in range(4):
            print(gridColumns)
        print(gridRows)

print("Grid with 3 rows x 3 columns:")
draw_grid(3, 3)

print("Grid with 4 rows x 4 columns:")
draw_grid(4, 4)
