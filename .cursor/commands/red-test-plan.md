# RED Test Plan — C2C 설계표·테스트 플랜 (Ask=RED ③)

`/red-test-plan` **만** 입력. 추가 인자·질문 **금지** — SSOT·채팅·Report에서 자동 추출.

## SSOT
- `.cursorrules` · `docs/PRD.md` · 채팅·`Report/`·`tests/`

## Skill
**magic-square-tdd** Skill 자동 따름.

## 자동 추출

| 항목 | 규칙 |
|------|------|
| Layer | domain→`entity` / 입력·E00*→`boundary` |
| Track | entity→`Logic` / boundary→`UI` |
| Test ID | entity `D-*` / boundary `U-*` — **미작성 첫 1개** |
| RED 묶음 | Test ID 1개 (Rule 2) |

PRD 비어 있으면 `.cursorrules` FR 대용 + `(PRD 미작성)` 명시.

## 필수 선언 (응답 첫 줄)
```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

## C2C Rule 1~3
1. 판단·규칙("~한다/허용한다")만 To-Do — 단순 행동 폐기
2. **1 To-Do : 1 Test Case**
3. RED 먼저 — GREEN·구현 언급 금지

## 절차
1. SSOT·채팅에서 Layer·Track·Test ID 확정.
2. **출력 4블록** 표 작성 (파일 생성 없음).
3. ECB·Mock 점검.
4. 완료 문구 출력.

## 출력 4블록

**블록 1 — C2C:** FR 인용 · To-Do 1개 · Test ID · Given/When/Then

**블록 2 — Track 설계표** (Test ID 1행)

| Track | 표 |
|-------|-----|
| Logic | Test ID \| 대상 함수 \| Given→Then \| Invariant \| Expected RED Failure |
| UI | Test ID \| Given \| Then \| Expected RED Failure |

**블록 3 — 테스트 플랜:** 파일 경로 · 함수명 · conftest · pytest 명령 · RED 묶음

**블록 4 — ECB·Mock:** Logic=Mock·E00* emit 금지 / UI=Mock·E00* 허용 → `PASS`/`FAIL`

## 금지
- `src/`·`tests/` 파일 생성·수정
- GREEN / REFACTOR · skip / xfail · 사용자에게 질문

## 완료 (마지막 줄)
```
/red-skeleton 으로 넘길 준비됐다
```
