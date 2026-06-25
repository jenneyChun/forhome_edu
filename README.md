# MagicSquare_1004 — Session 3

4×4 마방진 검증 도구. **C2C × Dual-Track TDD** (ARRR) 실습 프로젝트.

## 개요

| 항목 | 내용 |
|------|------|
| 도메인 | 4×4 격자 · 빈칸 `0` · 1~16 · 마법상수 `34` |
| API | `validate_lines(grid) → {status, failed_lines}` |
| 10선 | R1~R4 · C1~C4 · D1 · D2 |
| SSOT | [`.cursorrules`](.cursorrules) · [`docs/PRD.md`](docs/PRD.md) |

## ARRR ↔ TDD

| ARRR | TDD | Command |
|------|-----|---------|
| ③ Ask | RED | `/red-test-plan` → `/red-skeleton` → `/tdd-red` |
| ④ Respond | GREEN | `/green-minimal` → `/golden-master` |
| ⑤ Refine | REFACTOR | `/refactor-smell` → `/refactor-safe` |
| ⑥ Repeat | 다음 RED | `/red-test-plan` |

**C2C:** PRD → To-Do → Test Case (Rule 1~3)

## RED · GREEN 체크리스트

> 출처: [`docs/PRD.md`](docs/PRD.md) §2 INV · §3 E · §4 AC · [`docs/TESTPLAN.md`](docs/TESTPLAN.md) · ARRR Command  
> `[x]` 완료 · `[ ]` 미완 · `RED`/`GREEN` = 해당 Phase에서 할 일

### RED (Ask) — 공통 절차

- [ ] `/red-test-plan` — 대상 계약 1개 → Test ID · Given/When/Then (출력만)
- [ ] `/red-skeleton` — `tests/`에 AAA + `pytest.fail("RED: {ID}")`
- [ ] `/tdd-red` — assert RED 전환 · pytest **FAIL** 확인
- [ ] 수정 범위: **`tests/`만** · `src/` 금지 · skip/xfail/assert 완화 금지
- [ ] 상수 리터럴 금지 → `tests/entity/constants.py`
- [ ] 1 RED 묶음 = **Test ID 1개** (C2C Rule 2)

### RED — Logic Track (`tests/entity/`, INV · AC)

| 체크 | Test ID | 수용 조건 (AC) | 불변식 (INV) | RED에서 할 일 | 상태 |
|------|---------|----------------|--------------|---------------|------|
| [x] | **D-LOC-01** | AC-LOC-01 | INV-06 | G1 → `[(2,3),(4,4)]` assert | GREEN |
| [x] | **D-SOL-01** | AC-SOL-01 | INV-08 | Step A `success` + golden assert | GREEN |
| [x] | **T2** | AC-VAL-02 | INV-01, INV-05, INV-09 | R2·C2 합≠34 → `fail` + `failed_lines` assert | RED (assert) |
| [ ] | **T3** | AC-VAL-03 | INV-10 | 빈칸 있으면 `incomplete`, `failed_lines=[]` assert | 예정 |
| [ ] | **D-MIS-01** | AC-MIS-01 | INV-07, INV-11 | G1 → `[7,10]` 오름차순 assert | 예정 |
| [ ] | **D-VAL-01** | AC-VAL-01 | INV-01, INV-02 | G0 → `pass`, `failed_lines=[]` assert | 예정 |
| [ ] | *(예정)* | — | INV-04 | 셀 값 `0`·`1~16` 외 거부 assert *(entity 경로)* | 예정 |

**RED Logic 금지:** Domain Mock · E001~E005 emit · boundary import

**INV 커버 맵 (Logic RED 완료 시)**

| INV | RED Test ID | 비고 |
|-----|-------------|------|
| INV-01 | T2, D-VAL-01 | 선 합 34 |
| INV-02 | D-VAL-01 | 1~16 각 1회 |
| INV-03 | — | boundary E001 (UI Track) |
| INV-04 | D-MIS-01, D-VAL-01 | 셀 값 허용 범위 |
| INV-05 | T2 | 10선만 검증 |
| INV-06 | D-LOC-01 | ✅ |
| INV-07 | D-MIS-01 | 없는 숫자 |
| INV-08 | D-SOL-01 | ✅ |
| INV-09 | T2 | `failed_lines` ID 형식 |
| INV-10 | T3 | incomplete 시 `[]` |
| INV-11 | D-MIS-01 | 오름차순 |

### RED — UI Track (`tests/boundary/`, E · AC)

| 체크 | Test ID | 수용 조건 (AC) | 에러 (E) | RED에서 할 일 | 상태 |
|------|---------|----------------|----------|---------------|------|
| [ ] | **U-IN-01** | AC-IN-01 | E003 `INVALID_NULL` | `grid=None` → E003 포함 assert | 설계 |
| [ ] | **U-IN-02** | AC-IN-02 | E001 `INVALID_SIZE` | 3×4 → E001 포함 assert | 설계 |
| [ ] | **U-IN-03** | AC-IN-03 | E002 `INVALID_BLANKS` | 빈칸 0개 → E002 assert | 설계 |
| [ ] | **U-OUT-01** | AC-OUT-01 | — | G1 유효 입력 → 결과 dict 키 6개 assert | 예정 |
| [ ] | **U-FLOW-02** | AC-FLOW-01 | — | `grid=None` 시 domain `execute()` 0회 assert | 예정 |
| [ ] | *(예정)* | — | E004 `INVALID_VALUE` | `0`·`1~16` 외 셀 → E004 assert | 예정 |
| [ ] | *(예정)* | — | E005 `INVALID_DUPLICATE` | 1~16 중복 → E005 assert | 예정 |

**RED UI 허용:** Domain Mock · `pytest.fail` · Then에 `E00N` 명시

**E · AC 커버 맵 (UI RED 완료 시)**

| E | AC | Test ID |
|---|-----|---------|
| E001 | AC-IN-02 | U-IN-02 |
| E002 | AC-IN-03 | U-IN-03 |
| E003 | AC-IN-01 | U-IN-01 |
| E004 | *(예정)* | *(예정)* |
| E005 | *(예정)* | *(예정)* |
| — | AC-OUT-01 | U-OUT-01 |
| — | AC-FLOW-01 | U-FLOW-02 |

---

### GREEN (Respond) — 공통 절차

- [ ] RED 재확인 — 대상 Test ID pytest **FAIL**
- [ ] `/green-minimal` — **`src/` 최소 구현** (이번 RED 묶음만)
- [ ] 테스트 전환 — `pytest.fail` 제거 · When 실제 호출 · Then assert
- [ ] 상수 SSOT — `src/entity/constants.py` (`MAGIC_CONSTANT`, `GRID_SIZE`, `MAX_NUM`, `BLANK`)
- [ ] ECB — entity: **E001~E005 emit 금지** · boundary/control import 금지
- [ ] pytest **PASS** — 대상 테스트 + 같은 파일 회귀
- [ ] *(선택)* `/golden-master` — `tests/golden/{id}.approved.txt` matched
- [ ] 구현 줄 주석 — 충족한 `INV-*` / `E-*` ID 표기
- [ ] 금지: 묶음 외 ID 동시 해결 · REFACTOR · assert 완화 · git commit *(요청 시만)*

### GREEN — Logic Track (INV · AC 충족)

| 체크 | Test ID | 구현 대상 | 충족 계약 | GREEN에서 할 일 | 상태 |
|------|---------|-----------|-----------|-----------------|------|
| [x] | **D-LOC-01** | `find_blank_coords` | INV-06 · AC-LOC-01 | BLANK 셀 row-major·1-index 반환 | PASS |
| [x] | **D-SOL-01** | `solution_step_a` | INV-08 · AC-SOL-01 | Step `"A"`, `status="success"`, `blank_coords` | PASS + golden |
| [ ] | **T2** | `validate_lines` | INV-01, INV-05, INV-09 · AC-VAL-02 | 10선 합 검증 · fail + `failed_lines` | 미구현 |
| [ ] | **T3** | `validate_lines` | INV-10 · AC-VAL-03 | `BLANK` 있으면 `incomplete` + `failed_lines=[]` | 예정 |
| [ ] | **D-MIS-01** | `find_not_exist_nums` | INV-07, INV-11 · AC-MIS-01 | 없는 1~16 오름차순 반환 | 예정 |
| [ ] | **D-VAL-01** | `validate_lines` (pass) | INV-01, INV-02 · AC-VAL-01 | G0 → `pass` | 예정 |
| [ ] | *(예정)* | `validate_lines` / entity | INV-04 | 허용 값 외 처리 *(entity 경로)* | 예정 |

**`validate_lines` GREEN 우선순위 (PRD §2):**

1. [ ] `BLANK` ≥ 1 → `incomplete` + `failed_lines=[]` (**INV-10** · T3)
2. [ ] 빈칸 없음 → 10선 합 검증 (**INV-01**, **INV-05** · T2)
3. [ ] 빈칸 없음 → 1~16 각 1회 (**INV-02** · D-VAL-01)
4. [ ] `failed_lines` ID 형식 (**INV-09** · T2)

### GREEN — UI Track (E · AC 충족)

| 체크 | Test ID | 구현 대상 | 충족 계약 | GREEN에서 할 일 | 상태 |
|------|---------|-----------|-----------|-----------------|------|
| [ ] | **U-IN-01** | `execute` — null 가드 | E003 · AC-IN-01 | `grid=None` 시 E003 반환 · domain 미호출 | 예정 |
| [ ] | **U-IN-02** | `execute` — 크기 검증 | E001 · AC-IN-02 | 4×4 아니면 E001 | 예정 |
| [ ] | **U-IN-03** | `execute` — 빈칸 개수 | E002 · AC-IN-03 | 빈칸 ≠ 2개면 E002 | 예정 |
| [ ] | **U-OUT-01** | boundary 결과 형태 | AC-OUT-01 | G1 결과 dict 키 6개 고정 | 예정 |
| [ ] | **U-FLOW-02** | domain 호출 가드 | AC-FLOW-01 | invalid 입력 시 `execute()` 0회 | 예정 |
| [ ] | *(예정)* | `execute` — 값 검증 | E004 | 셀 값 범위 밖 → E004 | 예정 |
| [ ] | *(예정)* | `execute` — 중복 검증 | E005 | 1~16 중복 → E005 | 예정 |

**ECB (GREEN 시):** `src/entity/`는 E emit 금지 · `src/` boundary만 E001~E005 반환

### AC 전체 추적표 (RED → GREEN)

| AC | 설명 | Track | Test ID | RED | GREEN |
|----|------|-------|---------|-----|-------|
| AC-VAL-01 | G0 → `pass` | Logic | D-VAL-01 | [ ] | [ ] |
| AC-VAL-02 | 선 합≠34 → `fail` + 선 ID | Logic | T2 | [x] | [ ] |
| AC-VAL-03 | 빈칸 → `incomplete`, `[]` | Logic | T3 | [ ] | [ ] |
| AC-LOC-01 | G1 빈칸 좌표 | Logic | D-LOC-01 | [x] | [x] |
| AC-MIS-01 | G1 없는 숫자 `[7,10]` | Logic | D-MIS-01 | [ ] | [ ] |
| AC-SOL-01 | G1 Step A success | Logic | D-SOL-01 | [x] | [x] |
| AC-IN-01 | None → E003 | UI | U-IN-01 | [ ] | [ ] |
| AC-IN-02 | 3×4 → E001 | UI | U-IN-02 | [ ] | [ ] |
| AC-IN-03 | 빈칸 0개 → E002 | UI | U-IN-03 | [ ] | [ ] |
| AC-OUT-01 | G1 결과 dict 키 6개 | UI | U-OUT-01 | [ ] | [ ] |
| AC-FLOW-01 | None 시 domain 0회 | UI | U-FLOW-02 | [ ] | [ ] |

### 권장 RED 순서 (의존성)

```
D-LOC-01 ✅ → D-SOL-01 ✅ → T2 (RED) → T3 → D-MIS-01 → D-VAL-01
                                          ↓
                U-IN-01 → U-IN-02 → U-IN-03 → U-FLOW-02 → U-OUT-01
                                          ↓
                                E004 · E005 (예정)
```

## Cursor Commands

| Command | 역할 |
|---------|------|
| `/red-test-plan` | C2C 설계표·플랜 (출력만) |
| `/red-skeleton` | `pytest.fail` 스켈레톤 |
| `/tdd-red` | assert RED 테스트 |
| `/green-minimal` | 최소 구현 |
| `/golden-master` | Approval Test |
| `/refactor-smell` | 스멜 탐지 |
| `/refactor-safe` | Safe Refactor 1건 |
| `/export-session` | Report · Transcript Export |

## Skills

| Skill | 경로 |
|-------|------|
| magic-square-tdd | [`.cursor/skills/magic-square-tdd/SKILL.md`](.cursor/skills/magic-square-tdd/SKILL.md) |
| magic-square-docs | [`.cursor/skills/magic-square-docs/SKILL.md`](.cursor/skills/magic-square-docs/SKILL.md) |

## 프로젝트 구조

```
src/
  validate_lines.py      # API (TDD 진행 중)
  entity/                # Domain/Logic
tests/
  entity/                # Track B (D-*)
  boundary/              # Track A (U-*) — 예정
  golden/                # Approval Test
Report/                  # 세션 보고서
Prompting/               # Transcript
```

## pytest

```bash
python -m pytest tests/ -v
```

## 세션 문서

| NN | 주제 | Phase | Report | Transcript |
|----|------|-------|--------|------------|
| 01 | Harness·규칙·T2 RED | red | [Report](Report/01.harness-and-red-t2.md) | [Transcript](Prompting/01.harness-and-red-t2.md) |
| 02 | T2 validate_lines RED | red | [Report](Report/02.REPORT.md) | [Transcript](Prompting/02.Export-Transcript.md) |
| 03 | ARRR 1사이클·D-LOC-01 | repeat | [Report](Report/03.REPORT.md) | [Transcript](Prompting/03.Export-Transcript.md) |
| 04 | ARRR 인프라·Track A/B RED 설계 | red | [Report](Report/04.REPORT.md) | [Transcript](Prompting/04.Export-Transcript.md) |
| 05 | 세션 Export (Report 04·README) | docs | [Report](Report/05.REPORT.md) | [Transcript](Prompting/05.Export-Transcript.md) |
| 06 | D-LOC-01 RED 스켈레톤 | red | [Report](Report/06.REPORT.md) | [Transcript](Prompting/06.Export-Transcript.md) |

## 현재 TDD 상태

| Test ID | Track | 상태 |
|---------|-------|------|
| D-LOC-01 | Logic | GREEN |
| D-SOL-01 | Logic | GREEN + golden |
| T2 | Logic | RED (`validate_lines` 미구현) |
| T3 | Logic | 예정 |
| D-MIS-01 | Logic | 예정 |
| U-IN-01/02/03 | UI | 설계만 |
