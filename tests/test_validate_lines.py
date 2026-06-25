from validate_lines import validate_lines


def test_t2_fail_r2_c2_wrong_sum():
    # Arrange — 완성 격자, (2,2) 1-based 값 6→7 (R2·C2 합 35)
    grid = [
        [16, 3, 2, 13],
        [5, 7, 12, 11],
        [9, 10, 7, 8],
        [4, 15, 14, 1],
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "R2" in result["failed_lines"]
    assert "C2" in result["failed_lines"]
