# Refactor Smell — 스멜 탐지 (Refine ⑤)

`/refactor-smell` **만** 입력. 추가 인자·질문 **금지** — `src/`·`tests/` 정적 분석만.

## SSOT
- `.cursorrules` · `docs/PRD.md`

## Skill
**magic-square-tdd** Skill 자동 따름.

## 전제 (미충족 시 중단)
```
python -m pytest tests/ -v
```
**전부 PASS** 아니면 실패 테스트명·원인 한 줄만 보고하고 **종료**.

## 필수 선언 (응답 첫 줄)
```
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```

## 절차
1. pytest 전부 PASS 확인.
2. 스멜 탐지 (수정 없음).
3. 스멜 표 + `/refactor-safe` 후보 1~3.
4. 다음 안내.

## 스멜 유형
Long Method · Duplicated Code · Mysterious Name · Magic Number · ECB 위반 · Feature Envy

## 우선순위
| P | 기준 |
|---|------|
| P0 | SSOT·ECB·회귀 위험 |
| P1 | 중복·Long Method |
| P2 | 네이밍 |

## Change Budget (refactor-safe 1회)
파일 ≤3 · 클래스 ≤1 · 메서드 ≤3

## 출력
1. `pytest tests/ -v → N passed`
2. 스멜 표 (P \| 유형 \| 위치 \| 요약)
3. refactor-safe 후보 1~3 (Budget 포함)
4. `P0 후보 1개를 골라 /refactor-safe 를 실행하세요.`

## 금지
- 코드 수정 · commit · FAIL 시 스멜 표 · 질문

## 완료 (마지막 줄)
```
/refactor-safe 실행 대기 (P0 1개 선택)
```
