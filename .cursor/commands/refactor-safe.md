# Refactor Safe — Safe Refactor 1건 (Refine ⑤)

`/refactor-safe` **만** 입력. 추가 인자·질문 **금지** — 직전 `/refactor-smell` **P0 후보 #1** 자동 선택.

## SSOT
- `.cursorrules` · 직전 `/refactor-smell` 표

## Skill
**magic-square-tdd** Skill 자동 따름.

## 전제
- `python -m pytest tests/ -v` **전부 PASS**
- refactor-smell 후보 **1건** (P0 우선)

## 자동 추출
- 스멜 유형 · 위치 · Budget — smell 표 #1 (P0 최상위)

## 필수 선언 (응답 첫 줄)
```
Phase: refactor | Layer: entity | Track: Logic
```

## Safe Refactor 원칙

| 허용 | 금지 |
|------|------|
| Extract · Rename · SSOT 통합 | 입출력·예외·1-index 변경 |
| 중복 제거 | E001~E005 emit · 기능 추가·BUGFIX |
| | assert·golden 수동 편집 |

## Budget
파일 ≤3 · 클래스 ≤1 · 메서드 ≤3 — 초과 시 **거부**

## 절차
1. P0 후보 1건 리팩터.
2. `python -m pytest tests/ -v` PASS.
3. golden 연결 시 `UPDATE_GOLDEN` 없이 **matched**.
4. diff: 의도적→ISS+`UPDATE_GOLDEN=1` / 비의도→**롤백**.
5. 보고.

## pytest
```
python -m pytest tests/ -v
```

## 보고
- 선택 스멜 · 변경 요약 · Budget · pytest · golden matched

## 금지
- 후보 2건+ · Budget 초과 · GREEN 혼입 · commit · 질문

## 완료 (마지막 줄)
```
/red-test-plan 또는 /export-session 준비됐다
```
