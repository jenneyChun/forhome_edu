import pytest


def test_d_sol_01_step_a_success(grid_g1):
    # Given: G1 격자
    _ = grid_g1
    # When: solution_step_a(grid_g1) 호출
    # Then: status=="success", step=="A", golden matched
    pytest.fail("RED: D-SOL-01 — 구현 없음, 의도적 실패")
