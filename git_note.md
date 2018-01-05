# Git使用笔记

## git查看远程版本库和本地库的差异

- **`git status`**
    ```
    On branch master
    Your branch is ahead of ‘origin/master’ by 2 commits.
    ```
- **`git cherry -v`**: 查看到未传送到远程代码库的提交描述/说明
    ```
    + b6568326134dc7d55073b289b07c4b3d64eff2e7 add default charset for table items_has_images
    + 4cba858e87752363bd1ee8309c0048beef076c60 move Savant3 class into www/includes/class/
    ```
- **`git log master ^origin/master`**: 查看到未传送到远程代码库的提交详情  
这是一个git log命令的过滤，^origin/master可改成其它分支。（注：master是当前本地库的分支，origin/master指origin指定的远程库的master分支。当然，master可以改为任意其他分支。）  
显示结果类似于这样：
    ````
    commit 4cba858e87752363bd1ee8309c0048beef076c60
    Author: Zam <zam@iaixue.com>
    Date: Fri Aug 9 16:14:30 2013 +0800

    move Savant3 class into www/includes/class/

    commit b6568326134dc7d55073b289b07c4b3d64eff2e7
    Author: Zam <zam@iaixue.com>
    Date: Fri Aug 9 16:02:09 2013 +0800
    add default charset for table items_has_images
    ```
- **总结**
    - `git status` 只能查看未传送提交的次数
    - `git cherry -v` 只能查看未传送提交的描述/说明
    - `git log master ^origin/master` 则可以查看未传送提交的详细信息  

**[注]**：以上内容转载互联网上的。http://bbs.iaixue.com/forum.php?mod=viewthread&tid=1577

由第3点，可以想到，将远程和本地分支位置调换一下，即变成 `git log origin/master ^master`，就可以查看远程库比本地库多的内容了。不过得先执行`git fetch origin master`命令，将远程库的commit内容同步到本地库。

**fetch和pull的区别**是：fetch只同步远程库的commit信息（log信息），但不会将文件同步到本地，pull则会将文件也同步到本地库。

使用`git log`的时候，也可以使用 -p 参数查看提交中的更详细信息