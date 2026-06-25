---
name: magic-square-docs
description: >-
  MagicSquare_1004 Report and Transcript export. Use for /export-session, Report
  Export, Transcript, Phase repeat, ARRR cycle reports, or session N docs.
  SSOT Report/NN.REPORT.md and Prompting/NN.Export-Transcript.md. Slash-only,
  no extra questions.
disable-model-invocation: true
---

# MagicSquare Docs Skill

`/export-session` **만** 입력. **magic-square-docs** checklist 필수.

> Export 요청 시 본 Skill 로드 후 [phase-checklist.md](phase-checklist.md) 수행.

## SSOT
- `.cursorrules` · `docs/PRD.md` · [.cursor/commands/export-session.md](../../commands/export-session.md)

## SSOT 경로

| 유형 | 형식 |
|------|------|
| Report | `Report/NN.REPORT.md` |
| Transcript | `Prompting/NN.Export-Transcript.md` |
| NN | `max(Report, Prompting) + 1` (두 자리) |

## 워크플로 (슬래시만 — 질문 금지)

### Step A — 입력 수집 (실행·기록)
```bash
git status --short
python -m pytest tests/ -v
```
+ Phase · Test ID · Command · 세션 주제 (채팅 자동)

### Step B — NN
`Report/NN.*` · `Prompting/NN.*` → max+1

### Step C — Report
[report-template.md](report-template.md) · Phase별 STEP (RED/GREEN/REFACTOR/repeat)

### Step D — Transcript
[transcript-template.md](transcript-template.md) · User/Cursor 전문 · `_Source uuid`

### Step E — README
있으면 세션 표 1행 · 없으면 "README 미존재"

### Step F — 완료 보고
`Report/NN.REPORT.md` · `Prompting/NN.Export-Transcript.md` · 한 줄 요약

## ARRR repeat 보고
RED · GREEN · REFACTOR · Golden · pytest 실측 · 다음 Ask(RED) 후보 1~3

## 금지
- commit · UPDATE_GOLDEN 임의 · 미실측 pytest/git 기재 · 질문 · NN 덮어쓰기

## 참고
- [phase-checklist.md](phase-checklist.md)
- [report-template.md](report-template.md)
- [transcript-template.md](transcript-template.md)

## 언어
한국어 (코드·경로·pytest 출력 원문)
