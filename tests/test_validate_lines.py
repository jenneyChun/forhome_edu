import pytest


def test_t2_fail_r2_c2_wrong_sum():
    # Given: 완성 격자, (2,2) 1-based 값 6→7 (R2·C2 합 35)
    grid = [
        [16, 3, 2, 13],
        [5, 7, 12, 11],
        [9, 10, 7, 8],
        [4, 15, 14, 1],
    ]
    _ = grid
    # When: validate_lines(grid) 호출
    # Then: status=="fail", "R2"·"C2" in failed_lines
    pytest.fail("RED: T2 — 구현 없음, 의도적 실패")


def test_t3_incomplete_when_blank_exists(grid_g1):
    # Given: G1 격자 (빈칸 ≥1)
    _ = grid_g1
    # When: validate_lines(grid_g1) 호출
    # Then: status=="incomplete", failed_lines==[]
    pytest.fail("RED: T3 — 구현 없음, 의도적 실패")
