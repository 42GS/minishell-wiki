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

## [2026-11-22] design | Phase 1: Lexer, Parser & AST Architecture Design & Deep Dive
- **Context**: 1단계 문법 및 파서 아키텍처 설계와 사용자 학습을 위한 이론적 심화 개념 문서화.
- **Architectural Specifications Added**:
  - `wiki/architecture/01_parser_and_ast.md`: 어휘 분석 파이프라인, EBNF 정형 문법, C 구조체(`t_token`, `t_redir`, `t_ast_node`), 재귀 하향 파서 알고리즘, 구문 에러 규칙 및 트리 메모리 재귀 해제 전략.
- **Deep Dive Concepts Added**:
  - `wiki/concepts/deep_dive_lexer_parser_ast.md`: 왜 `ft_split`은 실패하는가, DFA 상태 머신 다이어그램, 촘스키 문법 계층(CFG)과 트리 구조의 필연성, 셔팅야드 vs 재귀 하향 파서 비교, 환경변수 조기 확장의 위험성과 POSIX 3단계 파이프라인.
- **Index Updated**: `index.md`에 아키텍처 및 딥다이브 섹션 반영.

## [2026-11-22] design | Phase 2: Execution Engine & IPC Pipeline Architecture & Deep Dive
- **Context**: 2단계 실행 엔진, 프로세스 생명주기 및 IPC 파이프라인 설계와 심화 OS 개념 문서화.
- **Architectural Specifications Added**:
  - `wiki/architecture/02_execution_engine_and_ipc.md`: AST 트리 순회 디스패처, 단일 빌트인의 부모 프로세스 FD 백업/원복 패턴, $N$개 명령어 파이프라인의 엄격한 Pipe-Close 프로토콜, 리다이렉션 테이블 순차 평가, `waitpid` 팬인 및 종료 상태 코드 정규화(128+N).
- **Deep Dive Concepts Added**:
  - `wiki/concepts/deep_dive_process_ipc_and_fd.md`: `fork()` 시 커널 PCB/CoW 메모리 모델, 파일 디스크립터 테이블 3단계(Process FD -> Open File Description -> VFS Inode) 포인터 구조, 파이프라인 무한 행(Deadlock)의 수학적 원인과 EOF 도달 조건, 좀비 프로세스 방지 및 Concurrency 보장 패턴.
- **Index Updated**: `index.md`에 Phase 2 문서 반영.
