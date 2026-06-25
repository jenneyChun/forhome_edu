from entity.constants import BLANK


def find_blank_coords(grid):
    coords = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == BLANK:
                coords.append((r + 1, c + 1))
    return coords
