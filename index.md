# Minishell LLM Wiki Index

> **Minishell Knowledge Base Catalog**  
> 모든 위키 문서의 목록과 카테고리별 요약 및 상호 참조 링크입니다.

---

## 1. System Specifications & Schemas (설계 및 스키마)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [[CLAUDE|CLAUDE.md]] | 위키 스키마 규격, 백엔드 포트폴리오 엔지니어링 표준, 운영 프로토콜 및 구버전 봉인 원칙 | [[CLAUDE]] |
| [[log|log.md]] | 위키 작업 히스토리 시계열 저널 (Ingest / Query / Lint / Refactor) | [[log]] |

---

## 2. Requirements & Evaluation (요구사항 및 평가 분석)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [[wiki/requirements/mandatory|mandatory.md]] | 42 서브젝트 v7.1 기준 필수(Mandatory) 과제 요구사항 정밀 분석 및 제약조건 | [[wiki/requirements/mandatory|Mandatory Spec]] |
| [[wiki/requirements/bonus|bonus.md]] | 보너스 과제 정밀 분석 (`&&`, `\|\|`, `( )` 서브셸 우선순위, 와일드카드 `*` Globbing) | [[wiki/requirements/bonus|Bonus Spec]] |
| [[wiki/requirements/evaluation_matrix|evaluation_matrix.md]] | 42evalhub 평가 시트 항목별 1:1 매핑 검증 체크리스트 및 방어 전략 | [[wiki/requirements/evaluation_matrix|Evaluation Matrix]] |

---

## 3. Core Concepts & Deep Dive (핵심 이론 및 심화 학습)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [[wiki/concepts/deep_dive_lexer_parser_ast|deep_dive_lexer_parser_ast.md]] | **[심화 1]** 왜 단순 split은 실패하는가? 오토마타(DFA), 문맥 자유 문법(CFG), 재귀 하향 파싱 및 확장 타이밍 논리 | [[wiki/concepts/deep_dive_lexer_parser_ast|Deep Dive: Parser & CFG]] |
| [[wiki/concepts/deep_dive_process_ipc_and_fd|deep_dive_process_ipc_and_fd.md]] | **[심화 2]** `fork()` 커널 메모리 모델(CoW), FD 테이블 3단계 구조, 파이프라인 무한 행(Deadlock)과 EOF 법칙 | [[wiki/concepts/deep_dive_process_ipc_and_fd|Deep Dive: Process & FD]] |
| [[wiki/concepts/deep_dive_signals_and_concurrency|deep_dive_signals_and_concurrency.md]] | **[심화 3]** 비동기 시그널(Signal)과 Self-Deadlock의 원리, `volatile sig_atomic_t`의 본질, 포그라운드 프로세스 그룹 제어 | [[wiki/concepts/deep_dive_signals_and_concurrency|Deep Dive: Signals & Concurrency]] |
| [[wiki/concepts/allowed_functions_matrix|allowed_functions_matrix.md]] | 허용 외부 함수 53종 전수 분석, Async-Signal-Safe 판정 및 FD/메모리 주의점 | [[wiki/concepts/allowed_functions_matrix|Allowed Functions Matrix]] |

---

## 4. System Architecture Specifications (시스템 아키텍처 상세 설계)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [[wiki/architecture/01_parser_and_ast|01_parser_and_ast.md]] | **[설계 1]** Lexer/Tokenizer DFA 규칙, EBNF 정형 문법, C 언어 AST 데이터 구조체 및 재귀 하향 파서 | [[wiki/architecture/01_parser_and_ast|Phase 1: Parser & AST Architecture]] |
| [[wiki/architecture/02_execution_engine_and_ipc|02_execution_engine_and_ipc.md]] | **[설계 2]** AST 트리 순회 디스패처, 파이프라인 병렬 IPC 실행 엔진, FD 라이프사이클 및 종료 상태 수집 | [[wiki/architecture/02_execution_engine_and_ipc|Phase 2: Execution Engine & IPC]] |
| [[wiki/architecture/03_signal_dispatcher_and_state_machine|03_signal_dispatcher_and_state_machine.md]] | **[설계 3]** 단일 전역 변수(`g_signal_num`) 격리, 3대 셸 시그널 상태 머신 및 터미널 에코 제어(`termios`) | [[wiki/architecture/03_signal_dispatcher_and_state_machine|Phase 3: Signal Dispatcher Architecture]] |

---

## 5. Raw Sources Registry (불변 원문 소스 보관소)

| 분류 | 소스 명 | 설명 | 위키 링크 |
| :--- | :--- | :--- | :--- |
| **과제 명세** | `raw/subject/en.subject.md` | 공식 과제 PDF 무손실 추출 텍스트 마크다운 | [[raw/subject/en.subject|Subject Text]] |
| **평가 기준** | `raw/evalhub/minishell_eval_scale.md` | 42evalhub 파싱 및 마크다운 구조화 문서 | [[raw/evalhub/minishell_eval_scale|EvalHub Scale Text]] |
| **셸 표준** | `raw/specs/bash_quoting.md` | Bash Quoting (따옴표) 명세 원문 | [[raw/specs/bash_quoting|Bash Quoting Spec]] |
| **셸 표준** | `raw/specs/bash_pipelines.md` | Bash Pipelines (`\|`) 및 서브셸 명세 원문 | [[raw/specs/bash_pipelines|Bash Pipelines Spec]] |
| **셸 표준** | `raw/specs/bash_lists.md` | Bash Lists (`&&`, `\|\|`) 연산자 명세 원문 | [[raw/specs/bash_lists|Bash Lists Spec]] |
| **셸 표준** | `raw/specs/bash_compound_commands.md` | Bash Compound Commands (`( )`) 명세 원문 | [[raw/specs/bash_compound_commands|Bash Compound Commands Spec]] |
| **셸 표준** | `raw/specs/bash_expansions_and_wildcards.md` | Bash Parameter Expansion 및 Globbing (`*`) 명세 원문 | [[raw/specs/bash_expansions_and_wildcards|Bash Expansions Spec]] |
| **셸 표준** | `raw/specs/bash_redirections.md` | Bash Redirection (`<`, `>`, `>>`, `<<`) 명세 원문 | [[raw/specs/bash_redirections|Bash Redirections Spec]] |
| **셸 표준** | `raw/specs/bash_signals.md` | Bash Signals 및 Interactive Shell 동작 명세 원문 | [[raw/specs/bash_signals|Bash Signals Spec]] |
| **셸 표준** | `raw/specs/bash_exit_status.md` | Bash Exit Status 반환 규칙 명세 원문 | [[raw/specs/bash_exit_status|Bash Exit Status Spec]] |
| **셸 표준** | `raw/specs/bash_builtins.md` | Bash Builtin Utilities 명세 원문 | [[raw/specs/bash_builtins|Bash Builtins Spec]] |
