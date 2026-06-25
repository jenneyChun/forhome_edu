import pytest


def test_u_flow_02_null_grid_domain_not_called(grid_none):
    # Given: grid=None
    _ = grid_none
    # When: execute(grid) 호출
    # Then: domain execute() 0회 호출 (Mock 검증)
    pytest.fail("RED: U-FLOW-02 — 구현 없음, 의도적 실패")
