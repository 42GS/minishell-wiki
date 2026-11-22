# Minishell LLM Wiki Index

> **Minishell Knowledge Base Catalog**  
> 모든 위키 문서의 목록과 카테고리별 요약 및 상호 참조 링크입니다.

---

## 1. System Specifications & Schemas (설계 및 스키마)

| 문서 | 설명 | 경로 |
| :--- | :--- | :--- |
| [CLAUDE.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/CLAUDE.md) | 위키 스키마 규격, 백엔드 포트폴리오 엔지니어링 표준, 운영 프로토콜 및 구버전 봉인 원칙 | [CLAUDE.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/CLAUDE.md) |
| [log.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/log.md) | 위키 작업 히스토리 시계열 저널 (Ingest / Query / Lint / Refactor) | [log.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/log.md) |

---

## 2. Requirements & Evaluation (요구사항 및 평가 분석)

| 문서 | 설명 | 경로 |
| :--- | :--- | :--- |
| [wiki/requirements/mandatory.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/requirements/mandatory.md) | 42 서브젝트 v7.1 기준 필수(Mandatory) 과제 요구사항 정밀 분석 및 제약조건 | [mandatory.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/requirements/mandatory.md) |
| [wiki/requirements/bonus.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/requirements/bonus.md) | 보너스 과제 정밀 분석 (`&&`, `\|\|`, `( )` 서브셸 우선순위, 와일드카드 `*` Globbing) | [bonus.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/requirements/bonus.md) |
| [wiki/requirements/evaluation_matrix.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/requirements/evaluation_matrix.md) | 42evalhub 평가 시트 항목별 1:1 매핑 검증 체크리스트 및 방어 전략 | [evaluation_matrix.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/requirements/evaluation_matrix.md) |

---

## 3. Core Concepts & Deep Dive (핵심 이론 및 심화 학습)

| 문서 | 설명 | 경로 |
| :--- | :--- | :--- |
| [wiki/concepts/deep_dive_lexer_parser_ast.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/concepts/deep_dive_lexer_parser_ast.md) | **[심화]** 왜 단순 split은 실패하는가? 오토마타(DFA), 문맥 자유 문법(CFG), 재귀 하향 파싱 및 확장 타이밍 논리 | [deep_dive_lexer_parser_ast.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/concepts/deep_dive_lexer_parser_ast.md) |
| [wiki/concepts/allowed_functions_matrix.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/concepts/allowed_functions_matrix.md) | 허용 외부 함수 53종 전수 분석, Async-Signal-Safe 판정 및 FD/메모리 주의점 | [allowed_functions_matrix.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/concepts/allowed_functions_matrix.md) |

---

## 4. System Architecture Specifications (시스템 아키텍처 상세 설계)

| 문서 | 설명 | 경로 |
| :--- | :--- | :--- |
| [wiki/architecture/01_parser_and_ast.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/architecture/01_parser_and_ast.md) | **[설계 1]** Lexer/Tokenizer DFA 규칙, EBNF 정형 문법, C 언어 AST 데이터 구조체 및 재귀 하향 파서 | [01_parser_and_ast.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/wiki/architecture/01_parser_and_ast.md) |

---

## 5. Raw Sources Registry (불변 원문 소스 보관소)

| 분류 | 소스 명 | 설명 | 경로 |
| :--- | :--- | :--- | :--- |
| **과제 명세** | `raw/subject/en.subject.pdf` | 42 공식 과제 PDF 원문 (v7.1) | [en.subject.pdf](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/subject/en.subject.pdf) |
| **과제 명세** | `raw/subject/en.subject.md` | 공식 과제 PDF 무손실 추출 텍스트 마크다운 | [en.subject.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/subject/en.subject.md) |
| **평가 기준** | `raw/evalhub/minishell_eval_scale.html` | 42evalhub 원본 평가 시트 HTML | [minishell_eval_scale.html](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/evalhub/minishell_eval_scale.html) |
| **평가 기준** | `raw/evalhub/minishell_eval_scale.md` | 42evalhub 파싱 및 마크다운 구조화 문서 | [minishell_eval_scale.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/evalhub/minishell_eval_scale.md) |
| **매뉴얼** | `raw/manpages/` | 허용 함수 53종 공식 시스템 man page 텍스트 아카이브 | [raw/manpages/](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/manpages/) |
| **셸 표준** | `raw/specs/bash_man.txt` | GNU Bash Reference Manual 전체 텍스트 | [bash_man.txt](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_man.txt) |
| **셸 표준** | `raw/specs/bash_quoting.md` | Bash Quoting (따옴표) 명세 원문 | [bash_quoting.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_quoting.md) |
| **셸 표준** | `raw/specs/bash_pipelines.md` | Bash Pipelines (`\|`) 및 서브셸 명세 원문 | [bash_pipelines.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_pipelines.md) |
| **셸 표준** | `raw/specs/bash_lists.md` | Bash Lists (`&&`, `\|\|`) 연산자 명세 원문 | [bash_lists.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_lists.md) |
| **셸 표준** | `raw/specs/bash_compound_commands.md` | Bash Compound Commands (`( )`) 명세 원문 | [bash_compound_commands.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_compound_commands.md) |
| **셸 표준** | `raw/specs/bash_expansions_and_wildcards.md` | Bash Parameter Expansion 및 Globbing (`*`) 명세 원문 | [bash_expansions_and_wildcards.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_expansions_and_wildcards.md) |
| **셸 표준** | `raw/specs/bash_redirections.md` | Bash Redirection (`<`, `>`, `>>`, `<<`) 명세 원문 | [bash_redirections.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_redirections.md) |
| **셸 표준** | `raw/specs/bash_signals.md` | Bash Signals 및 Interactive Shell 동작 명세 원문 | [bash_signals.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_signals.md) |
| **셸 표준** | `raw/specs/bash_exit_status.md` | Bash Exit Status 반환 규칙 명세 원문 | [bash_exit_status.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_exit_status.md) |
| **셸 표준** | `raw/specs/bash_builtins.md` | Bash Builtin Utilities 명세 원문 | [bash_builtins.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_builtins.md) |
