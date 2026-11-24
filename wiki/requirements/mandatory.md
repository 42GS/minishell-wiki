# Minishell Mandatory Requirements Specification

> **Navigation**: [[index|Hub: Index]] | [[wiki/requirements/bonus|Bonus Spec]] | [[wiki/requirements/evaluation_matrix|Evaluation Matrix]]  
> **Architecture Mappings**: [[wiki/architecture/01_parser_and_ast|Phase 1: Parser & AST]] | [[wiki/architecture/02_execution_engine_and_ipc|Phase 2: Execution Engine]] | [[wiki/architecture/03_signal_dispatcher_and_state_machine|Phase 3: Signal Dispatcher]] | [[wiki/architecture/04_builtins_and_env_table|Phase 4: Builtins & Env]]  
> **Source**: [[raw/subject/en.subject|en.subject.md]] (v7.1) | **Reference**: [[raw/specs/bash_quoting|Quoting]], [[raw/specs/bash_expansions_and_wildcards|Expansions]], [[raw/specs/bash_builtins|Builtins]]  
> **Status**: Ingested & Verified

---

## 1. Program & Build Specifications

| 항목 | 요구사항 규격 | 구현 아키텍처 매핑 |
| :--- | :--- | :--- |
| **프로그램 명** | `minishell` | Makefile의 `$(NAME)` |
| **제출 파일** | `Makefile`, `*.h`, `*.c` | Libft 허용 (내부 포함 필수) |
| **Makefile Rules** | `$(NAME)`, `all`, `clean`, `fclean`, `re` | `bonus` 룰 포함 권장 |
| **컴파일 플래그** | `cc -Wall -Wextra -Werror` | **No Relink** 엄격 준수 |
| **외부 라이브러리** | GNU Readline (`-lreadline`) | 메모리 릭 발생 허용 (OS/라이브러리 기인분) |
| **코드 규격** | 42 Norm (최신 Norminette 100% 준수) | 주석, 함수 길이 25줄, 5개 함수/파일 등 |
| **크래시 규격** | Segfault, Bus Error, Double Free 등 비정상 종료 시 평가 0점 | 모든 예외 상황 방어 |

---

## 2. Global Variable Constraint (핵심 제약)

> [!CAUTION]
> **단 하나의 전역 변수만 허용, 수신된 시그널 번호(int) 저장 전용**  
> - "Avoid using more than one global variable to indicate a received signal."  
> - "This global variable cannot provide any other information or data access than the number of a received signal."  
> - 상세 설계: [[wiki/architecture/03_signal_dispatcher_and_state_machine|시그널 디스패처 단일 전역 변수 격리 설계]]  
> - 이론적 배경: [[wiki/concepts/deep_dive_signals_and_concurrency|비동기 시그널 안전성과 volatile sig_atomic_t 심화]]

---

## 3. Core Shell Features

### 3.1 Prompt & History
- 명령어 입력 대기 시 새 프롬프트(`minishell$ ` 등) 표시
- 입력된 명령어 히스토리 기록 (`add_history`)
- **예외**: Here-doc (`<<`) 입력 시 히스토리 갱신 생략 가능 (Subject 명시)
- 관련 시스템 콜: [[wiki/concepts/allowed_functions_matrix|Readline 함수군]]

### 3.2 Executable Search & Execution
- 절대 경로(`/bin/ls`), 상대 경로(`./my_prog`) 기반 실행 파일 실행
- `PATH` 환경변수 파싱 -> 콜론(`:`) 구분 디렉토리 목록 내 실행 파일 탐색
- 구현 상세: [[wiki/architecture/02_execution_engine_and_ipc|실행 엔진 아키텍처]]
- 에러 처리 규격 (Bash 호환):
  - 파일 미존재: `command not found` (Exit status 127)
  - 실행 권한 없음 / 디렉토리 실행 시도: `Permission denied` / `Is a directory` (Exit status 126)

### 3.3 Quoting Rules (따옴표 처리)
- 문법 상세: [[wiki/architecture/01_parser_and_ast|어휘 분석기(Lexer) 상태 머신]]
- 이론적 배경: [[wiki/concepts/deep_dive_lexer_parser_ast|오토마타와 따옴표 제거 3단계 파이프라인]]
- **닫히지 않은 따옴표**: 미해석 (요구사항 외 백슬래시(`\`), 세미콜론(`;`) 특수문자 미해석)
- **싱글 쿼트 (`'`)**: 내부 모든 메타문자(`$`, `\`, `"` 등) 특수 의미 무효화 (Literal 처리)
- **더블 쿼트 (`"`)**: 내부 메타문자 무효화, **환경변수 확장(`$`)만 허용**

### 3.4 Expansions (변수 및 상태 코드 확장)
- `$VAR`: 환경변수 이름 매칭 후 값 치환, 미정의 변수는 빈 문자열 치환
- `$?`: 최근 실행된 포그라운드 파이프라인 종료 상태 코드(Exit Status, 0~255) 치환
- 스펙 원문: [[raw/specs/bash_expansions_and_wildcards|Bash Expansion Spec]]

### 3.5 Redirections (입출력 재지향)
1. `<`: 입력 리다이렉션 (`O_RDONLY`)
2. `>`: 출력 리다이렉션 (Truncate 모드, `O_WRONLY | O_CREAT | O_TRUNC`, 0644)
3. `>>`: 출력 추가 리다이렉션 (Append 모드, `O_WRONLY | O_CREAT | O_APPEND`, 0644)
4. `<< DELIMITER`: Here-document (`DELIMITER` 단일 라인 입력까지 수집)
- 구현 상세: [[wiki/architecture/02_execution_engine_and_ipc|리다이렉션 엔진 아키텍처]]
- 스펙 원문: [[raw/specs/bash_redirections|Bash Redirection Spec]]

### 3.6 Pipelines (`|`)
- 이전 명령어 `stdout` -> 다음 명령어 `stdin` 연결
- 모든 파이프라인 명령어의 자식 프로세스 병렬 포크(`fork`) 및 동시 실행
- 파이프라인 최종 반환값: **마지막 실행 명령어의 종료 상태 코드**
- 이론적 배경: [[wiki/concepts/deep_dive_process_ipc_and_fd|파이프라인 무한 행(Deadlock)의 원인과 해결]]
- 구현 상세: [[wiki/architecture/02_execution_engine_and_ipc|파이프라인 실행 엔진]]

### 3.7 Signal Handling (대화형 및 비대화형)
- 구현 상세: [[wiki/architecture/03_signal_dispatcher_and_state_machine|시그널 디스패처 3대 상태 머신]]
- 이론적 배경: [[wiki/concepts/deep_dive_signals_and_concurrency|시그널 인터럽트와 포그라운드 제어]]
- **Interactive Prompt 대기 중**:
  - `Ctrl + C` (`SIGINT`): 새 라인 이동 및 새 프롬프트 출력 (`rl_on_new_line`, `rl_redisplay`), 종료 코드 `130` (`128 + 2`)
  - `Ctrl + D` (`EOF`): 셸 정상 종료 (`exit`)
  - `Ctrl + \` (`SIGQUIT`): 무반응 (무시)
- **자식 프로세스 실행 중 (Foreground Command)**:
  - `Ctrl + C`: 자식 프로세스 `SIGINT` 종료, 새 라인 출력 및 `$? = 130`
  - `Ctrl + \`: 자식 프로세스 `SIGQUIT` 종료, `Quit (core dumped)\n` 출력 및 `$? = 131`
- **Here-doc 입력 중**:
  - `Ctrl + C`: 입력 즉시 중단, 프롬프트 복귀 및 `$? = 130`

---

## 4. Built-in Utilities (7종)

외부 프로세스 포크 없이 부모 셸 상태를 변경하거나 내장 실행되는 유틸리티:

| 빌트인 | 요구사항 명세 | 부모 프로세스 직접 실행 필요성 | 구현 매핑 |
| :--- | :--- | :--- | :--- |
| `echo` | `-n` 옵션 지원 (연속 `-nnnn` 포함) | 서브셸/부모 무관 | [[wiki/architecture/04_builtins_and_env_table]] |
| `cd` | 상대/절대 경로만 지원 (옵션 없음) | **반드시 부모 프로세스** (작업 디렉토리 변경) | [[wiki/architecture/04_builtins_and_env_table]] |
| `pwd` | 옵션 없음 (현재 작업 디렉토리 출력) | 서브셸/부모 무관 | [[wiki/architecture/04_builtins_and_env_table]] |
| `export` | 옵션 없음 (환경변수 설정 및 무인자 정렬 목록 출력) | **반드시 부모 프로세스** (환경변수 테이블 갱신) | [[wiki/architecture/04_builtins_and_env_table]] |
| `unset` | 옵션 없음 (환경변수 제거) | **반드시 부모 프로세스** (환경변수 테이블 갱신) | [[wiki/architecture/04_builtins_and_env_table]] |
| `env` | 옵션/인자 없음 (현재 환경변수 목록 출력) | 서브셸/부모 무관 | [[wiki/architecture/04_builtins_and_env_table]] |
| `exit` | 옵션 없음 (종료 코드 인자 지정 가능, 0~255 오버플로우 처리) | **반드시 부모 프로세스** (셸 프로세스 종료) | [[wiki/architecture/04_builtins_and_env_table]] |
