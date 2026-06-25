# Phase Checklist — Export (`/export-session`)

**슬래시만** — 추가 입력·질문 금지.

## Step A — 수집 (실행 필수)
- [ ] `git status --short` → Report §3
- [ ] `python -m pytest tests/ -v` → Report·Transcript
- [ ] Phase · Test ID · Command · 주제 (채팅 자동)

## Step B — NN
- [ ] `Report/NN.*` · `Prompting/NN.*` max+1 · 덮어쓰기 없음

## Step C — Report
- [ ] [report-template.md](report-template.md) → `Report/NN.REPORT.md`

## Step D — Transcript
- [ ] [transcript-template.md](transcript-template.md) → `Prompting/NN.Export-Transcript.md`

## Step E — README
- [ ] 있으면 표 1행 / 없으면 "README 미존재"

## Step F — 보고
- [ ] 경로 2개 · NN · 한 줄 요약

## 금지
- [ ] commit · UPDATE_GOLDEN 임의 · 미실측 기재 · 질문
