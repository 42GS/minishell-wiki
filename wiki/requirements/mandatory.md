# Minishell Mandatory Requirements Specification

> **Source**: [en.subject.md](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/subject/en.subject.md) (v7.1)  
> **Reference**: [Bash Reference Manual](file:///Users/yong/Projects/gdtknight/42/minishell-wiki/raw/specs/bash_man.txt)  
> **Status**: Ingested & Verified

---

## 1. Program & Build Specifications

| 항목 | 요구사항 규격 | 비고 |
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
> **단 하나의 전역 변수만 허용되며, 오직 수신된 시그널 번호(int)만을 저장할 수 있다.**  
> - "Avoid using more than one global variable to indicate a received signal."  
> - "This global variable cannot provide any other information or data access than the number of a received signal."  
> - `t_data`나 구조체 포인터를 전역 변수에 담는 행위는 **치팅/규정 위반으로 즉시 0점 처리**된다.

---

## 3. Core Shell Features

### 3.1 Prompt & History
- 명령어 입력을 대기할 때 새로운 프롬프트(`minishell$ ` 등)를 표시.
- 입력된 명령어를 히스토리에 기록(`add_history`).
- **예외**: Here-doc (`<<`) 입력 시에는 히스토리를 갱신하지 않아도 됨(Subject 명시).

### 3.2 Executable Search & Execution
- 절대 경로(`/bin/ls`), 상대 경로(`./my_prog`)를 통한 실행 파일 직접 실행.
- `PATH` 환경변수를 파싱하여 콜론(`:`)으로 구분된 디렉토리 목록에서 실행 파일 탐색.
- 에러 처리 규격 (Bash 호환):
  - 파일 미존재: `command not found` (Exit status 127)
  - 실행 권한 없음 / 디렉토리 실행 시도: `Permission denied` / `Is a directory` (Exit status 126)

### 3.3 Quoting Rules (따옴표 처리)
- **닫히지 않은 따옴표**: 해석하지 않음 (과제 요구사항 외의 백슬래시(`\`)나 세미콜론(`;`) 같은 특수문자 미해석).
- **싱글 쿼트 (`'`)**: 감싸진 문자열 내부의 모든 메타문자(`$`, `\`, `"` 등)의 특수 의미를 무효화(Literal 처리).
- **더블 쿼트 (`"`)**: 감싸진 문자열 내부의 메타문자를 무효화하되, **환경변수 확장(`$`)은 허용**.

### 3.4 Expansions (변수 및 상태 코드 확장)
- `$VAR`: 환경변수 이름 매칭 후 해당 값으로 확장. 정의되지 않은 변수는 빈 문자열로 치환.
- `$?`: 가장 최근에 실행된 포그라운드 파이프라인의 종료 상태 코드(Exit Status, 0~255)로 확장.

### 3.5 Redirections (입출력 재지향)
1. `<`: 입력 리다이렉션 (Input file 열기, `O_RDONLY`).
2. `>`: 출력 리다이렉션 (Truncate 모드, `O_WRONLY | O_CREAT | O_TRUNC`, 0644).
3. `>>`: 출력 추가 리다이렉션 (Append 모드, `O_WRONLY | O_CREAT | O_APPEND`, 0644).
4. `<< DELIMITER`: Here-document. 사용자가 `DELIMITER`만 적힌 라인을 입력할 때까지 입력을 수집.

### 3.6 Pipelines (`|`)
- 이전 명령어의 `stdout`을 다음 명령어의 `stdin`으로 연결.
- 모든 파이프라인 명령어는 자식 프로세스로 병렬 포크(`fork`)되어 동시 실행.
- 파이프라인의 최종 반환값은 **마지막으로 실행된 명령어의 종료 상태 코드**.

### 3.7 Signal Handling (대화형 및 비대화형)
- **Interactive Prompt 대기 중**:
  - `Ctrl + C` (`SIGINT`): 새 라인으로 이동하여 새 프롬프트 출력 (`rl_on_new_line`, `rl_redisplay`). 종료 코드는 130 (128 + 2).
  - `Ctrl + D` (`EOF`): 셸을 정상 종료 (`exit`).
  - `Ctrl + \` (`SIGQUIT`): 아무 반응 없음 (무시).
- **자식 프로세스 실행 중 (Foreground Command)**:
  - `Ctrl + C`: 자식 프로세스가 `SIGINT`로 종료되며 셸이 새 라인을 출력하고 `$? = 130`.
  - `Ctrl + \`: 자식 프로세스가 `SIGQUIT`로 종료되며 `Quit (core dumped)\n` 출력 후 `$? = 131`.
- **Here-doc 입력 중**:
  - `Ctrl + C`: 즉시 입력을 중단하고 프롬프트 복귀, `$? = 130`.

---

## 4. Built-in Utilities (7종)

외부 프로세스 포크 없이 부모 셸의 상태를 변경해야 하거나 내장 실행되는 유틸리티:

| 빌트인 | 요구사항 명세 | 부모 프로세스 직접 실행 필요성 |
| :--- | :--- | :--- |
| `echo` | `-n` 옵션 지원 (연속된 `-nnnn` 지원 포함) | 서브셸/부모 무관 |
| `cd` | 상대 또는 절대 경로만 지원 (옵션 없음) | **반드시 부모 프로세스** (작업 디렉토리 변경) |
| `pwd` | 옵션 없음 (현재 작업 디렉토리 출력) | 서브셸/부모 무관 |
| `export` | 옵션 없음 (환경변수 설정 및 미인자 호출 시 목록 출력) | **반드시 부모 프로세스** (환경변수 테이블 갱신) |
| `unset` | 옵션 없음 (환경변수 제거) | **반드시 부모 프로세스** (환경변수 테이블 갱신) |
| `env` | 옵션/인자 없음 (현재 환경변수 목록 출력) | 서브셸/부모 무관 |
| `exit` | 옵션 없음 (종료 코드 인자 지정 가능, 0~255 오버플로우 처리) | **반드시 부모 프로세스** (셸 프로세스 종료) |
