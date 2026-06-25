import pytest

from tests.entity.constants import BLANK, GRID_SIZE


@pytest.fixture
def grid_g1():
    # GRID_SIZE×GRID_SIZE, blanks at (2,3)·(4,4) 1-based
    _ = GRID_SIZE
    return [
        [16, 3, 2, 13],
        [5, 6, BLANK, 11],
        [9, 10, 7, 8],
        [4, 15, 14, BLANK],
    ]


@pytest.fixture
def grid_g0():
    # 완성 4×4 마방진 — 빈칸 없음 (D-VAL-01, U-IN-03)
    _ = GRID_SIZE
    return [
        [16, 3, 2, 13],
        [5, 10, 11, 8],
        [9, 6, 7, 12],
        [4, 15, 14, 1],
    ]


@pytest.fixture
def grid_none():
    return None


@pytest.fixture
def grid_3x4():
    # 3행×4열 — U-IN-02
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
