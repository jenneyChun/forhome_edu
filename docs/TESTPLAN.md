# MagicSquare_1004 — Test Plan (RED)

| 항목 | 내용 |
|------|------|
| 프로젝트 | MagicSquare_1004 Session 3 |
| Phase | **RED (Ask)** |
| SSOT | [`PRD.md`](PRD.md) · [`.cursorrules`](../.cursorrules) · [`README.md`](../README.md) |
| 갱신일 | 2026-06-25 |

본 문서는 README RED 체크리스트(Logic · UI Track)를 **C2C 실행 가능한 테스트 플랜**으로 펼친다.  
각 Test ID마다 FR → To-Do → Given/When/Then · 파일 경로 · pytest 명령 · Expected RED Failure를 고정한다.

---

## 1. RED 공통 절차

| # | 단계 | Command | 산출물 | 금지 |
|---|------|---------|--------|------|
| 1 | 설계 | `/red-test-plan` | C2C 4블록 (채팅 출력) | `tests/`·`src/` 생성 |
| 2 | 스켈레톤 | `/red-skeleton` | `pytest.fail("RED: {ID}")` | assert 본문 · Domain 호출 |
| 3 | assert RED | `/tdd-red` | AAA assert · pytest **FAIL** | `src/` · skip/xfail |
| 4 | — | — | 1 RED 묶음 = **Test ID 1개** | assert 완화 |

**상수:** `34`/`16`/`4`/`0` 리터럴 금지 → `tests/entity/constants.py`  
**픽스처:** `tests/conftest.py` — `grid_g1` (G1, 빈칸 2개 row-major)

---

## 2. Track B — Logic (`tests/entity/`, `tests/test_validate_lines.py`)

**규칙:** Domain Mock 금지 · E001~E005 emit 금지 · boundary import 금지  
**계약:** INV-* · AC-* (PRD §2, §4)

### 2.1 D-LOC-01 — `find_blank_coords` ✅ GREEN

| 항목 | 내용 |
|------|------|
| FR | FR-LOC-01 |
| AC / INV | AC-LOC-01 · INV-06 |
| 파일 | `tests/entity/test_d_loc_01.py` |
| 함수 | `test_d_loc_01_blank_coords_row_major` |
| Given | `grid_g1` — G1, `(2,3)`·`(4,4)` 1-based `0` |
| When | `find_blank_coords(grid)` |
| Then | `[(2, 3), (4, 4)]` (row-major, 1-index) |
| pytest | `python -m pytest tests/entity/test_d_loc_01.py -v` |
| RED Failure | `pytest.fail` / `ModuleNotFoundError` *(완료)* |

### 2.2 D-SOL-01 — `solution_step_a` ✅ GREEN

| 항목 | 내용 |
|------|------|
| FR | FR-SOL-01 |
| AC / INV | AC-SOL-01 · INV-08 |
| 파일 | `tests/entity/test_d_sol_01.py` |
| 함수 | `test_d_sol_01_step_a_success` |
| Given | `grid_g1` |
| When | `solution_step_a(grid)` |
| Then | `status=="success"`, `step=="A"`, golden matched |
| pytest | `python -m pytest tests/entity/test_d_sol_01.py -v` |
| golden | `tests/golden/d-sol-01.approved.txt` |

### 2.3 T2 — `validate_lines` fail (선 합) ✅ RED (assert)

| 항목 | 내용 |
|------|------|
| FR | FR-VAL-02 |
| AC / INV | AC-VAL-02 · INV-01 · INV-05 · INV-09 |
| 파일 | `tests/test_validate_lines.py` |
| 함수 | `test_t2_fail_r2_c2_wrong_sum` |
| Given | 완성 4×4, **(2,2) 1-based `6→7`** → R2·C2 합 **35** |
| When | `validate_lines(grid)` |
| Then | `status=="fail"`, `"R2"`·`"C2"` ∈ `failed_lines` |
| grid | `[[16,3,2,13],[5,7,12,11],[9,10,7,8],[4,15,14,1]]` |
| pytest | `python -m pytest tests/test_validate_lines.py::test_t2_fail_r2_c2_wrong_sum -v` |
| Expected RED | `TypeError` (`None` 반환) *(현재)* |

### 2.4 T3 — `validate_lines` incomplete ⬜ 예정

| 항목 | 내용 |
|------|------|
| FR | FR-VAL-03 |
| AC / INV | AC-VAL-03 · **INV-10** |
| 파일 | `tests/test_validate_lines.py` *(예정)* |
| 함수 | `test_t3_incomplete_when_blank_exists` *(예정)* |
| Given | `grid_g1` 또는 빈칸 ≥1 격자 |
| When | `validate_lines(grid)` |
| Then | `status=="incomplete"`, `failed_lines==[]` |
| 우선순위 | `0` 존재 시 선 합 검증·실패 보고 **하지 않음** |
| pytest | `python -m pytest tests/test_validate_lines.py -k T3 -v` |
| Expected RED | `AssertionError` / `TypeError` |

### 2.5 D-MIS-01 — `find_not_exist_nums` ⬜ 예정

| 항목 | 내용 |
|------|------|
| FR | FR-MIS-01 |
| AC / INV | AC-MIS-01 · INV-07 · INV-11 |
| 파일 | `tests/entity/test_d_mis_01.py` *(예정)* |
| 함수 | `test_d_mis_01_g1_missing_nums_ascending` *(예정)* |
| Given | `grid_g1` |
| When | `find_not_exist_nums(grid)` |
| Then | `[7, 10]` (오름차순) |
| pytest | `python -m pytest tests/entity/test_d_mis_01.py -v` |
| Expected RED | `ModuleNotFoundError` / `pytest.fail("RED: D-MIS-01")` |

### 2.6 D-VAL-01 — 완성 격자 pass ⬜ 예정

| 항목 | 내용 |
|------|------|
| FR | FR-VAL-01 |
| AC / INV | AC-VAL-01 · INV-01 · INV-02 |
| 파일 | `tests/entity/test_d_val_01.py` 또는 `tests/test_validate_lines.py` *(예정)* |
| 함수 | `test_d_val_01_g0_pass` *(예정)* |
| Given | **G0** — 빈칸 없는 완성 4×4 마방진 |
| When | `validate_lines(grid)` 또는 `is_magic_square(grid)` |
| Then | `status=="pass"`, `failed_lines==[]` |
| pytest | `python -m pytest tests/entity/test_d_val_01.py -v` |
| Expected RED | `AssertionError` / `TypeError` |

---

## 3. Track A — UI (`tests/boundary/`)

**규칙:** Domain **Mock 허용** · Then에 **E00*** 명시 · `execute(grid)` 진입점  
**계약:** E-* · AC-IN/OUT/FLOW (PRD §3, §4)

### 3.1 U-IN-01 — `grid=None` ⬜ 설계

| 항목 | 내용 |
|------|------|
| FR | FR-IN-01 |
| AC / E | AC-IN-01 · **E003** `INVALID_NULL` |
| 파일 | `tests/boundary/test_input_validation.py` *(예정)* |
| 함수 | `test_u_in_01_null_grid_returns_e003` |
| Given | `grid = None` |
| When | `execute(grid)` |
| Then | 결과에 `"E003"` 또는 `"INVALID_NULL"` 포함 |
| conftest | `grid_none` → `None` |
| pytest | `python -m pytest tests/boundary/test_input_validation.py -k U-IN-01 -v` |
| Expected RED | `ModuleNotFoundError` / `pytest.fail("RED: U-IN-01")` |

### 3.2 U-IN-02 — 3×4 크기 ⬜ 설계

| 항목 | 내용 |
|------|------|
| FR | FR-IN-02 |
| AC / E | AC-IN-02 · **E001** `INVALID_SIZE` |
| 파일 | `tests/boundary/test_input_validation.py` |
| 함수 | `test_u_in_02_invalid_size_returns_e001` |
| Given | `grid_3x4` — 3행×4열 |
| When | `execute(grid)` |
| Then | 결과에 `"E001"` 또는 `"INVALID_SIZE"` 포함 |
| grid 예시 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` |
| pytest | `python -m pytest tests/boundary/test_input_validation.py -k U-IN-02 -v` |
| Expected RED | `AssertionError` *(E001 미반환)* |

### 3.3 U-IN-03 — 빈칸 0개 ⬜ 설계

| 항목 | 내용 |
|------|------|
| FR | FR-IN-03 |
| AC / E | AC-IN-03 · **E002** `INVALID_BLANKS` |
| 파일 | `tests/boundary/test_input_validation.py` |
| 함수 | `test_u_in_03_zero_blanks_returns_e002` |
| Given | 완성 격자 (빈칸 `0` 없음) |
| When | `execute(grid)` |
| Then | 결과에 `"E002"` 또는 `"INVALID_BLANKS"` 포함 |
| pytest | `python -m pytest tests/boundary/test_input_validation.py -k U-IN-03 -v` |
| Expected RED | `AssertionError` |

### 3.4 U-OUT-01 — boundary 출력 형태 ⬜ 예정

| 항목 | 내용 |
|------|------|
| AC | AC-OUT-01 |
| Given | 유효 입력 G1 |
| When | `execute(grid_g1)` |
| Then | `len(result) == 6` *(boundary 결과 dict 키 6개)* |
| Expected RED | `pytest.fail("RED: U-OUT-01")` |

### 3.5 U-FLOW-02 — domain 미호출 ⬜ 예정

| 항목 | 내용 |
|------|------|
| AC | AC-FLOW-01 |
| Given | `grid = None` |
| When | `execute(grid)` |
| Then | domain `execute()` **0회** 호출 (Mock 검증) |
| Expected RED | `pytest.fail("RED: U-FLOW-02")` |

### 3.6 E004 · E005 ⬜ 예정

| ID | 이름 | 조건 | 비고 |
|----|------|------|------|
| E004 | `INVALID_VALUE` | 셀 값이 `0`·`1~16` 외 | Test ID 미할당 |
| E005 | `INVALID_DUPLICATE` | `1~16` 중복 | Test ID 미할당 |

---

## 4. 픽스처 SSOT

### G1 (`grid_g1`) — `tests/conftest.py`

```
[16,  3,  2, 13]
[ 5,  6,  0, 11]   ← (2,3)=0
[ 9, 10,  7,  8]
[ 4, 15, 14,  0]   ← (4,4)=0
```

| 픽스처 | 용도 | Test ID |
|--------|------|---------|
| `grid_g1` | 빈칸 2개 | D-LOC-01, D-SOL-01, D-MIS-01, T3, U-OUT-01 |
| `grid_none` *(예정)* | `None` | U-IN-01, U-FLOW-02 |
| `grid_3x4` *(예정)* | 3×4 | U-IN-02 |
| `grid_g0` *(예정)* | 완성 마방진 | D-VAL-01 |

---

## 5. ECB · Mock 점검

| Track | 경로 | Mock | E emit | RED Then |
|-------|------|------|--------|----------|
| **Logic** | `tests/entity/`, `tests/test_validate_lines.py` | **금지** | **금지** | assert / `pytest.fail` |
| **UI** | `tests/boundary/` | **허용** | **허용** | E00* 문자열 · Mock 호출 횟수 |

---

## 6. RED 실행 순서 (권장)

```
[완료] D-LOC-01 → D-SOL-01 → T2 (assert RED)
[다음] T2 GREEN (/green-minimal) — validate_lines 선 합
       T3 RED — incomplete (INV-10)
       D-MIS-01 RED — find_not_exist_nums
       U-IN-01/02 RED 묶음 — boundary 스켈레톤
       D-VAL-01 RED — G0 pass
```

---

## 7. RED 진행 현황

| Test ID | Track | RED | GREEN | 비고 |
|---------|-------|-----|-------|------|
| D-LOC-01 | Logic | ✅ | ✅ | |
| D-SOL-01 | Logic | ✅ | ✅ | golden |
| T2 | Logic | ✅ assert | ⬜ | `validate_lines` stub |
| T3 | Logic | ⬜ | ⬜ | |
| D-MIS-01 | Logic | ⬜ | ⬜ | |
| D-VAL-01 | Logic | ⬜ | ⬜ | |
| U-IN-01 | UI | ⬜ 설계 | ⬜ | |
| U-IN-02 | UI | ⬜ 설계 | ⬜ | |
| U-IN-03 | UI | ⬜ 설계 | ⬜ | |
| U-OUT-01 | UI | ⬜ | ⬜ | |
| U-FLOW-02 | UI | ⬜ | ⬜ | |

---

*본 문서는 `docs/TESTPLAN.md` — MagicSquare_1004 RED Test Plan (README §RED 체크리스트 기반)입니다.*
