# Minishell LLM Wiki Log

All changes, ingests, queries, and maintenance operations on the wiki are chronologically tracked below.

Format: `## [YYYY-MM-DD] <Operation> | <Title>`

---

## [2026-11-22] init | Minishell LLM Wiki Bootstrap & Raw Sources Ingestion
- **Context**: 42 Minishell 과제 수행을 위한 LLM Wiki 아키텍처 셋업 및 백엔드 포트폴리오 수준의 시스템 엔지니어링 표준 구축.
- **Raw Sources Ingestion**:
  - `raw/subject/en.subject.pdf` 아카이빙 및 `raw/subject/en.subject.md` 무손실 텍스트 추출 (v7.1).
  - 42evalhub 평가 시트 수집: `raw/evalhub/minishell_eval_scale.html` 확보 및 `raw/evalhub/minishell_eval_scale.md` 마크다운 변환 완료.
  - 허용 외부 함수 53종 공식 man page 전수 추출: `raw/manpages/*.txt` (GNU Readline/History 포함).
  - GNU Bash Reference Manual 및 핵심 사양 9대 섹션(`bash_quoting`, `bash_pipelines`, `bash_lists`, `bash_compound_commands`, `bash_expansions_and_wildcards`, `bash_redirections`, `bash_signals`, `bash_exit_status`, `bash_builtins`) 원문 추출 완료.
- **Wiki Synthesis**:
  - `wiki/requirements/mandatory.md`: 필수 과제 요구사항 및 단일 전역 변수(시그널 전용) 제약 정밀 명세.
  - `wiki/requirements/bonus.md`: 보너스(`&&`, `||`, `( )`, `*`) 요구사항 및 AST/서브셸 아키텍처 요건 명세.
  - `wiki/requirements/evaluation_matrix.md`: 42evalhub 1:1 매핑 평가 체크리스트 작성.
  - `wiki/concepts/allowed_functions_matrix.md`: 53종 허용 함수 시그널 안전성 및 리소스 누수 위험도 매트릭스 작성.
- **Constraints Recorded**:
  - `minishell-old.git` 구버전 코드는 현재 설계/구현 단계에서 절대 참조하지 않음. 최종 완성 후 정량적/정성적 비교 회고 시에만 활용.
