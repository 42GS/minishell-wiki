## 📋 변경 사항 요약 (Summary)
<!-- 이번 PR에서 변경된 핵심 내용을 간결하게 작성해주세요. -->

## 🔗 관련 이슈 (Related Issues)
<!-- Closes #이슈번호 형식으로 작성하여 머지 시 자동으로 이슈가 닫히도록 해주세요. -->
- Closes #

## 💡 아키텍처 및 구현 의도 (Architecture & Design Rationale)
<!-- 기술적인 결정 이유(Why)와 대안 대비 선택 이유를 기술해주세요. -->
- **선택한 설계**: 
- **트레이드오프 및 고려사항**: 

## 🧪 테스트 및 품질 검증 결과 (Verification Results)
<!-- 로컬 및 테스트 슈트 검증 결과를 명시해주세요. -->

### 1. 기능 및 Bash 호환성 검증
```text
<테스트 케이스 실행 결과 로그 또는 통과 목록>
```

### 2. 메모리 및 파일 디스크립터(FD) 누수 검증
- [ ] **Valgrind / Leaks 검사 통과**: `definitely lost: 0 bytes`, `indirectly lost: 0 bytes`
- [ ] **열린 파일 디스크립터(FD) 검사 통과**: `0(stdin)`, `1(stdout)`, `2(stderr)` 외 잔여 열린 FD 없음

### 3. 코드 컨벤션
- [ ] **42 Norminette 통과**: `norminette src/ include/` 에러 0건
- [ ] **엄격 컴파일 플래그 통과**: `cc -Wall -Wextra -Werror` 경고 0건

## 📸 스크린샷 또는 데모 (선택 사항)
