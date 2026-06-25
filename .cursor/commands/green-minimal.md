# GREEN Minimal — 최소 구현 (Respond=GREEN ④)

`/green-minimal` **만** 입력. 추가 인자·질문 **금지** — 채팅·`tests/` FAIL·플랜에서 RED 묶음 1개 자동 추출.

## SSOT
- `.cursorrules` · `docs/PRD.md` · 직전 RED 플랜·테스트

## Skill
**magic-square-tdd** Skill 자동 따름.

## 자동 추출
- **RED 묶음 Test ID 1개** — 최근 FAIL 테스트 또는 미 GREEN 첫 ID
- Layer · Track · 대상 `src/` 모듈

## 필수 선언 (응답 첫 줄)
```
Phase: green | Layer: entity | Track: Logic
```
boundary → `Phase: green | Layer: boundary | Track: UI`

## 절차
1. 대상 Test ID pytest **FAIL** 재확인.
2. `src/` **최소 구현** (이번 묶음만).
3. `pytest.fail`→assert · When 해제 *(의도 불변)*.
4. pytest **PASS** + 회귀(같은 파일).
5. 보고.

## 상수 SSOT
- 구현: `src/entity/constants.py` — `MAGIC_CONSTANT`, `GRID_SIZE`, `MAX_NUM`, `BLANK`
- 테스트: `tests/entity/constants.py`
- 리터럴 `34`/`16`/`4`/`0` 금지

## ECB
- entity: E001~E005 emit 금지 · boundary/control import 금지
- boundary: E00*·입력 검증 허용

## 수정 범위

| 허용 | 금지 |
|------|------|
| `src/` 이번 묶음 | 묶음 외 ID 동시 GREEN |
| `tests/` fail→assert | assert 완화 · REFACTOR |
| | skip/xfail · git commit *(요청 시만)* |

## pytest
```
pytest tests/entity/test_{file}.py::{함수} -v
pytest tests/entity/test_{file}.py -v
```

## 보고
- PASS Test ID · 변경 `src/`·`tests/` · pytest PASS (한 줄)

## 금지
- 1 RED 묶음 초과 · REFACTOR · commit 임의 · 질문

## 완료 (마지막 줄)
```
/golden-master 또는 다음 RED 묶음 준비됐다
```
