---
name: "🐛 Bug Report"
about: "셸 실행 도중 발견된 결함, 크래시, 메모리/FD 릭 또는 Bash 동작 불일치"
title: "[BUG] "
labels: ["type:bug"]
assignees: ""
---

## 💥 버그 증상 요약 (Problem Description)
<!-- 어떤 문제가 발생했는지 간결하게 설명해주세요. -->

## 🔁 재현 단계 (Steps to Reproduce)
```bash
minishell$ <재현 명령어 입력>
```

## 🔍 기대 동작 vs 실제 동작 (Expected vs Actual Behavior)
- **Bash 기대 동작**: 
- **Minishell 실제 동작**: 

## 🩺 근본 원인 분석 (Root Cause Hypothesis)
<!-- 결함이 발생한 원인(메모리 해제 누락, 시그널 경쟁 상태, 파이프 미닫힘 등)을 분석해주세요. -->

## 🛡️ 검증 및 안전성 체크리스트 (Verification Checklist)
- [ ] 회귀 테스트(Regression Test) 케이스 추가 완료
- [ ] Valgrind / Leaks 누수 검증 완료
- [ ] 비정상 종료(Segfault, Bus Error) 방어 확인
