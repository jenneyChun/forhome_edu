import pytest


def test_u_in_01_null_grid_returns_e003(grid_none):
    # Given: grid=None
    _ = grid_none
    # When: execute(grid) 호출
    # Then: 결과에 E003 / INVALID_NULL 포함
    pytest.fail("RED: U-IN-01 — 구현 없음, 의도적 실패")


def test_u_in_02_invalid_size_returns_e001(grid_3x4):
    # Given: grid_3x4 (3행×4열)
    _ = grid_3x4
    # When: execute(grid) 호출
    # Then: 결과에 E001 / INVALID_SIZE 포함
    pytest.fail("RED: U-IN-02 — 구현 없음, 의도적 실패")


def test_u_in_03_zero_blanks_returns_e002(grid_g0):
    # Given: 완성 격자 (빈칸 0개)
    _ = grid_g0
    # When: execute(grid) 호출
    # Then: 결과에 E002 / INVALID_BLANKS 포함
    pytest.fail("RED: U-IN-03 — 구현 없음, 의도적 실패")
