# Minishell Evaluation Matrix & Defense Checklist

> **Navigation**: [[index|Hub: Index]] | [[wiki/requirements/mandatory|Mandatory Spec]] | [[wiki/requirements/bonus|Bonus Spec]]  
> **Source**: [[raw/evalhub/minishell_eval_scale|42 EvalHub Minishell Scale]]  
> **Purpose**: 평가 시트의 모든 질문 및 채점 항목을 사전 검증하고 방어할 수 있도록 1:1 매핑한 체크리스트.

---

## 1. Mandatory Evaluation Matrix

| 분류 | 평가 항목 | 테스트 케이스 및 검증 내용 | 합격 기준 | 담당 아키텍처 모듈 |
| :--- | :--- | :--- | :--- | :--- |
| **빌드** | `Compile` | `make -n`으로 `-Wall -Wextra -Werror` 확인<br/>`make` 실행 시 컴파일 에러 없음<br/>연속 `make` 시 **re-link 발생 금지** | 정상 컴파일 및 Makefile No-relink 준수 | [[wiki/requirements/mandatory]] |
| **기본 실행** | `Simple Command & global variables` | `/bin/ls` 절대 경로 실행<br/>단일 전역 변수 개수 및 용도 소명 (시그널 번호 전용)<br/>빈 입력(Enter), 공백/탭만 입력 | 크래시 없이 정상 프롬프트 복귀, 전역 변수 1개 규칙 증명 | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| **인자 전달** | `Arguments` | `/bin/ls -la /tmp` 등 따옴표 없는 다중 인자 실행 반복 | 인자가 `execve`의 `argv`에 정확히 분리되어 전달 | [[wiki/architecture/01_parser_and_ast]] |
| **빌트인** | `echo` | `echo`, `echo hello`, `echo -n hello`, `echo -nnnn -n hello world` | `-n` 옵션 정상 동작, 개행 생략 여부 일치 | [[wiki/architecture/04_builtins_and_env_table]] |
| **빌트인** | `exit` | `exit`, `exit 42`, `exit 259` (오버플로우 3), `exit numeric_error` | 정확한 종료 코드 전달 및 비숫자 인자 에러 처리 | [[wiki/architecture/04_builtins_and_env_table]] |
| **종료 상태** | `Return value of a process` | `/bin/ls`<br/>`echo &#36;?` 출력 확인<br/>`/bin/ls nonexistent` 실행 후 `echo &#36;?` 에러 코드 비교<br/>`expr &#36;? + &#36;?` 복수 확장 | Bash와 동일한 종료 상태 코드 출력 및 인라인 복수 확장 지원 | [[wiki/architecture/02_execution_engine_and_ipc]] |
| **시그널** | `Signals` | 빈 프롬프트에서 `Ctrl+C` (새 프롬프트)<br/>빈 프롬프트에서 `Ctrl+\` (무반응)<br/>빈 프롬프트에서 `Ctrl+D` (셸 종료)<br/>글자 입력 후 `Ctrl+C` (라인 버퍼 초기화 후 새 프롬프트)<br/>`cat` 등 블로킹 명령 중 `Ctrl+C`, `Ctrl+\` | 버퍼 오염 방지, `&#36;?` 값 130/131 정확 설정, 블로킹 프로세스 정상 종료 | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| **따옴표** | `Double Quotes` | `echo "cat lol.c &#124; cat > lol.c"`<br/>인자 내부 공백 및 환경변수 확장 유지 | 메타문자 무효화, 환경변수만 치환 | [[wiki/architecture/01_parser_and_ast]] |
| **따옴표** | `Single Quotes` | `echo '&#36;USER'` 실행 시 `&#36;USER` 문자 그대로 출력<br/>모든 특수문자 리터럴 취급 | 어떠한 확장도 발생하지 않음 | [[raw/specs/bash_quoting]] |
| **환경변수** | `env` | `env` 실행 시 현재 환경변수 출력 | `PATH`, `USER`, `PWD` 등 출력 확인 | [[wiki/architecture/04_builtins_and_env_table]] |
| **환경변수** | `export` | `export TEST=123`<br/>`export` 무인자 실행 시 정렬 목록 출력<br/>새 환경변수가 자식 프로세스에 상속되는지 확인 | 환경변수 테이블 추가 및 정렬 출력 | [[wiki/architecture/04_builtins_and_env_table]] |
| **환경변수** | `unset` | `unset TEST`<br/>`env`에서 사라졌는지 확인 | 정상 삭제 | [[wiki/architecture/04_builtins_and_env_table]] |
| **디렉토리** | `cd` & `pwd` | `cd ..`, `cd /tmp`, `cd -`, `pwd` 확인<br/>`PWD` 및 `OLDPWD` 환경변수 갱신 확인 | 작업 디렉토리 실제 이동 및 환경변수 동기화 | [[wiki/architecture/04_builtins_and_env_table]] |
| **경로 탐색** | `Relative Path` & `Environment path` | `./my_script`<br/>`unset PATH` 후 `ls` 실행 시 `No such file or directory` 에러 확인<br/>`PATH` 복구 후 명령 실행 | PATH 파싱 탐색 및 상대 경로 실행 정확성 | [[wiki/architecture/02_execution_engine_and_ipc]] |
| **리다이렉션** | `Redirection` | `echo hello > test.txt`<br/>`cat < test.txt`<br/>`echo world >> test.txt`<br/>`cat << EOF` heredoc 테스트 | 파일 입출력 redirection 및 heredoc 정상 종료 | [[wiki/architecture/02_execution_engine_and_ipc]] |
| **파이프** | `Pipes` | `cat file &#124; grep word &#124; wc -l`<br/>파이프라인 프로세스 간 동시 실행 및 파이프 누수(FD leak) 방지 | 모든 자식 프로세스 정상 대기(`waitpid`), 파이프 닫힘 | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |
| **복합 검증** | `Go Crazy and history` | 긴 명령어, 복잡한 파이프라인, 비정상적 인자 조합 반복 실행<br/>방향키 위/아래로 history 정상 탐색 확인 | 세그폴트 및 메모리 릭 없이 완벽 동작 | [[wiki/architecture/01_parser_and_ast]] |

---

## 2. Bonus Evaluation Matrix

| 분류 | 평가 항목 | 테스트 케이스 및 검증 내용 | 합격 기준 | 담당 아키텍처 모듈 |
| :--- | :--- | :--- | :--- | :--- |
| **논리 연산자** | `And, Or` | `true && echo yes`<br/>`false && echo no`<br/>`false &#124;&#124; echo fallback`<br/>`true &#124;&#124; echo skipped`<br/>`false && echo A &#124;&#124; echo B` | Bash 단락 평가 규칙과 100% 일치 | [[wiki/architecture/01_parser_and_ast]] |
| **괄호 우선순위** | `Parentheses Priority` | `(exit 1) &#124;&#124; echo success`<br/>`(cd /tmp && pwd); pwd`<br/>`echo A && (echo B &#124;&#124; echo C)` | 서브셸 환경 격리(CWD/환경변수 원복) 및 우선순위 분기 | [[wiki/architecture/02_execution_engine_and_ipc]] |
| **와일드카드** | `Wildcard` | `echo *`<br/>`echo *.c`<br/>`echo nonexistent*` (매칭 실패 시 패턴 유지)<br/>숨김 파일 제외 확인 | 사전순 정렬 출력, Bash CWD globbing 호환 | [[wiki/concepts/allowed_functions_matrix]] |
| **서프라이즈** | `Surprise! (or not...)` | `echo "'&#36;USER'"` 실행 시 `'username'` 출력<br/>`echo '"&#36;USER"'` 실행 시 `"&#36;USER"` 출력 | 중첩 따옴표 파싱 및 치환 규칙 엄격 준수 | [[wiki/concepts/deep_dive_lexer_parser_ast]] |
