# 关于Linux core文件

## core文件的简单介绍
在一个程序崩溃时，它一般会在指定目录下生成一个core文件。core文件仅仅是一个内存映象(同时加上调试信息)，主要是用来调试的。

### 开启或关闭core文件的生成
用以下命令来阻止系统生成core文件:
```
ulimit -c 0
```
下面的命令可以检查生成core文件的选项是否打开:
```
ulimit -a
```
该命令将显示所有的用户定制，其中选项-a代表“all”。

也可以修改系统文件来调整core选项
在/etc/profile通常会有这样一句话来禁止产生core文件，通常这种设置是合理的:
```shell
# No core files by default
ulimit -S -c 0 > /dev/null 2>&1
```
但是在开发过程中有时为了调试问题，还是需要在特定的用户环境下打开core文件产生的设置
在用户的~/.bash_profile里加上`ulimit -c unlimited`来让特定的用户可以产生core文件
如果`ulimit -c 0`则也是禁止产生core文件，而`ulimit -c 1024`则限制产生的core文件的大小不能超过1024kb

## 设置Core Dump的核心转储文件目录和命名规则
/proc/sys/kernel/core_uses_pid可以控制产生的core文件的文件名中是否添加pid作为扩展，如果添加则文件内容为1，否则为0

/proc/sys/kernel/core_pattern可以设置格式化的core文件保存位置或文件名，比如原来文件内容是core-%e, 可以这样修改:
```
echo "/corefile/core-%e-%p-%t" > /proc/sys/kernel/core_pattern
```
将会控制所产生的core文件会存放到/corefile目录下，产生的文件名为core-命令名-pid-时间戳
以下是参数列表:
```
    %p - insert pid into filename 添加pid
    %u - insert current uid into filename 添加当前uid
    %g - insert current gid into filename 添加当前gid
    %s - insert signal that caused the coredump into the filename 添加导致产生core的信号
    %t - insert UNIX time that the coredump occurred into filename 添加core文件生成时的unix时间
    %h - insert hostname where the coredump happened into filename 添加主机名
    %e - insert coredumping executable name into filename 添加命令名
```
## 使用core文件
在core文件所在目录下键入:
```
gdb -c core
```
它会启动GNU的调试器，来调试core文件，并且会显示生成此core文件的程序名，中止此程序的信号等等

如果你已经知道是由什么程序生成此core文件的，比如MyServer崩溃了生成core.12345，那么用此指令调试:
```
gdb -c core MyServer
```
以下怎么办就该去学习gdb的使用了

## 一个小方法来测试产生core文件
直接输入指令:
```
kill -s SIGSEGV $$
```
## 为何有时程序Down了，却没生成 Core文件。

Linux下，有一些设置，标明了resources available to the shell and to processes。 可以使用
```
#ulimit -a 来看这些设置。 (ulimit是bash built-in Command)

             -a     All current limits are reported
              -c     The maximum size of core files created
              -d     The maximum size of a process鈥檚 data segment
              -e     The maximum scheduling priority ("nice")
              -f     The maximum size of files written by the shell and its children
              -i     The maximum number of pending signals
              -l     The maximum size that may be locked into memory
              -m     The maximum resident set size (has no effect on Linux)
              -n     The maximum number of open file descriptors (most systems do not allow this value to be set)
              -p     The pipe size in 512-byte blocks (this may not be set)
              -q     The maximum number of bytes in POSIX message queues
              -r     The maximum real-time scheduling priority
              -s     The maximum stack size
              -t     The maximum amount of cpu time in seconds
              -u     The maximum number of processes available to a single user
              -v     The maximum amount of virtual memory available to the shell
              -x     The maximum number of file locks
```
从这里可以看出，如果 -c是显示：core file size          (blocks, -c)

如果这个值为0，则无法生成core文件。所以可以使用：
```
#ulimit -c 1024 或者 #ulimit -c unlimited 来使能 core文件。
```
如果程序出错时生成Core 文件，则会显示Segmentation fault (core dumped)。

## Core Dump的核心转储文件目录和命名规则:
/proc/sys/kernel/core_uses_pid可以控制产生的core文件的文件名中是否添加pid作为扩展，如果添加则文件内容为1，否则为0