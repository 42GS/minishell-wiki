# GitHub Engineering Standards & Portfolio Strategy

> **Navigation**: [[index|Hub: Index]] | [[CLAUDE|Schema & Rules]] | [[wiki/process/roadmap_and_issues|Dual-Repo Roadmap]]  
> **Code Repository**: `git@github.com:42GS/minishell.git` | **Wiki Repository**: `git@github.com:42GS/minishell-wiki.git`  
> **Templates**: `templates/github/` (Issue/PR Templates, CI Workflow)  
> **Purpose**: 백엔드·시스템 소프트웨어 엔지니어링 관점의 기술 깊이 및 추적성 확보용 포트폴리오 표준

---

## 1. Portfolio Philosophy: Core Competencies

깃허브 저장소 평가 시 핵심 4대 엔지니어링 역량:

```mermaid
graph TD
    Repo["GitHub Repository (Portfolio Core)"]
    
    Repo --> C1["1. Engineering Discipline: Conventional Commits"]
    Repo --> C2["2. Problem Solving: Issue-driven Traceability"]
    Repo --> C3["3. Architectural Thinking: PR Trade-off Notes"]
    Repo --> C4["4. Quality Assurance: CI Automation Gate"]
```

1. **공학적 규율 (Engineering Discipline)**: 원자적(Atomic) 단위 커밋 분리 및 일관된 커밋 컨벤션 유지
2. **문제 정의와 추적성 (Traceability)**: 모든 변경의 발단(이슈), 해결(PR), 머지 이력의 100% 상호 연결
3. **설계 의도 및 트레이드오프 (Architectural Communication)**: PR 본문 내 선택 이유(Why)와 배제 대안(Trade-off) 명시
4. **품질 자동화 (Quality Automation)**: CI 기반 코드 컨벤션(Norminette), 엄격 빌드, 메모리 누수 자동 게이팅

---

## 2. Git Branching Strategy: GitHub Flow

단순하고 명확한 **GitHub Flow** 적용

```mermaid
gitGraph
    commit id: "init"
    branch feat/parser
    checkout feat/parser
    commit id: "feat: add lexer dfa"
    commit id: "feat: implement ast"
    checkout main
    merge feat/parser id: "merge PR #1"
    branch feat/executor
    checkout feat/executor
    commit id: "feat: pipe engine"
    checkout main
    merge feat/executor id: "merge PR #2"
```

### 2.1 브랜치 명명 규칙
- **기능 개발**: `feat/<issue-number>-<short-description>` (예: `feat/12-ast-parser`)
- **버그 수정**: `fix/<issue-number>-<short-description>` (예: `fix/25-heredoc-signal-leak`)
- **리팩토링**: `refactor/<short-description>` (예: `refactor/unify-fd-closing`)
- **문서화**: `docs/<short-description>` (예: `docs/update-readme-c4-diagram`)

### 2.2 메인 브랜치 (`main`) 보호 원칙
- `main` 브랜치의 상시 정상 컴파일, Norm 통과, 릭 제로, 평가 통과 상태 유지
- `main` 직접 푸시(`git push origin main`) 금지, **PR(Pull Request) 전용 머지** 강제

---

## 3. Conventional Commits Specification

[Conventional Commits 1.0.0](https://www.conventionalcommits.org/) 표준 준수

### 3.1 커밋 메시지 포맷
```text
[#<issue>] <type>(<scope>): <subject>

[optional body: Why this change was made, technical details]

[optional footer: Closes #issue-number]
```

### 3.2 허용 Type 및 Minishell Scope 목록
| Type | 설명 | 허용 Scope 예시 |
| :--- | :--- | :--- |
| `feat` | 새로운 기능 추가 | `lexer`, `parser`, `ast`, `pipe`, `redir`, `builtin`, `signal`, `bonus` |
| `fix` | 버그 및 결함 수정 | `leak`, `heredoc`, `exit-code`, `quote`, `signal-race` |
| `refactor` | 기능 변경 없는 코드 구조 개선 | `cleanup`, `norm`, `fd-table`, `ast-walker` |
| `test` | 테스트 케이스 및 하네스 추가/수정 | `unit`, `e2e`, `eval`, `fuzz` |
| `docs` | README 및 문서 추가/수정 | `readme`, `adr`, `architecture`, `schema` |
| `ci` | GitHub Actions 워크플로우 수정 | `actions`, `lint`, `valgrind` |
| `chore` | 빌드 스크립트, Makefile 수정 | `makefile`, `gitignore` |

### 3.3 우수한 커밋 메시지 예시
```text
[#27] feat(executor): implement multi-command pipeline execution engine

- Resolve command list from AST and allocate (N - 1) pipes
- Implement strict pipe-closing protocol in child and parent to prevent hangs
- Wait for all children and propagate the rightmost command exit status to $?

Closes #27
```

---

## 4. Milestone & Label Architecture

진행 상황 추적용 5단계 마일스톤 및 4계층 라벨 체계

### 4.1 마일스톤 (Milestones)
1. **M1: Architecture & Scaffolding** (인프라, 뼈대, 자료구조, 빌드 시스템)
2. **M2: Lexer & AST Parser** (어휘 분석, 정형 문법, AST 트리 빌더)
3. **M3: Execution & IPC Engine** (프로세스 생명주기, 파이프라인, 리다이렉션)
4. **M4: Signals & Builtin Utilities** (3대 상태 머신, 7대 빌트인, 환경변수)
5. **M5: Bonus Features & Final Hardening** (`&&`, `||`, `( )`, `*`, 릭 제로 검증)

### 4.2 라벨 체계 (Issue & PR Labels)
- **우선순위**: `P0: Critical`, `P1: High`, `P2: Normal`
- **영역(Scope)**: `area:infra`, `area:parser`, `area:executor`, `area:signals`, `area:builtins`, `area:bonus`
- **유형(Type)**: `type:architecture`, `type:concept`, `type:feature`, `type:bug`, `type:refactor`, `type:docs`, `type:test`, `type:lint`
- **안정성(Safety)**: `safety:memory-leak`, `safety:fd-leak`, `safety:norminette`

---

## 5. GitHub Actions CI Pipeline Specification

PR 생성 및 `main` 푸시 시 자동 실행되는 품질 게이트 파이프라인:

```mermaid
flowchart LR
    Push["PR / Push Event"] --> Runner["Ubuntu Runner"]
    Runner --> Step1["Step 1: Norminette Check"]
    Step1 --> Step2["Step 2: Strict Build (-Wall -Wextra -Werror)"]
    Step2 --> Step3["Step 3: Automated Test Suite Run"]
    Step3 --> Step4["Step 4: Valgrind Memory Leak Gate"]
```

### CI 검증 항목
1. **Norminette Check**: 전체 소스코드 42 Norminette 컨벤션 위반 검사
2. **Strict Compilation**: `cc -Wall -Wextra -Werror` 및 `make`, `make re`, `make bonus` No-Relink 빌드 검사
3. **Memory Leak Gate**: Valgrind 환경 파이프라인·리다이렉션·에러 케이스 힙 릭 0바이트(`definitely lost: 0`, `indirectly lost: 0`) 검증
