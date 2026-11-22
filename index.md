# Minishell LLM Wiki Index

> **Minishell Knowledge Base Catalog**  
> 모든 위키 문서의 목록과 카테고리별 요약 및 상호 참조 링크입니다.

---

## 1. System Specifications & Schemas (설계 및 스키마)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [CLAUDE.md](CLAUDE.md) | 위키 스키마 규격, 백엔드 포트폴리오 엔지니어링 표준, 운영 프로토콜 및 구버전 봉인 원칙 | [CLAUDE](CLAUDE.md) |
| [log.md](log.md) | 위키 작업 히스토리 시계열 저널 (Ingest / Query / Lint / Refactor) | [log](log.md) |

---

## 2. Engineering Process & GitHub Infrastructure (프로세스 및 깃허브 인프라)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [github_engineering_standards.md](wiki/process/github_engineering_standards.md) | **[포트폴리오 전략]** GitHub Flow, Conventional Commits, 마일스톤/라벨, Issue/PR 템플릿, CI 자동화 파이프라인 | [GitHub Engineering Standards](wiki/process/github_engineering_standards.md) |
| [roadmap_and_issues.md](wiki/process/roadmap_and_issues.md) | **[로드맵 & 이슈]** 42GS/minishell 17개 GitHub 이슈 및 마일스톤(M1~M5) 추적 매핑 테이블 | [Roadmap & Issues](wiki/process/roadmap_and_issues.md) |

---

## 3. Requirements & Evaluation (요구사항 및 평가 분석)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [mandatory.md](wiki/requirements/mandatory.md) | 42 서브젝트 v7.1 기준 필수(Mandatory) 과제 요구사항 정밀 분석 및 제약조건 | [Mandatory Spec](wiki/requirements/mandatory.md) |
| [bonus.md](wiki/requirements/bonus.md) | 보너스 과제 정밀 분석 (`&&`, `&#124;&#124;`, `( )` 서브셸 우선순위, 와일드카드 `*` Globbing) | [Bonus Spec](wiki/requirements/bonus.md) |
| [evaluation_matrix.md](wiki/requirements/evaluation_matrix.md) | 42evalhub 평가 시트 항목별 1:1 매핑 검증 체크리스트 및 방어 전략 | [Evaluation Matrix](wiki/requirements/evaluation_matrix.md) |

---

## 4. Core Concepts & Deep Dive (핵심 이론 및 심화 학습)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [deep_dive_lexer_parser_ast.md](wiki/concepts/deep_dive_lexer_parser_ast.md) | **[심화 1]** 왜 단순 split은 실패하는가? 오토마타(DFA), 문맥 자유 문법(CFG), 재귀 하향 파싱 및 확장 타이밍 논리 | [Deep Dive: Parser & CFG](wiki/concepts/deep_dive_lexer_parser_ast.md) |
| [deep_dive_process_ipc_and_fd.md](wiki/concepts/deep_dive_process_ipc_and_fd.md) | **[심화 2]** `fork()` 커널 메모리 모델(CoW), FD 테이블 3단계 구조, 파이프라인 무한 행(Deadlock)과 EOF 법칙 | [Deep Dive: Process & FD](wiki/concepts/deep_dive_process_ipc_and_fd.md) |
| [deep_dive_signals_and_concurrency.md](wiki/concepts/deep_dive_signals_and_concurrency.md) | **[심화 3]** 비동기 시그널(Signal)과 Self-Deadlock의 원리, `volatile sig_atomic_t`의 본질, 포그라운드 프로세스 그룹 제어 | [Deep Dive: Signals & Concurrency](wiki/concepts/deep_dive_signals_and_concurrency.md) |
| [deep_dive_builtins_and_environment.md](wiki/concepts/deep_dive_builtins_and_environment.md) | **[심화 4]** 프로세스 가상 메모리 `environ` 레이아웃, CoW 격리와 부모 실행 필연성, 64비트 오버플로 방어 수학 | [Deep Dive: Builtins & Env](wiki/concepts/deep_dive_builtins_and_environment.md) |
| [allowed_functions_matrix.md](wiki/concepts/allowed_functions_matrix.md) | 허용 외부 함수 53종 전수 분석, Async-Signal-Safe 판정 및 FD/메모리 주의점 | [Allowed Functions Matrix](wiki/concepts/allowed_functions_matrix.md) |

---

## 5. System Architecture Specifications (시스템 아키텍처 상세 설계)

| 문서 | 설명 | 위키 링크 |
| :--- | :--- | :--- |
| [01_parser_and_ast.md](wiki/architecture/01_parser_and_ast.md) | **[설계 1]** Lexer/Tokenizer DFA 규칙, EBNF 정형 문법, C 언어 AST 데이터 구조체 및 재귀 하향 파서 | [Phase 1: Parser & AST Architecture](wiki/architecture/01_parser_and_ast.md) |
| [02_execution_engine_and_ipc.md](wiki/architecture/02_execution_engine_and_ipc.md) | **[설계 2]** AST 트리 순회 디스패처, 파이프라인 병렬 IPC 실행 엔진, FD 라이프사이클 및 종료 상태 수집 | [Phase 2: Execution Engine & IPC](wiki/architecture/02_execution_engine_and_ipc.md) |
| [03_signal_dispatcher_and_state_machine.md](wiki/architecture/03_signal_dispatcher_and_state_machine.md) | **[설계 3]** 단일 전역 변수(`g_signal_num`) 격리, 3대 셸 시그널 상태 머신 및 터미널 에코 제어(`termios`) | [Phase 3: Signal Dispatcher Architecture](wiki/architecture/03_signal_dispatcher_and_state_machine.md) |
| [04_builtins_and_env_table.md](wiki/architecture/04_builtins_and_env_table.md) | **[설계 4]** 7대 빌트인 정밀 명세, 단일 빌트인 FD 백업/복원 프로토콜, 환경변수 딕셔너리 및 `envp` 직렬화 | [Phase 4: Builtins & Env Architecture](wiki/architecture/04_builtins_and_env_table.md) |

---

## 6. Raw Sources Registry (불변 원문 소스 보관소)

| 분류 | 소스 명 | 설명 | 위키 링크 |
| :--- | :--- | :--- | :--- |
| **과제 명세** | `raw/subject/en.subject.md` | 공식 과제 PDF 무손실 추출 텍스트 마크다운 | [Subject Text](raw/subject/en.subject.md) |
| **평가 기준** | `raw/evalhub/minishell_eval_scale.md` | 42evalhub 파싱 및 마크다운 구조화 문서 | [EvalHub Scale Text](raw/evalhub/minishell_eval_scale.md) |
| **셸 표준** | `raw/specs/bash_quoting.md` | Bash Quoting (따옴표) 명세 원문 | [Bash Quoting Spec](raw/specs/bash_quoting.md) |
| **셸 표준** | `raw/specs/bash_pipelines.md` | Bash Pipelines (`&#124;`) 및 서브셸 명세 원문 | [Bash Pipelines Spec](raw/specs/bash_pipelines.md) |
| **셸 표준** | `raw/specs/bash_lists.md` | Bash Lists (`&&`, `&#124;&#124;`) 연산자 명세 원문 | [Bash Lists Spec](raw/specs/bash_lists.md) |
| **셸 표준** | `raw/specs/bash_compound_commands.md` | Bash Compound Commands (`( )`) 명세 원문 | [Bash Compound Commands Spec](raw/specs/bash_compound_commands.md) |
| **셸 표준** | `raw/specs/bash_expansions_and_wildcards.md` | Bash Parameter Expansion 및 Globbing (`*`) 명세 원문 | [Bash Expansions Spec](raw/specs/bash_expansions_and_wildcards.md) |
| **셸 표준** | `raw/specs/bash_redirections.md` | Bash Redirection (`<`, `>`, `>>`, `<<`) 명세 원문 | [Bash Redirections Spec](raw/specs/bash_redirections.md) |
| **셸 표준** | `raw/specs/bash_signals.md` | Bash Signals 및 Interactive Shell 동작 명세 원문 | [Bash Signals Spec](raw/specs/bash_signals.md) |
| **셸 표준** | `raw/specs/bash_exit_status.md` | Bash Exit Status 반환 규칙 명세 원문 | [Bash Exit Status Spec](raw/specs/bash_exit_status.md) |
| **셸 표준** | `raw/specs/bash_builtins.md` | Bash Builtin Utilities 명세 원문 | [Bash Builtins Spec](raw/specs/bash_builtins.md) |
