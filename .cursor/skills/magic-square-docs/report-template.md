# Report Template — `Report/NN.REPORT.md`

```markdown
# MagicSquare_1004 — {세션 주제}

| 항목 | 내용 |
|------|------|
| **프로젝트** | MagicSquare_1004 (세션 3) |
| **단계** | {RED | GREEN | REFACTOR | repeat} |
| **Phase** | {red|green|refactor} \| Layer \| Track |
| **Test ID** | … |
| **Command** | … |
| **보고서 생성일** | YYYY-MM-DD |
| **목적** | … |

---

## 1. 요약
- …

## 2. 핵심 결정·산출물

### STEP: RED
| Test ID | pytest | 변경 |

### STEP: GREEN
| PASS ID | src/ | golden |

### STEP: REFACTOR
| 스멜 | Budget | 실행 여부 |

### STEP: repeat
| 완료 사이클 | 다음 RED 후보 |

## 3. pytest · git (실측)
{터미널 출력 — 미실행 시 "미실행"}

## 4. 다음 단계
1. …

---
관련 Transcript: [Prompting/NN.Export-Transcript.md](../Prompting/NN.Export-Transcript.md)
*본 문서는 Report/NN.REPORT.md — …입니다.*
```

Phase별 STEP: RED only→RED / GREEN only→GREEN / repeat→전체+repeat
