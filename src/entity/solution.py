from entity.find_blank_coords import find_blank_coords

STEP_A = "A"
STATUS_SUCCESS = "success"


def solution_step_a(grid):
    blank_coords = find_blank_coords(grid)
    return {
        "step": STEP_A,
        "status": STATUS_SUCCESS,
        "blank_coords": blank_coords,
    }
