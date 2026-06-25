import pytest


def test_u_out_01_g1_result_has_six_keys(grid_g1):
    # Given: 유효 입력 G1
    _ = grid_g1
    # When: execute(grid_g1) 호출
    # Then: len(result)==6 (boundary 결과 dict 키 6개)
    pytest.fail("RED: U-OUT-01 — 구현 없음, 의도적 실패")
