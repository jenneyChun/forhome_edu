# RED Skeleton — pytest.fail 스켈레톤 (Ask=RED ④)

`/red-skeleton` **만** 입력. 추가 인자·질문 **금지** — 직전 `/red-test-plan` 블록 3·채팅에서 자동 추출.

## SSOT
- `.cursorrules` · 직전 `/red-test-plan` 출력 · `docs/PRD.md`

## Skill
**magic-square-tdd** Skill 자동 따름.

## 자동 추출
- Test ID · 파일 경로 · 함수명 · Given/Then · 픽스처(`grid_g0`/`grid_g1`)

## 필수 선언 (응답 첫 줄)
```
Phase: red | Layer: entity | Track: Logic
```
boundary → `Phase: red | Layer: boundary | Track: UI`

## 절차
1. 플랜 블록 3 확인.
2. `tests/` 에 스켈레톤·conftest·constants(필요 시) 작성.
3. **Then** = `pytest.fail("RED: {ID} — …")` **한 줄만**.
4. pytest → **FAIL** 확인.
5. 보고.

## AAA

| 구간 | 허용 | 금지 |
|------|------|------|
| Given | 픽스처·변수 | Domain 호출 |
| When | 함수명 **주석** | `execute()`/`find_*()` 호출 |
| Then | `pytest.fail` 1줄 | assert · pass |

## 상수
- `34`/`16`/`4` 리터럴 금지 → `tests/entity/constants.py`
- `src/` 수정 금지

## conftest
- `tests/conftest.py` — `grid_g1`: 4×4, `0` 두 개, row-major 1-based

## pytest
```
pytest tests/entity/test_{모듈}.py -v
```

## 보고
- Test ID · pytest FAIL (한 줄) · 변경 `tests/` 목록

## 금지
- `src/` · assert · skip/xfail · GREEN · 플랜 없이 ID invent · 질문

## 완료 (마지막 줄)
```
/tdd-red 로 assert RED 전환 준비됐다
```
