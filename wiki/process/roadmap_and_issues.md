# Minishell Project Roadmap & Dual-Repository Issue Tracking

> **Dual-Repository Architecture & Issue Tracking Strategy**  
> **지식베이스(위키/설계)**와 **프로덕션 소스 코드(C 구현)**를 두 개의 독립 GitHub 리포지토리로 분리 관리  
> - **위키/설계 리포지토리**: [42GS/minishell-wiki](https://github.com/42GS/minishell-wiki)  
> - **코드 구현 리포지토리**: [42GS/minishell](https://github.com/42GS/minishell)

---

## 1. Dual-Repository Structure & Roles

```mermaid
flowchart LR
    subgraph WIKI_REPO["Repository: 42GS/minishell-wiki"]
        W1["#1 Knowledge Base Ingest"]
        W2["#2 Phase 1: Lexer/AST Arch"]
        W3["#3 Phase 2: Executor/IPC Arch"]
        W4["#4 Phase 3: Signal Arch"]
        W5["#5 GitHub Standards & Infra"]
        W6["#6 Phase 4: Builtins/Env Arch (Done)"]
        W7["#16 Lint: Sync #41-#45 and Audit (Done)"]
        W8["#18 Retro: Legacy Comparison (Done)"]
        W9["#20/#22 Portfolio README and Wiki CI (Done)"]
    end

    subgraph CODE_REPO["Repository: 42GS/minishell"]
        C1["#23 Infra: Scaffolding & Makefile (Done)"]
        C2["#24 Test: Compliance Harness (Done)"]
        C3["#25 Feat: Lexer DFA Engine (Done)"]
        C4["#26 Feat: Recursive Descent AST (Done)"]
        C5["#27 Feat: Pipeline & Concurrency (Done)"]
        C6["#28 Feat: Redirection & Heredoc (Done)"]
        C7["#29 Feat: 7 Builtins & Env (Done)"]
        C8["#30 Feat: Signal Handling (Done)"]
        C8b["#41-#45 Stabilize: Review and Refactor (Done)"]
        C9["#31 Bonus: Logic Ops and Subshell (Done)"]
        C10["#32 Bonus: Wildcard Globbing (Done)"]
        C11["#33 QA: Valgrind and Retro (Done)"]
        C12["#54-#60 Docs: Doxygen and GHCR CI (Done)"]
    end

    WIKI_REPO -->|Architectural Blueprints and Specifications| CODE_REPO

    classDef done fill:#2e7d32,stroke:#1b5e20,color:#ffffff;

    class W1,W2,W3,W4,W5,W6,W7,W8,W9,C1,C2,C3,C4,C5,C6,C7,C8,C8b,C9,C10,C11,C12 done;
```

---

## 2. Wiki & Architecture Issues (`42GS/minishell-wiki`)

`minishell-wiki` 커밋 타이틀의 이슈 번호(`[#1]`, `[#2]`, ...) 1:1 연결 규격:

| Issue # | Type / Priority | Title | Milestone | Status | Related Wiki Spec |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **#1** | `feat` &#124; P1: High | [FEAT] Knowledge Base & Source of Truth Ingestion | M1 | **CLOSED** | [CLAUDE](../../CLAUDE.md), [mandatory](../requirements/mandatory.md) |
| **#2** | `arch` &#124; P0: Critical | [ARCH] Phase 1: Lexer, Formal Grammar & AST Parser Architecture Design | M1 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md), [deep_dive_lexer_parser_ast](../concepts/deep_dive_lexer_parser_ast.md) |
| **#3** | `arch` &#124; P0: Critical | [ARCH] Phase 2: Execution Engine, Process Lifecycle & IPC Pipeline Design | M1 | **CLOSED** | [02_execution_engine_and_ipc](../architecture/02_execution_engine_and_ipc.md), [deep_dive_process_ipc_and_fd](../concepts/deep_dive_process_ipc_and_fd.md) |
| **#4** | `arch` &#124; P0: Critical | [ARCH] Phase 3: Asynchronous Signal Dispatcher & 3-State Machine Design | M1 | **CLOSED** | [03_signal_dispatcher_and_state_machine](../architecture/03_signal_dispatcher_and_state_machine.md), [deep_dive_signals_and_concurrency](../concepts/deep_dive_signals_and_concurrency.md) |
| **#5** | `infra` &#124; P1: High | [INFRA] GitHub Engineering Standards, Issue/PR Templates & CI Specification | M1 | **CLOSED** | [github_engineering_standards](github_engineering_standards.md) |
| **#6** | `arch` &#124; P0: Critical | [ARCH] Phase 4: 7 Builtin Utilities Specification & Environment Variable Engine Design | M1 | **CLOSED** | [04_builtins_and_env_table](../architecture/04_builtins_and_env_table.md), [deep_dive_builtins_and_environment](../concepts/deep_dive_builtins_and_environment.md) |
| **#16** | `lint` &#124; P1: High | [LINT] Sync Stabilization Batch (#41-#45) & Perform Wiki Health Audit | M2 | **CLOSED** | [roadmap_and_issues](roadmap_and_issues.md), [log](../../log.md) |
| **#18** | `retro` &#124; P0: Critical | [RETRO] Legacy Comparison Retrospective (minishell-old vs minishell) & Final Roadmap Sync | M3 | **CLOSED** | [legacy_retrospective](../eval/legacy_retrospective.md), [log](../../log.md) |
| **#20** | `docs` &#124; P1: High | [Docs] Create Portfolio README and Synchronize Wiki Catalog | M3 | **CLOSED** | [README](../../README.md), [index](../../index.md) |
| **#22** | `infra` &#124; P1: High | [CI] Use System python3 and Concurrency in wiki-lint Workflow | M3 | **CLOSED** | [github_engineering_standards](github_engineering_standards.md), [log](../../log.md) |

---

## 3. Implementation & QA Issues (`42GS/minishell`)

C 소스 코드 리포지토리(`~/Projects/gdtknight/42/minishell`) 브랜치 및 Conventional Commits 추적 이슈 목록:

| Issue # | Type / Priority | Title | Milestone | Status | Preceding Wiki Architecture |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **#23** | `infra` &#124; P1: High | [INFRA] Project Repository Scaffolding, Strict Makefile & Norminette Setup | M1 | **CLOSED** | [github_engineering_standards](github_engineering_standards.md) |
| **#24** | `test` &#124; P1: High | [TEST] Automated Test Suite & 42evalhub Compliance Harness Design | M1 | **CLOSED** | [evaluation_matrix](../requirements/evaluation_matrix.md) |
| **#25** | `feat` &#124; P0: Critical | [FEAT] Implement Lexer (DFA) & Tokenizer Engine | M2 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md) |
| **#26** | `feat` &#124; P0: Critical | [FEAT] Implement Recursive Descent AST Parser & Syntax Validator | M2 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md) |
| **#27** | `feat` &#124; P0: Critical | [FEAT] Implement Pipeline Execution Engine & Strict Pipe-Closing Protocol | M3 | **CLOSED** | [02_execution_engine_and_ipc](../architecture/02_execution_engine_and_ipc.md) |
| **#28** | `feat` &#124; P0: Critical | [FEAT] Implement Redirection Engine (<, >, >>, << Heredoc) | M3 | **CLOSED** | [02_execution_engine_and_ipc](../architecture/02_execution_engine_and_ipc.md) |
| **#29** | `feat` &#124; P1: High | [FEAT] Implement 7 Builtin Commands & Environment Variable Management | M4 | **CLOSED** | [04_builtins_and_env_table](../architecture/04_builtins_and_env_table.md) |
| **#30** | `feat` &#124; P0: Critical | [FEAT] Implement Asynchronous Signal Handling & Terminal termios Control | M4 | **CLOSED** | [03_signal_dispatcher_and_state_machine](../architecture/03_signal_dispatcher_and_state_machine.md) |
| **#41** | `fix` &#124; P0: Critical | [BUG] Eliminate Here-doc Tempfile Race Condition and Sibling Pipe FD Leak | M5 | **CLOSED** | [02_execution_engine_and_ipc](../architecture/02_execution_engine_and_ipc.md) |
| **#42** | `fix` &#124; P0: Critical | [BUG] Implement Unquoted Expansion IFS Word Splitting, Ambiguous Redirect & Bash Special Dollar Parity | M5 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md) |
| **#43** | `fix` &#124; P1: High | [BUG] Fix PATH Resolution Edge Cases (Empty Segments, Directory Filtering, ./.. & EACCES 126) | M5 | **CLOSED** | [02_execution_engine_and_ipc](../architecture/02_execution_engine_and_ipc.md) |
| **#44** | `fix` &#124; P1: High | [BUG] Harden Lexer/Parser Error Paths (&&&, OOM/NULL Guards) and Unchecked Syscalls | M5 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md), [04_builtins_and_env_table](../architecture/04_builtins_and_env_table.md) |
| **#45** | `refactor` &#124; P2: Normal | [REFACTOR] Eliminate O(N^2) String Reallocation, Deduplicate Quote/Redir Helpers & Reduce Complexity | M5 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md), [04_builtins_and_env_table](../architecture/04_builtins_and_env_table.md) |
| **#31** | `bonus` &#124; P1: High | [BONUS] Implement Logical Operators (&&, &#124;&#124;) and Subshells ( ) | M5 | **CLOSED** | [bonus](../requirements/bonus.md) |
| **#32** | `bonus` &#124; P1: High | [BONUS] Implement Wildcard Globbing (*) for Current Working Directory | M5 | **CLOSED** | [bonus](../requirements/bonus.md) |
| **#33** | `test` &#124; P0: Critical | [QA] Full Memory Leak (Valgrind) & Regression Hardening, Legacy Retrospective | M5 | **CLOSED** | [evaluation_matrix](../requirements/evaluation_matrix.md), [allowed_functions_matrix](../concepts/allowed_functions_matrix.md), [legacy_retrospective](../eval/legacy_retrospective.md) |
| **#54** | `docs` &#124; P1: High | [Docs] Upgrade Portfolio README (Architecture, Trade-offs, Quantitative Metrics) | M5 | **CLOSED** | [legacy_retrospective](../eval/legacy_retrospective.md), [log](../../log.md) |
| **#56** | `docs` &#124; P2: Normal | [Docs] Add Norminette-compliant Doxygen Comments Across All 58 Production Files | M5 | **CLOSED** | [01_parser_and_ast](../architecture/01_parser_and_ast.md), [log](../../log.md) |
| **#58** | `infra` &#124; P2: Normal | [CI] Build and Publish Lightweight GHCR Custom CI Image | M5 | **CLOSED** | [github_engineering_standards](github_engineering_standards.md), [log](../../log.md) |
| **#60** | `infra` &#124; P2: Normal | [CI] Switch CI Pipeline to GHCR Image and Parallelize Unit & Valgrind QA | M5 | **CLOSED** | [github_engineering_standards](github_engineering_standards.md), [log](../../log.md) |

---

## 4. Work Execution Roadmap

1. **위키 설계 완료 (Wiki Issue #1 ~ #6, #16, #18 - ALL CLOSED)**:
   - Phase 1~4 아키텍처 및 심화 개념 문서 전수 작성, 안정화 감사(`#16`) 및 최종 구버전 비교 회고(`#18`) 완료
2. **코드 리포지토리 구축 및 테스트 셋업 완료 (Code Issue #23, #24 - CLOSED)**:
   - 로컬 `~/Projects/gdtknight/42/minishell` 초기화, `.github/` 템플릿/CI 이식, No-relink `Makefile` 및 `libft` 구축 완료
   - 자동화 단위 테스트(`tests/unit/`) 및 42evalhub 비교 E2E 테스트 하네스(`tests/e2e/`) 구축 완료
   - GitHub Actions CI (Norminette + Strict Build + No-relink + Valgrind 0 leaks) Green 통과 확인
3. **전체 구현·안정화·보너스·QA 100% 완료 (Code Issue #25 ~ #33, #41 ~ #45 - ALL CLOSED)**:
   - 토크나이저(#25 완료) -> 파서(#26 완료) -> 파이프라인(#27 완료) -> 리다이렉션/Heredoc(#28 완료) -> 빌트인(#29 완료) -> 시그널(#30 완료, M4 달성) -> 코드 리뷰 안정화(#41~#45 완료, PR #46~#50) -> 보너스(#31, #32 완료, PR #51~#52) -> Valgrind/FD QA 및 구버전 회고(#33, Wiki #18 완료, PR #53)
4. **포트폴리오 고도화, 코드 Doxygen 문서화 & CI 병렬 최적화 (Code #54 ~ #60, Wiki #20, #22 - ALL CLOSED)**:
   - 양 저장소 포트폴리오 `README.md`, `v1.0.0`~`v1.1.0` Release 및 GitHub Wiki 발행 완료
   - 전체 58개 파일 Norminette 준수 영문 Doxygen 주석 적용(`#56`, 실행 코드 변경 `0`건)
   - GHCR 커스텀 이미지(`ghcr.io/42gs/minishell-ci`), Job/Unit/Valgrind 병렬화로 CI 속도 **`77~80s -> 29~36s`**(`-62.3%`) 및 Wiki Lint **`12~15s -> 9~10s`** 단축 달성

---

## 5. Cross References (상호 참조)
- **위키 스키마**: [[CLAUDE]]
- **전체 색인**: [[index]]
- **히스토리 저널**: [[log]]
- **GitHub 엔지니어링 표준**: [[github_engineering_standards]]
- **평가 매트릭스**: [[evaluation_matrix]]
