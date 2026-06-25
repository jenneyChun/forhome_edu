import pytest


def test_d_val_01_g0_pass(grid_g0):
    # Given: G0 완성 4×4 마방진 (빈칸 없음)
    _ = grid_g0
    # When: validate_lines(grid_g0) 호출
    # Then: status=="pass", failed_lines==[]
    pytest.fail("RED: D-VAL-01 — 구현 없음, 의도적 실패")
