# Python 3.13 `os` 模块 API 文档（详细版）

## 说明

- 本文以 Python 3.13 官方文档为主进行整理，目标是做一份“适合项目中查阅”的中文 API 文档。
- `os` 模块非常大，并且存在大量平台专属 API。为了可读性，本文采用“按功能分组 + 同类函数一起讲解”的方式。
- 文中把 `exec*`、`spawn*`、`wait*`、`sched_*`、`O_*`、`EX_*` 这类同族 API 合并说明；这比逐个重复解释更适合工程使用。
- 示例默认尽量写成“可直接运行”的参考代码；涉及 `fork()`、`exec*()`、`setuid()`、`sched_*()`、`xattr`、`eventfd`、`timerfd` 等平台/权限相关 API 时，会明确说明适用平台。

---

## 1. 全部属性和方法清单

### 1.1 异常、协议、结果对象、子模块

- `os.error`
- `os.PathLike`
- `os.DirEntry`
- `os.stat_result`
- `os.statvfs_result`
- `os.terminal_size`
- `os.times_result`
- `os.uname_result`
- `os.sched_param`
- `os.path`

### 1.2 核心属性与能力探测属性

- `os.name`
- `os.environ`
- `os.environb`
- `os.supports_bytes_environ`
- `os.supports_dir_fd`
- `os.supports_effective_ids`
- `os.supports_fd`
- `os.supports_follow_symlinks`
- `os.curdir`
- `os.pardir`
- `os.sep`
- `os.altsep`
- `os.extsep`
- `os.pathsep`
- `os.defpath`
- `os.linesep`
- `os.devnull`

### 1.3 编码、路径与环境变量 API

- `os.fsencode()`
- `os.fsdecode()`
- `os.fspath()`
- `os.getenv()`
- `os.getenvb()`
- `os.get_exec_path()`
- `os.putenv()`
- `os.unsetenv()`
- `os.strerror()`

### 1.4 工作目录、文件与目录 API

- `os.ctermid()`
- `os.chdir()`
- `os.fchdir()`
- `os.getcwd()`
- `os.getcwdb()`
- `os.listdir()`
- `os.scandir()`
- `os.walk()`
- `os.fwalk()`
- `os.listdrives()`
- `os.listmounts()`
- `os.listvolumes()`
- `os.mkdir()`
- `os.makedirs()`
- `os.mkfifo()`
- `os.mknod()`
- `os.major()`
- `os.minor()`
- `os.makedev()`
- `os.remove()`
- `os.unlink()`
- `os.removedirs()`
- `os.rename()`
- `os.renames()`
- `os.replace()`
- `os.rmdir()`
- `os.readlink()`
- `os.link()`
- `os.symlink()`
- `os.pathconf()`
- `os.pathconf_names`
- `os.truncate()`
- `os.utime()`
- `os.access()`
- `os.chmod()`
- `os.chflags()`
- `os.chown()`
- `os.chroot()`
- `os.lchmod()`
- `os.lchflags()`
- `os.lchown()`
- `os.lstat()`
- `os.stat()`
- `os.statvfs()`
- `os.fstat()`
- `os.fstatvfs()`
- `os.umask()`
- `os.uname()`
- `os.startfile()`
- `os.add_dll_directory()`

### 1.5 文件描述符与底层 I/O API

- `os.fdopen()`
- `os.open()`
- `os.close()`
- `os.closerange()`
- `os.copy_file_range()`
- `os.device_encoding()`
- `os.dup()`
- `os.dup2()`
- `os.fdatasync()`
- `os.fpathconf()`
- `os.fsync()`
- `os.ftruncate()`
- `os.get_blocking()`
- `os.set_blocking()`
- `os.get_inheritable()`
- `os.set_inheritable()`
- `os.get_handle_inheritable()`
- `os.set_handle_inheritable()`
- `os.grantpt()`
- `os.isatty()`
- `os.lockf()`
- `os.login_tty()`
- `os.lseek()`
- `os.openpty()`
- `os.pipe()`
- `os.pipe2()`
- `os.posix_fallocate()`
- `os.posix_fadvise()`
- `os.posix_openpt()`
- `os.pread()`
- `os.preadv()`
- `os.ptsname()`
- `os.pwrite()`
- `os.pwritev()`
- `os.read()`
- `os.readv()`
- `os.sendfile()`
- `os.splice()`
- `os.sync()`
- `os.tcgetpgrp()`
- `os.tcsetpgrp()`
- `os.ttyname()`
- `os.unlockpt()`
- `os.write()`
- `os.writev()`
- `os.get_terminal_size()`

### 1.6 进程、执行、等待与权限相关 API

- `os.abort()`
- `os.getlogin()`
- `os.getpid()`
- `os.getppid()`
- `os.getuid()`
- `os.geteuid()`
- `os.getgid()`
- `os.getegid()`
- `os.getgroups()`
- `os.getresuid()`
- `os.getresgid()`
- `os.getpgid()`
- `os.getpgrp()`
- `os.getsid()`
- `os.getpriority()`
- `os.initgroups()`
- `os.kill()`
- `os.killpg()`
- `os.nice()`
- `os.pidfd_open()`
- `os.plock()`
- `os.popen()`
- `os.posix_spawn()`
- `os.posix_spawnp()`
- `os.register_at_fork()`
- `os.setns()`
- `os.unshare()`
- `os.setpgrp()`
- `os.setpgid()`
- `os.setpriority()`
- `os.setuid()`
- `os.seteuid()`
- `os.setgid()`
- `os.setegid()`
- `os.setgroups()`
- `os.setresuid()`
- `os.setresgid()`
- `os.setreuid()`
- `os.setregid()`
- `os.setsid()`
- `os.spawnl()`
- `os.spawnle()`
- `os.spawnlp()`
- `os.spawnlpe()`
- `os.spawnv()`
- `os.spawnve()`
- `os.spawnvp()`
- `os.spawnvpe()`
- `os.system()`
- `os.times()`
- `os.wait()`
- `os.waitid()`
- `os.waitpid()`
- `os.wait3()`
- `os.wait4()`
- `os.waitstatus_to_exitcode()`
- `os.fork()`
- `os.forkpty()`
- `os.execl()`
- `os.execle()`
- `os.execlp()`
- `os.execlpe()`
- `os.execv()`
- `os.execve()`
- `os.execvp()`
- `os.execvpe()`

### 1.7 调度、系统信息、随机数与 Linux 扩展 API

- `os.sched_get_priority_min()`
- `os.sched_get_priority_max()`
- `os.sched_getparam()`
- `os.sched_getscheduler()`
- `os.sched_rr_get_interval()`
- `os.sched_setparam()`
- `os.sched_setscheduler()`
- `os.sched_yield()`
- `os.sched_setaffinity()`
- `os.sched_getaffinity()`
- `os.cpu_count()`
- `os.process_cpu_count()`
- `os.getloadavg()`
- `os.confstr()`
- `os.confstr_names`
- `os.sysconf()`
- `os.sysconf_names`
- `os.getrandom()`
- `os.urandom()`
- `os.getxattr()`
- `os.listxattr()`
- `os.setxattr()`
- `os.removexattr()`
- `os.memfd_create()`
- `os.eventfd()`
- `os.eventfd_read()`
- `os.eventfd_write()`
- `os.timerfd_create()`
- `os.timerfd_settime()`
- `os.timerfd_gettime()`

### 1.8 常量族

#### 访问权限常量

- `os.F_OK`
- `os.R_OK`
- `os.W_OK`
- `os.X_OK`

#### 文件偏移常量

- `os.SEEK_SET`
- `os.SEEK_CUR`
- `os.SEEK_END`
- `os.SEEK_DATA`
- `os.SEEK_HOLE`

#### `open()` 旗标

- 通用: `os.O_RDONLY`, `os.O_WRONLY`, `os.O_RDWR`, `os.O_APPEND`, `os.O_CREAT`, `os.O_EXCL`, `os.O_TRUNC`
- Unix: `os.O_DSYNC`, `os.O_RSYNC`, `os.O_SYNC`, `os.O_NDELAY`, `os.O_NONBLOCK`, `os.O_NOCTTY`, `os.O_CLOEXEC`
- Windows: `os.O_BINARY`, `os.O_NOINHERIT`, `os.O_SHORT_LIVED`, `os.O_TEMPORARY`, `os.O_RANDOM`, `os.O_SEQUENTIAL`, `os.O_TEXT`
- macOS: `os.O_EVTONLY`, `os.O_FSYNC`, `os.O_SYMLINK`, `os.O_NOFOLLOW_ANY`
- 扩展: `os.O_ASYNC`, `os.O_DIRECT`, `os.O_DIRECTORY`, `os.O_NOFOLLOW`, `os.O_NOATIME`, `os.O_PATH`, `os.O_TMPFILE`, `os.O_SHLOCK`, `os.O_EXLOCK`

#### 锁、管道、向量 I/O、零拷贝常量

- `os.F_LOCK`, `os.F_TLOCK`, `os.F_ULOCK`, `os.F_TEST`
- `os.POSIX_FADV_NORMAL`, `os.POSIX_FADV_SEQUENTIAL`, `os.POSIX_FADV_RANDOM`, `os.POSIX_FADV_NOREUSE`, `os.POSIX_FADV_WILLNEED`, `os.POSIX_FADV_DONTNEED`
- `os.RWF_HIPRI`, `os.RWF_DSYNC`, `os.RWF_SYNC`, `os.RWF_APPEND`
- `os.SF_NODISKIO`, `os.SF_MNOWAIT`, `os.SF_SYNC`, `os.SF_NOCACHE`
- `os.SPLICE_F_MOVE`, `os.SPLICE_F_NONBLOCK`, `os.SPLICE_F_MORE`

#### 进程/等待/调度/优先级常量

- `os.P_WAIT`, `os.P_NOWAIT`, `os.P_NOWAITO`, `os.P_DETACH`, `os.P_OVERLAY`
- `os.PRIO_PROCESS`, `os.PRIO_PGRP`, `os.PRIO_USER`
- `os.PRIO_DARWIN_THREAD`, `os.PRIO_DARWIN_PROCESS`, `os.PRIO_DARWIN_BG`, `os.PRIO_DARWIN_NONUI`
- `os.P_PID`, `os.P_PGID`, `os.P_ALL`, `os.P_PIDFD`
- `os.WEXITED`, `os.WSTOPPED`, `os.WCONTINUED`, `os.WNOHANG`, `os.WNOWAIT`, `os.WUNTRACED`
- `os.CLD_EXITED`, `os.CLD_KILLED`, `os.CLD_DUMPED`, `os.CLD_TRAPPED`, `os.CLD_STOPPED`, `os.CLD_CONTINUED`
- `os.SCHED_OTHER`, `os.SCHED_BATCH`, `os.SCHED_IDLE`, `os.SCHED_SPORADIC`, `os.SCHED_FIFO`, `os.SCHED_RR`, `os.SCHED_RESET_ON_FORK`
- `os.PIDFD_NONBLOCK`

#### `posix_spawn`、namespace、匿名文件、事件与计时器常量

- `os.POSIX_SPAWN_OPEN`, `os.POSIX_SPAWN_CLOSE`, `os.POSIX_SPAWN_DUP2`, `os.POSIX_SPAWN_CLOSEFROM`
- `os.CLONE_FILES`, `os.CLONE_FS`, `os.CLONE_NEWCGROUP`, `os.CLONE_NEWIPC`, `os.CLONE_NEWNET`, `os.CLONE_NEWNS`, `os.CLONE_NEWPID`, `os.CLONE_NEWTIME`, `os.CLONE_NEWUSER`, `os.CLONE_NEWUTS`, `os.CLONE_SIGHAND`, `os.CLONE_SYSVSEM`, `os.CLONE_THREAD`, `os.CLONE_VM`
- `os.MFD_CLOEXEC`, `os.MFD_ALLOW_SEALING`, `os.MFD_HUGETLB`, `os.MFD_HUGE_SHIFT`, `os.MFD_HUGE_MASK`, `os.MFD_HUGE_64KB`, `os.MFD_HUGE_512KB`, `os.MFD_HUGE_1MB`, `os.MFD_HUGE_2MB`, `os.MFD_HUGE_8MB`, `os.MFD_HUGE_16MB`, `os.MFD_HUGE_32MB`, `os.MFD_HUGE_256MB`, `os.MFD_HUGE_512MB`, `os.MFD_HUGE_1GB`, `os.MFD_HUGE_2GB`, `os.MFD_HUGE_16GB`
- `os.EFD_CLOEXEC`, `os.EFD_NONBLOCK`, `os.EFD_SEMAPHORE`
- `os.TFD_NONBLOCK`, `os.TFD_CLOEXEC`, `os.TFD_TIMER_ABSTIME`, `os.TFD_TIMER_CANCEL_ON_SET`

#### 随机数、扩展属性、动态链接、退出码常量

- `os.GRND_RANDOM`, `os.GRND_NONBLOCK`
- `os.XATTR_CREATE`, `os.XATTR_REPLACE`
- `os.RTLD_LAZY`, `os.RTLD_NOW`, `os.RTLD_GLOBAL`, `os.RTLD_LOCAL`, `os.RTLD_NODELETE`, `os.RTLD_NOLOAD`, `os.RTLD_DEEPBIND`
- `os.EX_OK`, `os.EX_USAGE`, `os.EX_DATAERR`, `os.EX_NOINPUT`, `os.EX_NOUSER`, `os.EX_NOHOST`, `os.EX_UNAVAILABLE`, `os.EX_SOFTWARE`, `os.EX_OSERR`, `os.EX_OSFILE`, `os.EX_CANTCREAT`, `os.EX_IOERR`, `os.EX_TEMPFAIL`, `os.EX_PROTOCOL`, `os.EX_NOPERM`, `os.EX_CONFIG`, `os.EX_NOTFOUND`

---

## 2. 属性与方法说明

## 2.1 异常、协议、结果对象

| API                 | 说明                                 | 关键点                                                                       |
| ------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| `os.error`          | `OSError` 的别名                      | 老代码里常见；新代码通常直接捕获 `OSError`                                                |
| `os.PathLike`       | 路径协议抽象基类                           | 实现 `__fspath__()` 的对象都可作为路径参数                                             |
| `os.DirEntry`       | `scandir()` 迭代返回的目录项对象             | 提供 `name`、`path`、`inode()`、`is_dir()`、`is_file()`、`is_symlink()`、`stat()` |
| `os.stat_result`    | `stat()`/`fstat()`/`lstat()` 返回值类型 | 包含 `st_mode`、`st_size`、`st_mtime` 等文件元信息                                  |
| `os.statvfs_result` | `statvfs()`/`fstatvfs()` 返回值类型     | 文件系统容量与块大小等信息                                                             |
| `os.terminal_size`  | `get_terminal_size()` 返回值类型        | 有 `columns` 和 `lines` 两个命名属性                                              |
| `os.times_result`   | `times()` 返回值类型                    | 包含进程用户态、内核态和子进程时间                                                         |
| `os.uname_result`   | `uname()` 返回值类型                    | 包含 `sysname`、`nodename`、`release`、`version`、`machine`                     |
| `os.sched_param`    | 调度器参数对象                            | 主要用于 `sched_setparam()` / `sched_setscheduler()`                          |
| `os.path`           | 路径处理子模块                            | `join()`、`split()`、`exists()` 等都在这里，不在 `os` 顶层                            |

## 2.2 核心属性

| 属性                            | 说明                          | 常见用途                           |
| ----------------------------- | --------------------------- | ------------------------------ |
| `os.name`                     | 当前底层实现名，如 `nt`、`posix`      | 写平台分支                          |
| `os.environ`                  | 字符串环境变量映射                   | 读取/修改环境变量                      |
| `os.environb`                 | 字节串环境变量映射                   | 需要原始字节环境时使用，仅部分平台可用            |
| `os.supports_bytes_environ`   | 是否支持字节环境                    | 判断 `environb`/`getenvb()` 是否可用 |
| `os.supports_dir_fd`          | 哪些函数支持 `dir_fd`             | 做目录 fd 相对路径操作                  |
| `os.supports_effective_ids`   | 哪些函数支持 `effective_ids=True` | 多用于 `access()`                 |
| `os.supports_fd`              | 哪些函数允许传文件描述符代替路径            | 低级文件系统操作                       |
| `os.supports_follow_symlinks` | 哪些函数支持 `follow_symlinks`    | 符号链接安全处理                       |
| `os.curdir`                   | 当前目录的文本表示，通常是 `.`           | 组合路径时少量使用                      |
| `os.pardir`                   | 父目录的文本表示，通常是 `..`           | 组合路径时少量使用                      |
| `os.sep`                      | 主路径分隔符                      | 一般不用手拼，优先 `os.path.join()`     |
| `os.altsep`                   | 备用路径分隔符                     | Windows 上通常是 `/`               |
| `os.extsep`                   | 扩展名分隔符 `.`                  | 很少直接用                          |
| `os.pathsep`                  | `PATH` 内多个路径的分隔符            | 处理搜索路径                         |
| `os.defpath`                  | 没有 `PATH` 时的默认搜索路径          | `exec*p*` / `spawn*p*` 会用到     |
| `os.linesep`                  | 平台行结束符                      | 文本文件写入时通常仍推荐 `\n`              |
| `os.devnull`                  | 空设备路径                       | 丢弃输出，如重定向到 `/dev/null` 或 `nul` |

## 2.3 常量族速记

| 常量族                   | 含义                                         |
| --------------------- | ------------------------------------------ |
| `F_OK/R_OK/W_OK/X_OK` | `access()` 访问检查模式                          |
| `SEEK_*`              | `lseek()` 偏移基准                             |
| `O_*`                 | `open()` 的底层打开旗标                           |
| `P_*`                 | `spawn*()` 的执行模式                           |
| `EX_*`                | 进程退出码常量                                    |
| `PRIO_*`              | `getpriority()` / `setpriority()` 参数       |
| `POSIX_FADV_*`        | `posix_fadvise()` 访问提示                     |
| `RWF_*`               | `preadv()` / `pwritev()` 读写旗标              |
| `SF_*`                | `sendfile()` 平台特有旗标                        |
| `SPLICE_F_*`          | `splice()` 旗标                              |
| `SCHED_*`             | 调度策略常量                                     |
| `W*`、`CLD_*`、`P_*`    | `waitid()` / `waitpid()` 相关                |
| `POSIX_SPAWN_*`       | `posix_spawn()` 文件动作描述                     |
| `CLONE_*`             | `setns()` / `unshare()` Linux namespace 旗标 |
| `MFD_*`               | `memfd_create()` 旗标                        |
| `EFD_*`               | `eventfd()` 旗标                             |
| `TFD_*`               | `timerfd_*()` 旗标                           |
| `GRND_*`              | `getrandom()` 旗标                           |
| `XATTR_*`             | 扩展属性创建/替换模式                                |
| `RTLD_*`              | 动态加载器旗标                                    |

## 2.4 编码、路径与环境变量方法

| API                          | 作用            | 补充说明                        |
| ---------------------------- | ------------- | --------------------------- |
| `fsencode(path)`             | 路径转 `bytes`   | 用文件系统编码编码                   |
| `fsdecode(path)`             | 路径转 `str`     | 用文件系统编码解码                   |
| `fspath(path)`               | 取出路径对象的文件系统表示 | 支持 `str`、`bytes`、`PathLike` |
| `getenv(key, default=None)`  | 读取字符串环境变量     | 基于 `os.environ`             |
| `getenvb(key, default=None)` | 读取字节环境变量      | 仅部分 Unix 支持                 |
| `get_exec_path(env=None)`    | 获取可执行文件搜索路径列表 | 类似 shell 解析 `PATH`          |
| `putenv(k, v)`               | 设置环境变量        | 更推荐改 `os.environ`           |
| `unsetenv(k)`                | 删除环境变量        | 更推荐删 `os.environ[k]`        |
| `strerror(code)`             | 错误号转错误消息      | 便于日志友好展示                    |

### 参考示例：环境变量与路径编码

```python
import os
from pathlib import Path

def demo_env_and_path():
    root = Path.cwd()
    path_obj = root / "data" / "example.txt"

    # PathLike -> str/bytes
    print("fspath:", os.fspath(path_obj))
    print("fsencode:", os.fsencode(path_obj))
    print("fsdecode:", os.fsdecode(os.fsencode(path_obj)))

    # 环境变量推荐直接改 os.environ
    os.environ["APP_ENV"] = "dev"
    print("APP_ENV =", os.getenv("APP_ENV"))
    print("exec path =", os.get_exec_path()[:3])

    try:
        os.remove("__not_exists__")
    except OSError as exc:
        print("errno:", exc.errno)
        print("message:", os.strerror(exc.errno))

if __name__ == "__main__":
    demo_env_and_path()
```

## 2.5 工作目录、目录遍历、创建与删除

| API                                               | 作用                  | 关键点                              |
| ------------------------------------------------- | ------------------- | -------------------------------- |
| `chdir()` / `fchdir()`                            | 切换当前工作目录            | `fchdir()` 用目录 fd                |
| `getcwd()` / `getcwdb()`                          | 获取当前目录              | 前者返回 `str`，后者返回 `bytes`          |
| `listdir()`                                       | 返回名称列表              | 简单，快，但不带文件类型缓存                   |
| `scandir()`                                       | 返回 `DirEntry` 迭代器   | 大目录遍历时比 `listdir()+stat()` 更高效   |
| `walk()`                                          | 递归遍历目录树             | 产出 `(root, dirs, files)`         |
| `fwalk()`                                         | 带目录 fd 的递归遍历        | 产出 `(root, dirs, files, rootfd)` |
| `listdrives()` / `listvolumes()` / `listmounts()` | Windows 驱动器/卷/挂载点枚举 | Windows 专用                       |
| `mkdir()`                                         | 创建一级目录              | 已存在时抛 `FileExistsError`          |
| `makedirs()`                                      | 递归建目录               | `exist_ok=True` 时可忽略已存在          |
| `mkfifo()`                                        | 创建命名管道              | Unix                             |
| `mknod()`                                         | 创建设备文件/特殊文件         | Unix，需系统支持                       |
| `remove()` / `unlink()`                           | 删除文件                | 对目录使用会报错                         |
| `removedirs()`                                    | 递归删除空目录             | 会尝试向上删父目录                        |
| `rmdir()`                                         | 删除空目录               | 非空目录会失败                          |
| `rename()`                                        | 重命名/移动              | 是否覆盖目标因平台而异                      |
| `renames()`                                       | 递归建新路径并删旧空路径        | 历史 API，现代项目少用                    |
| `replace()`                                       | 原子替换目标文件            | 更新配置/输出文件很常用                     |

### 参考示例：目录创建、遍历、重命名与删除

```python
import os
import shutil
import tempfile
from pathlib import Path

def demo_dirs():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        src = root / "src"
        dst = root / "dst"
        nested = src / "a" / "b"

        os.makedirs(nested, exist_ok=True)
        (nested / "one.txt").write_text("hello", encoding="utf-8")
        (nested / "two.txt").write_text("world", encoding="utf-8")

        print("listdir(src):", os.listdir(src))

        with os.scandir(nested) as it:
            for entry in it:
                print("name:", entry.name, "is_file:", entry.is_file(), "size:", entry.stat().st_size)

        for current_root, dirs, files in os.walk(src):
            print("walk:", current_root, dirs, files)

        os.makedirs(dst, exist_ok=True)
        os.replace(nested / "one.txt", dst / "one.txt")
        print("moved exists:", (dst / "one.txt").exists())

        os.remove(dst / "one.txt")
        shutil.rmtree(src)
        print("src exists after rmtree:", src.exists())

if __name__ == "__main__":
    demo_dirs()
```

## 2.6 链接、路径配置与文件时间/大小

| API                                 | 作用                   | 关键点            |
| ----------------------------------- | -------------------- | -------------- |
| `readlink()`                        | 读取符号链接目标             | 不解析目标，只读链接文本   |
| `link()`                            | 创建硬链接                | 同一文件系统内使用更稳定   |
| `symlink()`                         | 创建符号链接               | Windows 可能需要权限 |
| `pathconf()` / `fpathconf()`        | 查询路径/文件描述符相关系统限制     | Unix           |
| `pathconf_names`                    | `pathconf()` 可接受名称映射 | Unix           |
| `truncate()` / `ftruncate()`        | 截断文件                 | 路径版与 fd 版      |
| `utime()`                           | 设置访问/修改时间            | 支持秒和纳秒         |
| `major()` / `minor()` / `makedev()` | 设备号拆分与组合             | 设备文件相关，Unix    |

### 参考示例：链接、文件时间与截断

```python
import os
import tempfile
import time
from pathlib import Path

def demo_links_and_times():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        file_path = root / "data.txt"
        file_path.write_text("0123456789", encoding="utf-8")

        # 截断到 5 字节
        os.truncate(file_path, 5)
        print("after truncate:", file_path.read_text(encoding="utf-8"))

        # 更新时间
        now_ns = time.time_ns()
        os.utime(file_path, ns=(now_ns, now_ns))
        st = os.stat(file_path)
        print("mtime_ns:", st.st_mtime_ns)

        # 符号链接示例（某些 Windows 环境可能需要管理员权限）
        link_path = root / "data-link.txt"
        try:
            os.symlink(file_path, link_path)
            print("readlink:", os.readlink(link_path))
        except (OSError, NotImplementedError) as exc:
            print("symlink unavailable:", exc)

if __name__ == "__main__":
    demo_links_and_times()
```

## 2.7 元数据、访问控制与权限

| API                                 | 作用             | 关键点               |
| ----------------------------------- | -------------- | ----------------- |
| `stat()`                            | 获取路径状态         | 默认跟随符号链接          |
| `lstat()`                           | 获取链接本身状态       | 不跟随符号链接           |
| `fstat()`                           | 获取文件描述符状态      | 低级 I/O 场景常用       |
| `statvfs()` / `fstatvfs()`          | 查询文件系统状态       | Unix              |
| `access()`                          | 按真实/有效身份检查可访问性 | 常用于预检查，但不能代替真正打开  |
| `chmod()`                           | 修改权限位          | Windows 只支持有限只读语义 |
| `chflags()` / `lchflags()`          | 修改文件 flags     | Unix              |
| `chown()` / `lchown()` / `fchown()` | 修改所有者/组        | Unix              |
| `chroot()`                          | 修改当前进程根目录      | Unix，管理员级操作       |
| `umask()`                           | 设置进程创建权限掩码     | 影响后续新建文件/目录       |

### `stat_result` 常用字段

- `st_mode`: 文件类型与权限位
- `st_ino`: inode 或文件索引号
- `st_dev`: 所在设备
- `st_nlink`: 硬链接数
- `st_uid` / `st_gid`: 所有者 UID/GID
- `st_size`: 文件大小
- `st_atime` / `st_mtime` / `st_ctime`: 秒级时间戳
- `st_atime_ns` / `st_mtime_ns` / `st_ctime_ns`: 纳秒级时间戳

### 参考示例：检查访问权限与修改权限

```python
import os
import stat
import tempfile
from pathlib import Path

def demo_stat_and_chmod():
    with tempfile.TemporaryDirectory() as tmp:
        file_path = Path(tmp) / "demo.txt"
        file_path.write_text("content", encoding="utf-8")

        info = os.stat(file_path)
        print("size:", info.st_size)
        print("mode:", oct(info.st_mode))
        print("readable:", os.access(file_path, os.R_OK))
        print("writable:", os.access(file_path, os.W_OK))

        # Unix 上更有意义；Windows 上主要映射只读位
        os.chmod(file_path, stat.S_IREAD)
        print("after chmod writable:", os.access(file_path, os.W_OK))

if __name__ == "__main__":
    demo_stat_and_chmod()
```

## 2.8 文件描述符与底层 I/O

| API                                                                       | 作用              | 关键点                   |
| ------------------------------------------------------------------------- | --------------- | --------------------- |
| `fdopen()`                                                                | 把文件描述符包装成文件对象   | 便于和高层 I/O 混用          |
| `open()`                                                                  | 底层打开文件，返回 fd    | 用 `O_*` 组合控制打开方式      |
| `close()` / `closerange()`                                                | 关闭一个或一段 fd      | `closerange()` 批量关闭更快 |
| `dup()` / `dup2()`                                                        | 复制 fd           | 重定向标准流时常见             |
| `get_inheritable()` / `set_inheritable()`                                 | 查询/设置 fd 是否可继承  | 子进程场景重要               |
| `get_handle_inheritable()` / `set_handle_inheritable()`                   | Windows 句柄继承控制  | Windows 专用            |
| `get_blocking()` / `set_blocking()`                                       | 查询/设置阻塞模式       | 管道/套接字/伪终端常用          |
| `lseek()`                                                                 | 移动文件偏移          | 配合 `SEEK_*`           |
| `read()` / `write()`                                                      | fd 级读写          | 只处理 `bytes`           |
| `pread()` / `pwrite()`                                                    | 指定偏移读写，不改变当前偏移  | Unix                  |
| `readv()` / `writev()`                                                    | 向量化多缓冲区 I/O     | Unix                  |
| `preadv()` / `pwritev()`                                                  | 指定偏移 + 多缓冲区 I/O | Unix                  |
| `pipe()` / `pipe2()`                                                      | 创建匿名管道          | 进程间通信                 |
| `openpty()` / `posix_openpt()` / `grantpt()` / `unlockpt()` / `ptsname()` | 伪终端接口           | Unix                  |
| `isatty()` / `ttyname()` / `tcgetpgrp()` / `tcsetpgrp()` / `login_tty()`  | TTY 控制          | Unix                  |
| `device_encoding()`                                                       | 查询终端/设备编码       | 文本 I/O 兼容性            |
| `fsync()` / `fdatasync()` / `sync()`                                      | 刷盘              | `fdatasync()` 不强制元数据  |
| `copy_file_range()` / `sendfile()` / `splice()`                           | 零拷贝/内核态转运       | 高性能复制/传输              |
| `posix_fallocate()` / `posix_fadvise()`                                   | 提前分配/访问提示       | Unix                  |
| `lockf()`                                                                 | POSIX 文件锁       | Unix                  |

### 参考示例：底层 fd 读写

```python
import os
import tempfile

def demo_low_level_io():
    fd, path = tempfile.mkstemp()
    try:
        os.write(fd, b"hello")
        os.lseek(fd, 0, os.SEEK_SET)
        data = os.read(fd, 5)
        print("read:", data)

        # 复制 fd 并包装成文件对象
        dup_fd = os.dup(fd)
        with os.fdopen(dup_fd, "rb") as f:
            f.seek(0)
            print("fdopen:", f.read())

        os.fsync(fd)
    finally:
        os.close(fd)
        os.remove(path)

if __name__ == "__main__":
    demo_low_level_io()
```

### 参考示例：管道与非阻塞模式

```python
import os

def demo_pipe():
    rfd, wfd = os.pipe()
    try:
        os.set_blocking(rfd, False)
        try:
            print("first read:", os.read(rfd, 10))
        except BlockingIOError:
            print("pipe has no data yet")

        os.write(wfd, b"ping")
        os.set_blocking(rfd, True)
        print("second read:", os.read(rfd, 10))
    finally:
        os.close(rfd)
        os.close(wfd)

if __name__ == "__main__":
    demo_pipe()
```

## 2.9 进程创建、执行与等待

### 基本进程信息

| API                                                                                                                                                                        | 作用                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `getlogin()`                                                                                                                                                               | 获取登录用户名                       |
| `getpid()` / `getppid()`                                                                                                                                                   | 当前进程 / 父进程 ID                 |
| `getuid()` / `geteuid()` / `getgid()` / `getegid()`                                                                                                                        | 真实/有效用户组 ID                   |
| `getgroups()`                                                                                                                                                              | 当前附加组列表                       |
| `getresuid()` / `getresgid()`                                                                                                                                              | 真实/有效/保存的 ID                  |
| `getpgid()` / `getpgrp()` / `getsid()`                                                                                                                                     | 进程组 / 会话信息                    |
| `getpriority()` / `setpriority()` / `nice()`                                                                                                                               | 进程优先级调整                       |
| `initgroups()`                                                                                                                                                             | 初始化用户组列表                      |
| `setuid()` / `seteuid()` / `setgid()` / `setegid()` / `setgroups()` / `setresuid()` / `setresgid()` / `setreuid()` / `setregid()` / `setsid()` / `setpgrp()` / `setpgid()` | 设置身份与会话关系，基本都属于 Unix 管理员级 API |

### 执行新程序：`exec*` 家族

| 变体       | 差异                |
| -------- | ----------------- |
| `execl*` | 参数逐个传入            |
| `execv*` | 参数以列表/元组传入        |
| `*p`     | 通过 `PATH` 搜索可执行文件 |
| `*e`     | 传入新的环境变量映射        |

关键点:

- `exec*` 会“替换当前进程”，成功后不会返回。
- 调用前要先刷新标准输出、文件缓冲。
- 新程序的 `argv[0]` 由你传入的第一个参数决定。

### 创建子进程：`spawn*`、`popen()`、`system()`、`posix_spawn*`

| API                                | 说明                                    |
| ---------------------------------- | ------------------------------------- |
| `spawn*()`                         | 历史进程创建 API；功能还在，但现代项目更常用 `subprocess` |
| `popen()`                          | `subprocess.Popen` 的简化文本包装            |
| `system()`                         | 调 shell 执行字符串命令                       |
| `posix_spawn()` / `posix_spawnp()` | POSIX 层的高效进程创建接口，Unix                 |

### 派生进程：`fork()` / `forkpty()` / `register_at_fork()`

- `fork()`：父进程返回子进程 pid，子进程返回 `0`。
- `forkpty()`：`fork()` + 伪终端。
- `register_at_fork()`：注册 fork 前后钩子。
- 这些接口只适合 Unix/POSIX，且在多线程程序里要非常谨慎。

### 终止与等待：`kill*` / `wait*`

| API                        | 说明                            |
| -------------------------- | ----------------------------- |
| `kill()`                   | 向进程发信号；Windows 语义与 Unix 不完全相同 |
| `killpg()`                 | 向进程组发信号                       |
| `wait()`                   | 等任意子进程结束                      |
| `waitpid()`                | 等指定 pid；Windows 也支持           |
| `waitid()`                 | 更细粒度等待，返回 `siginfo_t` 风格结果    |
| `wait3()` / `wait4()`      | 额外返回资源使用信息，Unix               |
| `waitstatus_to_exitcode()` | 把 wait 状态转成普通退出码              |
| `pidfd_open()`             | Linux pidfd 管理                |
| `plock()`                  | 段锁定，极少用                       |
| `abort()`                  | 发送 `SIGABRT` 给当前进程            |

### 参考示例：`popen()`、`system()`、`waitpid()`

```python
import os
import sys

def demo_process_apis():
    # popen: 获取子进程文本输出
    with os.popen(f'"{sys.executable}" -c "print(123)"') as pipe:
        output = pipe.read().strip()
        print("popen output:", output)

    # system: 直接让 shell 执行
    rc = os.system(f'"{sys.executable}" -c "print(456)"')
    print("system rc:", rc)

    # Windows 上 spawnv + waitpid 比较容易演示
    argv = [sys.executable, "-c", "import time; print('child'); time.sleep(0.2)"]
    handle_or_pid = os.spawnv(os.P_NOWAIT, sys.executable, argv)
    waited_pid, status = os.waitpid(handle_or_pid, 0)
    print("waitpid:", waited_pid, os.waitstatus_to_exitcode(status))

if __name__ == "__main__":
    demo_process_apis()
```

### 参考示例：`exec*` 家族差异说明

```python
"""
exec* 会替换当前进程，下面示例应单独放在一个测试脚本里运行。
运行后，本脚本后续代码不会再执行。
"""

import os
import sys

def demo_execv():
    os.execv(sys.executable, [sys.executable, "-c", "print('replaced process')"])

if __name__ == "__main__":
    demo_execv()
```

### 参考示例：`posix_spawn()` 文件动作（Unix）

```python
import os
import sys

def demo_posix_spawn():
    if not hasattr(os, "posix_spawn"):
        print("posix_spawn unavailable on this platform")
        return

    argv = [sys.executable, "-c", "print('hello from posix_spawn')"]
    pid = os.posix_spawn(sys.executable, argv, os.environ.copy())
    waited_pid, status = os.waitpid(pid, 0)
    print("pid:", waited_pid, "exit:", os.waitstatus_to_exitcode(status))

if __name__ == "__main__":
    demo_posix_spawn()
```

## 2.10 调度、系统信息与终端

| API                                                     | 作用               | 关键点                                |
| ------------------------------------------------------- | ---------------- | ---------------------------------- |
| `sched_get_priority_min()` / `sched_get_priority_max()` | 查询调度策略支持的优先级范围   | Unix                               |
| `sched_getparam()` / `sched_setparam()`                 | 获取/设置调度参数        | Unix                               |
| `sched_getscheduler()` / `sched_setscheduler()`         | 获取/设置调度策略        | Unix                               |
| `sched_rr_get_interval()`                               | RR 调度时间片         | Unix                               |
| `sched_yield()`                                         | 主动让出 CPU         | Unix                               |
| `sched_setaffinity()` / `sched_getaffinity()`           | 设置/读取 CPU 亲和性    | Linux 常见                           |
| `cpu_count()`                                           | 系统逻辑 CPU 数       | 不一定等于当前进程可用 CPU                    |
| `process_cpu_count()`                                   | 当前线程可用逻辑 CPU 数   | 3.13 新增                            |
| `getloadavg()`                                          | 系统 1/5/15 分钟平均负载 | Unix                               |
| `confstr()` / `confstr_names`                           | 字符串系统配置          | Unix                               |
| `sysconf()` / `sysconf_names`                           | 整数系统配置           | Unix                               |
| `times()`                                               | 当前进程时间统计         | Windows 只可靠填充部分字段                  |
| `get_terminal_size()`                                   | 查询终端尺寸           | 返回 `terminal_size(columns, lines)` |
| `uname()`                                               | 获取操作系统标识信息       | Unix                               |

### 参考示例：系统信息与终端信息

```python
import os

def demo_system_info():
    print("cpu_count:", os.cpu_count())

    if hasattr(os, "process_cpu_count"):
        print("process_cpu_count:", os.process_cpu_count())

    try:
        ts = os.get_terminal_size()
        print("terminal:", ts.columns, ts.lines)
    except OSError:
        print("terminal size unavailable in this environment")

    print("times:", os.times())

    if hasattr(os, "uname"):
        print("uname:", os.uname())

if __name__ == "__main__":
    demo_system_info()
```

## 2.11 随机数、扩展属性与 Linux 高级接口

### 随机数

| API                        | 说明                   |
| -------------------------- | -------------------- |
| `getrandom(size, flags=0)` | 从操作系统随机源读取随机字节，Linux |
| `urandom(size)`            | 返回适合加密用途的随机字节        |

### 扩展属性

| API             | 说明      |
| --------------- | ------- |
| `getxattr()`    | 读取扩展属性  |
| `listxattr()`   | 列出扩展属性名 |
| `setxattr()`    | 设置扩展属性  |
| `removexattr()` | 删除扩展属性  |

### Linux 高级接口

| API                                                            | 说明             |
| -------------------------------------------------------------- | -------------- |
| `memfd_create()`                                               | 创建匿名内存文件       |
| `eventfd()` / `eventfd_read()` / `eventfd_write()`             | 事件计数器 fd       |
| `timerfd_create()` / `timerfd_settime()` / `timerfd_gettime()` | 计时器 fd，3.13 新增 |
| `setns()` / `unshare()`                                        | namespace 相关   |

### 参考示例：安全随机数

```python
import os

def demo_random():
    print("urandom(16):", os.urandom(16).hex())

    if hasattr(os, "getrandom"):
        try:
            print("getrandom(16):", os.getrandom(16).hex())
        except OSError as exc:
            print("getrandom failed:", exc)

if __name__ == "__main__":
    demo_random()
```

### 参考示例：扩展属性（Linux）

```python
import os
import tempfile

def demo_xattr():
    if not hasattr(os, "setxattr"):
        print("xattr unavailable on this platform")
        return

    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        attr = "user.demo"
        os.setxattr(path, attr, b"hello")
        print("listxattr:", os.listxattr(path))
        print("getxattr:", os.getxattr(path, attr))
        os.removexattr(path, attr)
    finally:
        os.remove(path)

if __name__ == "__main__":
    demo_xattr()
```

### 参考示例：`eventfd()`（Linux）

```python
import os

def demo_eventfd():
    if not hasattr(os, "eventfd"):
        print("eventfd unavailable on this platform")
        return

    fd = os.eventfd(0, os.EFD_CLOEXEC)
    try:
        os.eventfd_write(fd, 3)
        print("counter:", os.eventfd_read(fd))
    finally:
        os.close(fd)

if __name__ == "__main__":
    demo_eventfd()
```

### 参考示例：`timerfd_*()`（Linux, Python 3.13）

```python
import os
import sys
import time

def demo_timerfd():
    required = ["timerfd_create", "timerfd_settime", "timerfd_gettime"]
    if not all(hasattr(os, name) for name in required):
        print("timerfd unavailable on this platform")
        return

    fd = os.timerfd_create(time.CLOCK_MONOTONIC, flags=os.TFD_CLOEXEC)
    try:
        # 第 1 秒触发，之后每 1 秒重复
        os.timerfd_settime(fd, initial=1.0, interval=1.0)
        raw = os.read(fd, 8)
        expirations = int.from_bytes(raw, byteorder=sys.byteorder)
        print("expirations:", expirations)
        print("current setting:", os.timerfd_gettime(fd))
    finally:
        os.close(fd)

if __name__ == "__main__":
    demo_timerfd()
```

---

## 3. 项目中最常用的 `os` API 建议

### 3.1 高频常用

- 路径/环境: `fspath()`, `getenv()`, `environ`
- 目录文件: `listdir()`, `scandir()`, `walk()`, `mkdir()`, `makedirs()`, `remove()`, `replace()`
- 文件元信息: `stat()`, `lstat()`, `utime()`
- 进程: `getpid()`, `system()`, `popen()`, `waitpid()`
- 随机数: `urandom()`

### 3.2 现代项目的取舍建议

- 处理路径时，优先 `pathlib`，必要时再落到 `os`。
- 进程管理优先 `subprocess`，只在需要非常底层的行为时使用 `spawn*()`、`exec*()`、`fork()`、`posix_spawn()`。
- 文件读写优先内置 `open()`，只有在需要 fd、零拷贝、伪终端、inheritability、non-blocking 之类能力时再用 `os.open()` 和 fd API。
- 递归扫描目录优先 `scandir()` / `walk()`。
- 需要安全随机数时优先 `urandom()`；Linux 特殊场景再考虑 `getrandom()`。

---

## 4. 参考资料

- Python 3.13 中文官方文档: https://docs.python.org/zh-cn/3.13/library/os.html
- Python 3.13 英文官方文档: https://docs.python.org/3.13/library/os.html
- 当前工作环境中的本地 `os` 模块公开成员清单是通过 `dir(os)` 与 `inspect.signature()` 做了补充核对，但平台仅代表本机 Windows/Python 3.12 运行环境，不能替代 3.13 官方文档的可用性说明。
