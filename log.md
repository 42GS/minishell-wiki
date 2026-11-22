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

## [2026-11-22] design | Phase 3: Signal Dispatcher & State Machine Architecture & Deep Dive
- **Context**: 3단계 비동기 시그널 디스패처, 상태 머신 설계 및 심화 시그널/동시성 개념 문서화.
- **Architectural Specifications Added**:
  - `wiki/architecture/03_signal_dispatcher_and_state_machine.md`: 단일 전역 변수(`volatile sig_atomic_t g_signal_num`) 격리, 3대 셸 상태 머신(`STATE_INTERACTIVE`, `STATE_EXECUTION`, `STATE_HEREDOC`), `sigaction` 핸들러 구현, 터미널 `termios` 에코 제어(`ECHOCTL`), 시그널-종료상태 동기화 프로토콜(130/131).
- **Deep Dive Concepts Added**:
  - `wiki/concepts/deep_dive_signals_and_concurrency.md`: 하드웨어 인터럽트에서 TTY 드라이버 거쳐 커널 트랩까지의 경로, 시그널 핸들러 내 `printf`/`malloc` 호출 시의 Self-Deadlock 메커니즘, `volatile sig_atomic_t`의 하드웨어/컴파일러적 의미, `EINTR`과 `SA_RESTART`의 트레이드오프, 포그라운드 프로세스 그룹 시그널 브로드캐스팅 제어.
- **Index Updated**: `index.md`에 Phase 3 문서 반영.

## [2026-11-22] lint | Full Wiki Lint & Mermaid Diagram Syntax Fix
- **Context**: 아키텍처 및 개념 문서 내 Mermaid 다이어그램 렌더링 깨짐 현상 전수 점검 및 린트 수정.
- **Root Causes Identified**:
  - `wiki/architecture/02_execution_engine_and_ipc.md`: 노드 라벨 내 `->` 연산자, `$?`, `==`, HTML `<br/>` 태그, 엣지 라벨 내 언쿼트 특수문자(`()`, `,`, `&`), 라벨 내 `<>` 태그 오인 문자로 인한 파서 충돌.
  - `wiki/concepts/deep_dive_lexer_parser_ast.md`: `stateDiagram-v2` 전이 라벨 내 작은따옴표(`'`), 큰따옴표(`"`), 파이프(`|`), 쉼표, 역슬래시(`\0`)로 인한 문법 에러.
  - `wiki/requirements/bonus.md`: 노드 라벨 내 `|` 파이프 문자로 인한 엣지 구분자 오인식.
  - `wiki/concepts/deep_dive_process_ipc_and_fd.md` & `CLAUDE.md`: `subgraph` 공백 미인용 및 HTML `<br/>` 태그 잔존.
  - `wiki/architecture/01_parser_and_ast.md`: 노드 라벨 내 특수문자 및 순환 그래프 에지 충돌.
- **Fixes Applied**:
  - 모든 HTML 태그(`<br/>`) 제거 및 간결한 표준 단일 텍스트로 치환.
  - 노드 라벨 내 `->`, `|`, `$?`, `()`, `<>` 특수문자를 안전한 텍스트로 교체.
  - `stateDiagram-v2` 전이 라벨을 표준 영문 식별자로 전면 수정.
  - `comprehensive_lint.py`를 작성하여 위키 전수 검증: 잔여 이슈 0건(Total issues found: 0) 달성.

## [2026-11-22] refactor | Transform All Links to Native Obsidian Wikilinks & Build 250-Edge Knowledge Graph
- **Context**: Obsidian Graph View에서 모든 노드가 연결선 없는 고아 노드로 표시되던 문제 해결 및 문서 간 지식 네트워크 구축.
- **Root Cause**: 모든 파일 참조가 외부 URL 형태인 `file:///Users/yong/...` 절대 경로로 작성되어 있어, Obsidian이 이를 로컬 볼트 내부 링크(Internal Link)로 인식하지 않고 외부 링크로 취급함.
- **Actions Taken**:
  - `file:///` 절대 경로 링크를 Obsidian 네이티브 위키링크(`[[target|alias]]`)로 전면 마이그레이션.
  - 모든 요구사항, 아키텍처, 딥다이브 개념, 평가 매트릭스, 허용 함수 및 스펙 원문 간의 2방향 시맨틱 상호 참조(Cross-reference) 네트워크 구축.
  - 마크다운 테이블 및 인용구 내 이스케이프 파이프(`\|`) 정규화로 미해결(Unresolved) 링크 0건 달성.
- **Graph Metrics Achieved**:
  - 총 문서 노드 (Nodes): **24개**
  - 총 위키링크 연결선 (Edges): **250개** (고아 노드 0개)
  - 미해결 링크 (Unresolved): **0개**
  - 핵심 허브 노드: `index.md`, `02_execution_engine_and_ipc.md`(43 백링크), `03_signal_dispatcher_and_state_machine.md`(30 백링크), `01_parser_and_ast.md`(20 백링크).

## [2026-11-22] fix | Resolve Markdown Table Column Mismatches and LaTeX Math Parser Collisions
- **Context**: Obsidian에서 마크다운 테이블이 깨져 보이고 수식 파서 충돌로 본문 텍스트가 깨지던 현상 전수 감사 및 수정.
- **Root Causes Identified**:
  - **테이블 열 분리자 파이프 충돌**: 마크다운 테이블 내부에서 위키링크 `[[target|alias]]`나 인라인 코드 내 파이프(`|`, `||`)를 사용할 경우 마크다운 파서가 이를 테이블 열(Column) 구분자로 파싱하여 헤더와 행의 컬럼 수가 어긋나 표가 붕괴됨.
  - **LaTeX 수식 파서 오인식**: 셸 변수(`&#36;?`, `&#36;VAR`, `&#36;USER`)가 문서 내 여러 번 등장할 때 마크다운 파서가 이를 인라인 LaTeX 수식으로 인식하여 사이의 본문 텍스트 전체를 수식으로 렌더링하고 레이아웃을 깨뜨림.
- **Fixes Applied**:
  - 모든 테이블 내부 위키링크를 파이프 없는 `[[target]]` 및 표준 마크다운 상대 링크 `[label](target.md)`로 교체.
  - 테이블 내부의 모든 파이프 문자를 HTML 엔티티 `&#124;`로 치환하여 테이블 컬럼 완벽 보존.
  - 셸 변수 표현의 `$`를 HTML 엔티티 `&#36;` 또는 정규 코드 스팬으로 격리하여 LaTeX 수식 충돌 0건 달성.
  - `audit_markdown.py` 전수 감사 결과: 테이블 불일치 0건, 수식 충돌 0건, 린트 에러 0건.

## [2026-11-22] feat | Establish Backend Portfolio GitHub Infrastructure & Standards
- **Context**: 백엔드 포트폴리오 엔지니어링 표준 수립 및 깃허브 관리 인프라(Issue/PR Templates, CI Pipeline) 구축.
- **Architectural Specifications Added**:
  - `wiki/process/github_engineering_standards.md`: 테크 기업 채용 관점 4대 가치, GitHub Flow 브랜치 전략, Conventional Commits 스펙/스코프, 5단계 마일스톤 및 4계층 라벨 체계, CI 품질 게이트웨이 사양.
- **Production Templates Created**:
  - `templates/github/ISSUE_TEMPLATE/01_feature_issue.md`: 스펙 기준 및 아키텍처 설계 중심 Feature Request 템플릿.
  - `templates/github/ISSUE_TEMPLATE/02_bug_issue.md`: 재현 스텝, 기대/실제 동작, 근본 원인 분석 중심 Bug Report 템플릿.
  - `templates/github/PULL_REQUEST_TEMPLATE.md`: 설계 의도(Why), 트레이드오프, Valgrind/FD 릭 제로 체크리스트 중심 PR 템플릿.
  - `templates/github/workflows/ci.yml`: Ubuntu 환경 Norminette, 엄격 빌드(-Wall -Wextra -Werror), No-relink 검사, Valgrind 메모리 릭 검증 자동화 파이프라인.
- **Index & Graph Updated**: `index.md`에 프로세스 섹션 추가 및 216개 상호 연결선 유지.

## [2026-11-22] refactor | Separate Dual-Repository Issue Architectures (minishell-wiki vs minishell)
- **Context**: 위키/설계 리포지토리(`minishell-wiki.git`)와 소스 코드 구현 리포지토리(`minishell.git`)의 역할 및 이슈 트래킹 체계 엄격 분리.
- **Repository Isolation**:
  - `42GS/minishell-wiki`:
    - 원격 `origin` (`git@github.com:42GS/minishell-wiki.git`) 연동 및 `main` 푸시 완료.
    - 위키/설계 전용 마일스톤(M1~M3) 및 12종 라벨 체계 생성.
    - 위키 전용 이슈 #1~#6 생성 및 완료 이슈(#1~#5) CLOSED 처리, #6 OPEN (Next).
    - `minishell-wiki` 커밋 타이틀의 `[#1]`~`[#5]`가 해당 위키 이슈와 1:1로 직접 연결됨.
  - `42GS/minishell`:
    - 기존 혼재되어 있던 17개 이슈 정리 후, 순수 C 언어 코드 구현 이슈 11개(#23~#33)로 명확히 재정렬.
- **Artifacts Updated**:
  - `wiki/process/roadmap_and_issues.md`: 듀얼 리포지토리 아키텍처 다이어그램 및 리포지토리별 분리된 이슈 트래킹 테이블 구축.
- **Index & Graph Updated**: 221개 지식 그래프 엣지 및 마크다운 무결성 유지.

## [2026-11-22] docs | Review and Update CLAUDE.md Schema with Dual-Repo & Lint Standards
- **Context**: `CLAUDE.md` 스키마가 현재의 듀얼 리포지토리(`minishell-wiki` vs `minishell`) 아키텍처와 확립된 Obsidian/Markdown 린트 규칙을 정확히 반영하도록 전면 현행화.
- **Updates Applied to `CLAUDE.md`**:
  - **헤더 및 내비게이션**: `Wiki Remote Repository`(`42GS/minishell-wiki`)와 `Implementation Remote Repository`(`42GS/minishell`) 명시, `wiki/process/` 링크 추가.
  - **Section 1.3 신설**: 이중 저장소 분리 원칙(Dual-Repository Isolation), 커밋 타이틀 `[#이슈번호]` 연결 규칙, `gh` CLI `--body-file`/`shell=False` 스크립트 안전 수칙 명문화.
  - **Section 2 현행화**: 실제 디렉토리 구조(`wiki/process/`, `templates/github/` 등) 반영 및 예정 디렉토리 구분.
  - **Section 4 전면 개정**: 구버전 `file:///` 링크 규정을 폐기하고 **Obsidian 네이티브 위키링크**, **테이블 파이프(`&#124;`) 보호**, **LaTeX 수식(`&#36;`) 충돌 방지**, **Mermaid 문법 무결성** 규정을 단일 진실 공급원(Schema)으로 승격.

## [2026-11-22] lint | Comprehensive Wiki Health Audit & Stale Reference Fix
- **Context**: Phase 4 착수 전 전체 위키의 고아 페이지, 미해결 링크, 문서 간 모순, 구버전 정보 전수 감사(Operations Protocol 3.3).
- **Issues Detected & Fixed**:
  - `wiki/requirements/mandatory.md`: 존재하지 않는 `[[raw/specs/bash_man]]` 링크를 실제 스펙 문서(`bash_quoting`, `bash_expansions_and_wildcards`, `bash_builtins`) 링크로 수정.
  - `wiki/process/github_engineering_standards.md`: 단일 리포지토리 표기를 듀얼 리포지토리(`minishell` + `minishell-wiki`)로 갱신하고 커밋 메시지 포맷(`[#<issue>]`) 및 라벨 체계를 현행화.
  - `wiki/process/roadmap_and_issues.md`: 미작성 상태인 `04_builtins_and_env_table.md` 임시 링크를 일반 코드 스팬으로 정규화.
  - `CLAUDE.md`: 이중 백틱 표기 파서 충돌을 방지하기 위해 `백틱 기호(Backtick)`로 교정.
- **Lint Audit Result**: Unresolved Links **0건**, Forbidden `file:///` **0건**, Orphan Pages **0건**, `index.md` 누락 **0건**, Mermaid/Table/LaTeX 오류 **0건** 달성.

## [2026-11-22] design | Phase 4: 7 Builtins & Environment Variable Engine Architecture & Deep Dive
- **Context**: `minishell-wiki` Issue #6 해결 — 4단계 내장 명령어(7대 빌트인)와 환경변수 사전 엔진 아키텍처 설계 및 심화 학습 문서화.
- **Architectural Specifications Added**:
  - `wiki/architecture/04_builtins_and_env_table.md`: `t_env_node` 연결 리스트 딕셔너리(`value == NULL` vs `""` 구분), `SHLVL`/`OLDPWD` 초기화, `execve`용 `envp` 직렬화 및 해제 계층, 단일 빌트인의 FD 백업/복원 프로토콜, 7대 빌트인(`echo`, `cd`, `pwd`, `export`, `unset`, `env`, `exit`) 정밀 명세 및 엣지 케이스 설계.
- **Deep Dive Concepts Added**:
  - `wiki/concepts/deep_dive_builtins_and_environment.md`: 프로세스 유저 스택 `environ` 레이아웃, 커널 PCB CWD 및 CoW 메모리 격리로 인한 부모 프로세스 실행 필연성, `exit` 8비트 모듈러 마스킹(`status & 0xFF`), C 표준 UB 없는 `LLONG_MAX`/`LLONG_MIN` 사전 컷오프 오버플로 방어 수학, `export` 비파괴적 포인터 배열 정렬 패턴.
- **Cross-References & Status**: `index.md`, `CLAUDE.md`, `roadmap_and_issues.md`, `mandatory.md`, `evaluation_matrix.md` 상호 연결 완료.
- **Context**: 사용자 요청에 따라 GitHub 원격 리포지토리(`42GS/minishell`)에 5개 마일스톤(M1~M5) 및 17개 표준 이슈 전수 등록 및 추적 체계 확립.
- **Remote Issues Created on `42GS/minishell`**:
  - **M1 (Architecture & Foundation)**:
    - #1: `[FEAT] Knowledge Base & LLM Wiki Bootstrap` (Closed)
    - #2: `[ARCH] Phase 1: Lexer, Parser & AST Architecture Design` (Closed)
    - #3: `[ARCH] Phase 2: Execution Engine & IPC Pipeline Design` (Closed)
    - #4: `[ARCH] Phase 3: Asynchronous Signal Dispatcher Design` (Closed)
    - #5: `[INFRA] GitHub Engineering Infrastructure & Standards` (Closed)
    - #6: `[ARCH] Phase 4: 7 Builtin Utilities & Environment Variable Engine Design` (Open - Next)
    - #7: `[INFRA] Project Repository Initialization, Norminette CI, and Makefile Scaffolding` (Open)
    - #8: `[TEST] Automated Test Suite Setup (FIRST Principles, AAA Pattern, Leak Detector)` (Open)
  - **M2 (Lexer & Parser)**:
    - #9: `[FEAT] Implement Lexer & Tokenizer DFA Engine` (Open)
    - #10: `[FEAT] Implement Recursive Descent Parser & AST Builder` (Open)
  - **M3 (Execution Engine & IPC)**:
    - #11: `[FEAT] Implement Pipeline Execution & Multi-Process Concurrency` (Open)
    - #12: `[FEAT] Implement Redirection & Heredoc Engine` (Open)
  - **M4 (Builtins & Signals)**:
    - #13: `[FEAT] Implement 7 Builtin Utilities & Environment Table` (Open)
    - #14: `[FEAT] Implement Asynchronous Signal Dispatcher & State Machine` (Open)
  - **M5 (Bonus & Full QA Hardening)**:
    - #15: `[BONUS] Implement Logical Operators (&&, ||) & Subshell ( )` (Open)
    - #16: `[BONUS] Implement Wildcard Expansion (*) via opendir/readdir` (Open)
    - #17: `[QA] Full Memory Leak (Valgrind) & FD Leak Automated Verification` (Open)
- **Artifacts Added**:
  - `wiki/process/roadmap_and_issues.md`: 마일스톤 개요, 17개 이슈 1:1 위키 매핑 테이블, Mermaid 순서도, 다음 단계 액션 아이템 명시.
- **Index Updated**: `index.md`에 `roadmap_and_issues.md` 등록.
