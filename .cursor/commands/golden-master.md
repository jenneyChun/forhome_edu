# Golden Master — Approval Test (GREEN 후)

`/golden-master` **만** 입력. 추가 인자·질문 **금지** — 최근 PASS Test ID·golden 미연결 1개 자동 추출.

## SSOT
- `.cursorrules` · `tests/_approval.py` · `tests/golden/`

## Skill
**magic-square-tdd** Skill 자동 따름.

## 전제
- 대상 Test ID **pytest PASS** (`/green-minimal` 완료)

## 자동 추출
- PASS Test ID 1개 · 테스트 파일 · `assert_matches_golden` 미연결 우선

## 필수 선언 (응답 첫 줄)
```
Phase: green | Layer: entity | Track: Logic
```

## 절차
1. `tests/_approval.py` — `assert_matches_golden` *(없으면 생성)*.
2. `tests/golden/{id}.approved.txt` 연결 (`D-LOC-01`→`d-loc-01.approved.txt`).
3. `UPDATE_GOLDEN=1` pytest → 기준 생성.
4. `UPDATE_GOLDEN` 없이 pytest → **matched**.
5. 보고.

## 출력 포맷 (고정)
- 좌표: **1-index** row-major
- 에러: `"E00N NAME"` 문자열
- 직렬화: `repr()` + 개행 1개

## pytest
```
UPDATE_GOLDEN=1 pytest tests/entity/test_*.py::{함수} -v
pytest tests/entity/test_*.py::{함수} -v
```

## 보고
- Test ID · golden 경로 · matched/mismatch · diff 한 줄

## 금지
- golden **수동 편집** · `src/` 로직 변경 · 미 PASS 시 구축 · commit · 질문

## 완료 (마지막 줄)
```
/refactor-smell 또는 다음 RED 묶음 준비됐다
```
