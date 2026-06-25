---
name: magic-square-tdd
description: >-
  MagicSquare_1004 Dual-Track ARRR TDD (C2C, pytest). Use when Phase is red,
  green, or refactor; when invoking /red-test-plan, /red-skeleton, /tdd-red,
  /green-minimal, /golden-master, /refactor-smell, or /refactor-safe; or when
  the user mentions TDD, RED, GREEN, REFACTOR, Dual-Track, C2C, pytest.fail,
  validate_lines, or Magic Square. Commands work slash-only without extra input.
disable-model-invocation: true
---

# MagicSquare TDD Skill

C2C × Dual-Track TDD — **슬래시 Command만**으로 동작 (추가 입력·질문 금지).

## SSOT
- `.cursorrules` · `docs/PRD.md`

## 1. ARRR ↔ TDD

| ARRR | TDD | Command |
|------|-----|---------|
| ③ Ask | RED | `/red-test-plan` → `/red-skeleton` → `/tdd-red` |
| ④ Respond | GREEN | `/green-minimal` → `/golden-master` |
| ⑤ Refine | REFACTOR | `/refactor-smell` → `/refactor-safe` |
| ⑥ Repeat | 다음 RED | `/red-test-plan` |

## 2. Phase 선언 (첫 줄)

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
Phase: green | Layer: {entity|boundary} | Track: {Logic|UI}
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```

## 3. C2C Rule 1~3
1. 판단·규칙만 To-Do
2. 1 To-Do : 1 Test Case
3. RED → FAIL 확인 → GREEN

## 4. RED 금지
`src/` · skip/xfail · assert 완화 · Logic Track Mock · E00* emit · GREEN 진입

## 5. GREEN
1 RED 묶음 = 1 구현 · 1 commit *(요청 시)* · constants SSOT (`src/entity/constants.py`)

## 6. REFACTOR
pytest 전부 PASS · Budget(파일≤3·메서드≤3) · golden matched 유지

## 7. Track A vs B

| | UI (boundary) | Logic (entity) |
|---|---------------|----------------|
| ID | `U-*` | `D-*` |
| Mock | 허용 | 금지 |
| E00* | 허용 | 금지 |
| 경로 | `tests/boundary/` | `tests/entity/` |

## 8. Command 체인

```
/red-test-plan → /red-skeleton → /tdd-red → /green-minimal → /golden-master
→ /refactor-smell → /refactor-safe → (repeat)
```

## 9. pytest 패턴

```bash
pytest tests/entity/test_*.py -v
python -m pytest tests/ -v
UPDATE_GOLDEN=1 pytest tests/entity/test_*.py::{fn} -v
```

## 10. 보고 형식
- RED: Test ID · FAIL · `tests/` only
- GREEN: PASS ID · `src/` · pytest
- Golden: 경로 · matched
- REFACTOR: 스멜 · Budget · pytest · golden

## 도메인 Quick Reference
4×4 · `0` 빈칸 · 1~16 · 마법상수 34 · 10선 R1~R4 C1~C4 D1 D2  
`validate_lines` → `{status, failed_lines}` · incomplete→`failed_lines=[]`  
좌표 1-index row-major · 한국어 · git commit 요청 시만
