# MagicSquare_1004 — PRD (Product Requirements Document)

> **MomTest Discovery 요약**  
> MomTest는 “무엇을 만들까”가 아니라 **어떤 계약을 검증할 수 있는가**를 발견하는 도구다.  
> 본 PRD는 세션 3 MomTest·Dual-Track 설계표에서 도출한 **판단 문장(FR)**, **불변식(INV)**, **에러(E)**, **수용 조건(AC)** 을 C2C 추적 가능한 ID로 고정한다.  
> **AC** = 사용자가 “됐다”고 받아들이는 조건 · **INV** = 어떤 입력에서도 깨지면 안 되는 규칙 · **E** = boundary가 반환하는 입력·흐름 오류.

| 항목 | 내용 |
|------|------|
| 프로젝트 | MagicSquare_1004 (4×4 마방진 검증·보조) |
| 세션 | Session 3 — C2C × Dual-Track TDD |
| SSOT 상수 | `MAGIC_CONSTANT=34`, `GRID_SIZE=4`, `MAX_NUM=16`, `BLANK=0` |
| 보조 SSOT | `.cursorrules` (TDD·API 형태), 본 PRD (계약 ID) |

---

## 1. 도메인 개요

4×4 격자에 `1`~`16`을 각 1회 배치한다. 미입력은 `BLANK(0)`이다.  
완성된 **10선**(행 R1~R4, 열 C1~C4, 대각 D1·D2)의 합은 **마법상수 34**와 같아야 한다.

| 기호 | 의미 |
|------|------|
| `G0` | 빈칸 없는 완성 4×4 격자 |
| `G1` | 빈칸 2개 — `(2,3)`, `(4,4)` 1-based (`tests/conftest.py` `grid_g1`) |
| 10선 | R1~R4, C1~C4, D1(↘), D2(↙) — **이 10개만** 검증·보고 |
| 좌표 | **1-index**, **row-major** (행 우선, 좌→우, 상→하) |

### 10선 셀 매핑 (0-index)

| 선 ID | 셀 |
|-------|-----|
| Rk | `grid[k-1][*]` |
| Ck | `grid[*][k-1]` |
| D1 | `grid[i][i]` for i=0..3 |
| D2 | `grid[i][3-i]` for i=0..3 |

---

## 2. 불변식 (INV)

어떤 유효 입력에서도 entity 로직이 지켜야 하는 규칙.  
Logic Track 테스트(`tests/entity/`)는 INV를 assert로 검증한다. **entity는 E emit 금지.**

| ID | 불변식 | 검증 예시 (Test ID) |
|----|--------|---------------------|
| **INV-01** | 완성 격자(G0)에서 **10선 각각**의 합은 `MAGIC_CONSTANT(34)`이다 | D-VAL-01, T2 |
| **INV-02** | 완성 격자에서 `1`~`MAX_NUM(16)`은 **각 정확히 1회** 등장한다 | D-VAL-01 |
| **INV-03** | 격자는 `GRID_SIZE×GRID_SIZE`(4×4)이다 | *(boundary E001과 분리)* |
| **INV-04** | 셀 값은 `BLANK(0)` 또는 `1`~`16`만 허용한다 | D-MIS-01, D-VAL-01 |
| **INV-05** | 검증·보고 대상 선은 **10선뿐**이다 (그 외 선 무시) | T2, validate_lines |
| **INV-06** | `find_blank_coords`는 `BLANK` 셀 좌표를 **row-major·1-index** `(row,col)` 리스트로 반환한다 | **D-LOC-01** |
| **INV-07** | `find_not_exist_nums`는 격자에 **없는** `1`~`16` 값을 찾는다 | D-MIS-01 |
| **INV-08** | `solution_step_a`는 Step `"A"`, `status="success"`, `blank_coords`를 반환한다 | **D-SOL-01** |
| **INV-09** | `validate_lines`의 `failed_lines` 항목은 `"R1"`~`"R4"`, `"C1"`~`"C4"`, `"D1"`, `"D2"` 형식이다 | T2 |
| **INV-10** | `incomplete`일 때 `failed_lines`는 **반드시 `[]`** 이다 (빈칸 있으면 선 실패 보고 안 함) | T3 *(예정)* |
| **INV-11** | `find_not_exist_nums` 결과는 **오름차순**이다 | D-MIS-01 |

> **우선순위 (validate_lines):** `0` 존재 → `incomplete` (INV-10). 빈칸 없을 때만 선 합·숫자 집합 검증.

---

## 3. 에러 코드 (E)

**boundary/UI Track** 전용. `execute(grid)` 등 진입점이 반환·포함한다.  
형식: `"E00N NAME"` 문자열 (golden·assert 공통).

| ID | 이름 | 조건 (MomTest 판단) | Test ID |
|----|------|---------------------|---------|
| **E001** | `INVALID_SIZE` | `grid`가 4×4가 **아니면** 유효하지 않다 | **U-IN-02** |
| **E002** | `INVALID_BLANKS` | 빈칸이 **정확히 2개가 아니면** 유효하지 않다 *(세션 3 입력 계약)* | **U-IN-03** |
| **E003** | `INVALID_NULL` | `grid`가 **None이면** 유효하지 않다 | **U-IN-01** |
| **E004** | `INVALID_VALUE` | 셀에 `0`·`1`~`16` **외 값**이 있으면 유효하지 않다 | *(예정)* |
| **E005** | `INVALID_DUPLICATE` | `1`~`16`이 **중복**이면 유효하지 않다 *(완성 입력 전제)* | *(예정)* |

**ECB:** entity(`src/entity/`)는 **E001~E005 raise/return 금지**. boundary만 emit.

---

## 4. 수용 조건 (AC)

사용자·교육자가 “요구사항 충족”으로 받아들이는 조건. FR보다 **관찰 가능한 결과**에 초점.

| ID | 수용 조건 | 연결 |
|----|-----------|------|
| **AC-VAL-01** | 완성 격자(G0)에 대해 `validate_lines`는 `status="pass"`, `failed_lines=[]`를 반환한다 | INV-01, INV-02 |
| **AC-VAL-02** | 빈칸 없이 한 선이라도 합≠34이면 `status="fail"`이고, 해당 선 ID가 `failed_lines`에 포함된다 | INV-01, INV-09 · **T2** |
| **AC-VAL-03** | 빈칸(`0`)이 하나 이상이면 `status="incomplete"`, `failed_lines=[]`이다 | INV-10 · **T3** *(예정)* |
| **AC-LOC-01** | G1에서 빈칸 좌표는 `[(2,3),(4,4)]` (row-major, 1-index)이다 | INV-06 · **D-LOC-01** |
| **AC-MIS-01** | G1에서 없는 숫자 목록은 `[7, 10]` 오름차순이다 | INV-07, INV-11 · D-MIS-01 |
| **AC-SOL-01** | G1에서 Step A는 `success`이고 `blank_coords`가 golden과 일치한다 | INV-08 · **D-SOL-01** |
| **AC-IN-01** | `grid=None`이면 결과에 `E003`/`INVALID_NULL`이 포함된다 | E003 · **U-IN-01** |
| **AC-IN-02** | `grid`가 3×4이면 결과에 `E001`/`INVALID_SIZE`가 포함된다 | E001 · **U-IN-02** |
| **AC-IN-03** | 빈칸 0개 격자는 `E002`/`INVALID_BLANKS`를 반환한다 | E002 · U-IN-03 |
| **AC-OUT-01** | 유효 입력 G1에 대해 boundary 결과 dict 키 개수는 6이다 | U-OUT-01 |
| **AC-FLOW-01** | `grid=None`이면 domain `execute()`는 **0회** 호출된다 | U-FLOW-02 |

---

## 5. 기능 요구 (FR) — C2C 판단 문장

MomTest Rule 1: **“~한다 / 허용한다 / 보고한다 / 판단한다”** 만 To-Do로 변환.

### 5.1 검증 API (`validate_lines`)

| ID | 판단 문장 |
|----|-----------|
| **FR-VAL-01** | 완성 격자에서 10선 합이 마법상수와 같으면 **pass로 판단한다**. |
| **FR-VAL-02** | 빈칸 없이 선 합이 마법상수와 다르면 **fail로 판단하고** 실패한 선 ID를 **보고한다**. |
| **FR-VAL-03** | 빈칸(`0`)이 하나 이상 있으면 **incomplete로 판단한다** (선 실패는 보고하지 않는다). |

### 5.2 Entity 보조

| ID | 판단 문장 |
|----|-----------|
| **FR-LOC-01** | 격자에 빈칸(`0`)이 있으면 해당 셀 좌표를 **row-major·1-index로 반환한다**. |
| **FR-MIS-01** | 격자에 없는 `1`~`16` 값을 **오름차순으로 보고한다**. |
| **FR-SOL-01** | G1에 대해 해결 Step A를 **시도하고** 성공 여부와 빈칸 좌표를 **반환한다**. |

### 5.3 Boundary 입력

| ID | 판단 문장 |
|----|-----------|
| **FR-IN-01** | 입력 `grid`가 **None이면** 유효하지 않다고 **판단한다**. |
| **FR-IN-02** | 입력 `grid`가 **4×4가 아니면** 유효하지 않다고 **판단한다**. |
| **FR-IN-03** | 입력 격자의 빈칸 개수가 **2가 아니면** 유효하지 않다고 **판단한다**. |

---

## 6. 공개 API 계약

```python
validate_lines(grid) -> dict
# grid: 4×4 list[list[int]]
# return: {"status": "pass"|"fail"|"incomplete", "failed_lines": list[str]}
```

| status | 조건 | failed_lines |
|--------|------|--------------|
| `pass` | 빈칸 없음, INV-01·INV-02 충족 | `[]` |
| `fail` | 빈칸 없음, INV-01 위반(선 합≠34 등) | 실패 선 ID 목록 |
| `incomplete` | `BLANK` ≥ 1 | **`[]` (INV-10)** |

```python
find_blank_coords(grid) -> list[tuple[int, int]]  # INV-06
find_not_exist_nums(grid) -> list[int]            # INV-07, INV-11
solution_step_a(grid) -> dict                       # INV-08
```

---

## 7. C2C 추적 (FR → To-Do → Test ID)

| FR | To-Do (1행위) | Test ID | Track | 상태 |
|----|---------------|---------|-------|------|
| FR-LOC-01 | G1에서 빈칸 2곳 좌표 찾기 | **D-LOC-01** | Logic | GREEN |
| FR-SOL-01 | G1 Step A 성공 반환 | **D-SOL-01** | Logic | GREEN + golden |
| FR-VAL-02 | (2,2)=7로 R2·C2 합 35 fail 보고 | **T2** | Logic | RED |
| FR-VAL-03 | 빈칸 있으면 incomplete | **T3** | Logic | 예정 |
| FR-MIS-01 | G1 없는 숫자 `[7,10]` | **D-MIS-01** | Logic | 예정 |
| FR-IN-01 | None → E003 | **U-IN-01** | UI | 설계 |
| FR-IN-02 | 3×4 → E001 | **U-IN-02** | UI | 설계 |
| FR-IN-03 | 빈칸 0개 → E002 | **U-IN-03** | UI | 설계 |

---

## 8. 픽스처 SSOT

### G1 (`grid_g1`)

```
[16,  3,  2, 13]
[ 5,  6,  0, 11]   ← (2,3)=0
[ 9, 10,  7,  8]
[ 4, 15, 14,  0]   ← (4,4)=0
```

- `find_blank_coords(G1)` → `[(2,3),(4,4)]` (**AC-LOC-01**)
- `find_not_exist_nums(G1)` → `[7, 10]` (**AC-MIS-01**)

> 초기 MomTest 스케치 `(2,2),(3,3)`은 **G1 픽스처 확정 후 `(2,3),(4,4)`로 정정**했다.

---

## 9. Dual-Track · ECB

| Track | 경로 | Mock | E emit | 계약 |
|-------|------|------|--------|------|
| **Logic** | `tests/entity/`, `src/entity/` | 금지 | 금지 | INV-* |
| **UI** | `tests/boundary/` | 허용 | 허용 | E-*, AC-IN/OUT/FLOW |

**규칙:** ID 없는 동작은 구현하지 않는다. GREEN 구현 줄에는 충족한 `INV-*` / `E-*`를 주석으로 단다.

---

*본 문서는 `docs/PRD.md` — MagicSquare_1004 MomTest Discovery 기반 PRD (INV · E · AC 포함)입니다.*
