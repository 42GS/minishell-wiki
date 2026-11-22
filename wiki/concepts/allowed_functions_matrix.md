# Allowed Functions Technical Matrix (53 Functions)

> **Navigation**: [[index|Hub: Index]] | **Architecture Mappings**: [[wiki/architecture/02_execution_engine_and_ipc|Execution Engine]] | [[wiki/architecture/03_signal_dispatcher_and_state_machine|Signal Dispatcher]]  
> **Deep Dives**: [[wiki/concepts/deep_dive_process_ipc_and_fd|Process & FD Deep Dive]] | [[wiki/concepts/deep_dive_signals_and_concurrency|Signals & Concurrency Deep Dive]]  
> **Source**: [[raw/subject/en.subject|en.subject.md]] (Chapter III) | **Man Pages Archive**: `raw/manpages/*.txt`  
> **Verification**: macOS Clang / POSIX.1-2017 Manual

---

## 1. Process Lifecycle & IPC Functions

| 함수명 | 헤더 | 시그니처 | Async-Signal-Safe | 핵심 역할 및 Minishell 구현 시 주의점 | 연계 문서 |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `fork` | `<unistd.h>` | `pid_t fork(void);` | **YES** | 자식 프로세스 복제 생성. 반환값(자식은 0, 부모는 자식 PID, 실패 -1) 분기 처리. FD 테이블 복제 시 유의. | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |
| `execve` | `<unistd.h>` | `int execve(const char *path, char *const argv[], char *const envp[]);` | **YES** | 새로운 바이너리로 프로세스 이미지 교체. 성공 시 반환하지 않음. 실패 시(파일 없음 127, 권한 없음 126) 메모리 해제 및 exit. | [[wiki/architecture/02_execution_engine_and_ipc]] |
| `wait` | `<sys/wait.h>` | `pid_t wait(int *stat_loc);` | **YES** | 임의의 자식 프로세스 종료 대기. 파이프라인에서 순서 보장이 어려우므로 `waitpid` 우선 사용. | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |
| `waitpid` | `<sys/wait.h>` | `pid_t waitpid(pid_t pid, int *stat_loc, int options);` | **YES** | 특정 PID의 종료 상태(`WIFEXITED`, `WEXITSTATUS`, `WIFSIGNALED`, `WTERMSIG`)를 정확히 수집. `WNOHANG` 옵션 활용 가능. | [[wiki/architecture/02_execution_engine_and_ipc]] |
| `wait3` | `<sys/wait.h>` | `pid_t wait3(int *stat_loc, int options, struct rusage *rusage);` | NO | 자식 프로세스 자원 사용량 통계 포함 대기 (`waitpid`가 권장됨). | - |
| `wait4` | `<sys/wait.h>` | `pid_t wait4(pid_t pid, int *stat_loc, int options, struct rusage *rusage);` | NO | 특정 PID 대상 자원 사용량 포함 대기. | - |
| `pipe` | `<unistd.h>` | `int pipe(int fildes[2]);` | **YES** | 단방향 IPC 파이프 생성 (`fildes[0]` read end, `fildes[1]` write end). 미사용 end를 즉시 `close`하지 않으면 EOF 감지 불가로 파이프라인 행(hang) 발생. | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |
| `kill` | `<signal.h>` | `int kill(pid_t pid, int sig);` | **YES** | 프로세스 또는 프로세스 그룹에 시그널 송신. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `exit` | `<stdlib.h>` | `void exit(int status);` | NO (`_exit` 아님) | 프로세스 정상 종료 및 표준 스트림 플러시. 단 `fork` 후 자식 프로세스 실패 시에는 stdio 버퍼 중복 플러시 방지 필요. | [[raw/specs/bash_exit_status]] |

---

## 2. File Descriptors & Filesystem Functions

| 함수명 | 헤더 | 시그니처 | Async-Signal-Safe | 핵심 역할 및 Minishell 구현 시 주의점 | 연계 문서 |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `open` | `<fcntl.h>` | `int open(const char *path, int oflag, ...);` | **YES** | 리다이렉션 파일 오픈. `O_RDONLY`(`<`), `O_WRONLY &#124; O_CREAT &#124; O_TRUNC`(`>`), `O_WRONLY &#124; O_CREAT &#124; O_APPEND`(`>>`). 권한 `0644`. | [[wiki/architecture/02_execution_engine_and_ipc]] |
| `close` | `<unistd.h>` | `int close(int fildes);` | **YES** | 사용 완료된 FD 즉시 회수. FD 누수(leak) 방지의 핵심. | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |
| `read` | `<unistd.h>` | `ssize_t read(int fildes, void *buf, size_t nbyte);` | **YES** | Here-doc 및 파일 읽기. | [[wiki/architecture/01_parser_and_ast]] |
| `write` | `<unistd.h>` | `ssize_t write(int fildes, const void *buf, size_t nbyte);` | **YES** | 표준 출력/에러 메시지 출력. 시그널 핸들러 내부 출력의 유일한 안전 수단. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `dup` | `<unistd.h>` | `int dup(int fildes);` | **YES** | 가장 낮은 번호의 사용 가능한 FD로 복제. 원본 stdin/stdout 백업 시 사용. | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |
| `dup2` | `<unistd.h>` | `int dup2(int fildes, int fildes2);` | **YES** | `fildes`를 지정된 `fildes2`(0: stdin, 1: stdout 등)로 원자적 복제. 리다이렉션의 핵심. | [[wiki/architecture/02_execution_engine_and_ipc]] |
| `access` | `<unistd.h>` | `int access(const char *path, int mode);` | **YES** | 파일 존재 여부(`F_OK`), 실행 권한(`X_OK`), 읽기/쓰기 권한 검사. | [[wiki/requirements/mandatory]] |
| `unlink` | `<unistd.h>` | `int unlink(const char *path);` | **YES** | 임시 파일(Here-doc 임시 파일 등) 생성 후 즉시 삭제 시 활용. | - |
| `stat` | `<sys/stat.h>` | `int stat(const char *path, struct stat *buf);` | **YES** | 파일 정보(디렉토리 여부 `S_ISDIR`) 조회. 디렉토리 실행 시도 감지. | [[wiki/requirements/evaluation_matrix]] |
| `lstat` | `<sys/stat.h>` | `int lstat(const char *path, struct stat *buf);` | **YES** | 심볼릭 링크 자체의 정보 조회. | - |
| `fstat` | `<sys/stat.h>` | `int fstat(int fildes, struct stat *buf);` | **YES** | 열려있는 FD의 파일 정보 조회. | - |
| `opendir` | `<dirent.h>` | `DIR *opendir(const char *filename);` | NO | 디렉토리 스트림 열기 (보너스 와일드카드 `*` 구현에 사용). | [[wiki/requirements/bonus]] |
| `readdir` | `<dirent.h>` | `struct dirent *readdir(DIR *dirp);` | NO | 디렉토리 엔트리 순차 조회 (`d_name`). | [[wiki/requirements/bonus]] |
| `closedir` | `<dirent.h>` | `int closedir(DIR *dirp);` | NO | 디렉토리 스트림 닫기. 메모리/FD 누수 방지. | [[wiki/requirements/bonus]] |
| `getcwd` | `<unistd.h>` | `char *getcwd(char *buf, size_t size);` | NO | 현재 작업 디렉토리 경로 획득. `pwd` 빌트인 및 `PWD` 갱신에 사용. | [[wiki/requirements/mandatory]] |
| `chdir` | `<unistd.h>` | `int chdir(const char *path);` | **YES** | 작업 디렉토리 변경. `cd` 빌트인에 사용. | [[wiki/concepts/deep_dive_process_ipc_and_fd]] |

---

## 3. Signal & Terminal Functions

| 함수명 | 헤더 | 시그니처 | Async-Signal-Safe | 핵심 역할 및 Minishell 구현 시 주의점 | 연계 문서 |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `signal` | `<signal.h>` | `sig_t signal(int sig, sig_t func);` | NO (구현체 종속) | 단순 시그널 핸들러 등록. 가급적 `sigaction` 사용 권장. | - |
| `sigaction` | `<signal.h>` | `int sigaction(int sig, const struct sigaction *act, struct sigaction *oact);` | **YES** | 신뢰성 있는 시그널 등록(`SA_RESTART` 플래그 제어). | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `sigemptyset` | `<signal.h>` | `int sigemptyset(sigset_t *set);` | **YES** | 시그널 마스크 집합 초기화. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `sigaddset` | `<signal.h>` | `int sigaddset(sigset_t *set, int signo);` | **YES** | 특정 시그널 마스크 추가. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `tcgetattr` | `<termios.h>` | `int tcgetattr(int fildes, struct termios *termios_p);` | **YES** | 터미널 속성 읽기. 에코 플래그(`ECHOCTL`) 제어에 사용. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `tcsetattr` | `<termios.h>` | `int tcsetattr(int fildes, int optional_actions, const struct termios *termios_p);` | **YES** | 터미널 속성 설정 (`TCSANOW`). `Ctrl+C` 입력 시 `^C` 화면 출력 억제. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `ioctl` | `<sys/ioctl.h>` | `int ioctl(int fildes, unsigned long request, ...);` | NO (디바이스 종속) | 장치 제어 I/O. 윈도우 사이즈 등 조회 가능. | - |
| `isatty` | `<unistd.h>` | `int isatty(int fildes);` | **YES** | FD가 유효한 터미널에 연결되어 있는지 확인 (대화형 모드 판정). | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `ttyname` | `<unistd.h>` | `char *ttyname(int fildes);` | NO | 터미널 디바이스 경로명 획득. | - |
| `ttyslot` | `<unistd.h>` | `int ttyslot(void);` | NO | tty 슬롯 인덱스 조회. | - |

---

## 4. Readline Library (대화형 프롬프트 & 히스토리)

| 함수명 | 헤더 | 역할 및 주의점 | 연계 문서 |
| :--- | :--- | :--- | :--- |
| `readline` | `<readline/readline.h>` | 사용자 입력을 읽어 동적 할당된 문자열 반환 (사용 후 반드시 `free`). 내부 캐시로 인한 라이브러리 레벨의 릭은 서브젝트에서 허용. | [[wiki/requirements/mandatory]] |
| `rl_clear_history` | `<readline/history.h>` | 히스토리 리스트 전체 해제 (셸 종료 시 클린업). | [[wiki/architecture/01_parser_and_ast]] |
| `rl_on_new_line` | `<readline/readline.h>` | 시그널 핸들러 등에서 새 라인으로 이동했음을 readline에 알림. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `rl_replace_line` | `<readline/readline.h>` | 현재 입력 중인 라인 버퍼 내용을 특정 텍스트(예: `""`)로 교체. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `rl_redisplay` | `<readline/readline.h>` | 현재 프롬프트와 버퍼를 터미널 화면에 다시 렌더링. | [[wiki/architecture/03_signal_dispatcher_and_state_machine]] |
| `add_history` | `<readline/history.h>` | 입력된 명령어를 히스토리 큐에 추가. 빈 문자열이나 Here-doc 입력은 추가 제외. | [[wiki/requirements/mandatory]] |

---

## 5. Memory, Environment & Error Utilities

| 함수명 | 헤더 | 역할 및 주의점 | 연계 문서 |
| :--- | :--- | :--- | :--- |
| `malloc` / `free` | `<stdlib.h>` | 힙 메모리 동적 할당 및 해제. **Zero Leak 원칙 준수**. 시그널 핸들러 내에서 호출 절대 금지(Non-reentrant). | [[wiki/concepts/deep_dive_signals_and_concurrency]] |
| `printf` | `<stdio.h>` | 포맷 스트림 출력. 디버깅 및 빌트인 출력에 사용. 시그널 핸들러 내부 사용 금지. | [[wiki/concepts/deep_dive_signals_and_concurrency]] |
| `getenv` | `<stdlib.h>` | 부모 프로세스의 환경변수 조회. minishell 시작 시 내부 환경변수 딕셔너리로 복제(Clone)하여 관리. | [[wiki/architecture/02_execution_engine_and_ipc]] |
| `strerror` | `<string.h>` | `errno`에 대응하는 시스템 에러 메시지 문자열 획득. | - |
| `perror` | `<stdio.h>` | 시스템 에러 메시지를 `stderr`에 출력. | [[wiki/architecture/02_execution_engine_and_ipc]] |
| `tgetent`, `tgetflag`, `tgetnum`, `tgetstr`, `tgoto`, `tputs` | `<term.h>` | Termcaps 터미널 제어 함수군. 터미널 커서 조작 및 화면 제어용. | - |
