# Git使用笔记

<!-- TOC -->

- [git查看远程版本库和本地库的差异](#git查看远程版本库和本地库的差异)
- [文件在工作目录、缓存区、本地仓库、远程仓库之间的差别](#文件在工作目录缓存区本地仓库远程仓库之间的差别)
    - [工作目录 vs 暂存区](#工作目录-vs-暂存区)
    - [暂存区 vs Git仓库](#暂存区-vs-git仓库)
    - [工作目录 vs Git仓库](#工作目录-vs-git仓库)
    - [Git仓库 vs Git仓库](#git仓库-vs-git仓库)
    - [本地文件 vs 远程Git仓库](#本地文件-vs-远程git仓库)

<!-- /TOC -->

## git查看远程版本库和本地库的差异
- **`git status`**
    ```
    On branch master
    Your branch is ahead of ‘origin/master’ by 2 commits.
    ```
- **`git fetch`加`git status`**
    
    `git fetch`可以取回远程分支的commit信息，但是不会进行本地文件的内容修改。之后`git status`同前面一样，显示本地仓库与本地远程仓库的区别。前面是ahead，如果本地落后就会显示behind。
    
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
    - 使用`git log`的时候，也可以使用 -p 参数查看提交中的更详细信息

**[注]**：以上内容转载互联网上的。http://bbs.iaixue.com/forum.php?mod=viewthread&tid=1577

由第3点，可以想到，将远程和本地分支位置调换一下，即变成 `git log origin/master ^master`，就可以查看远程库比本地库多的内容了。不过得先执行`git fetch origin master`命令，将远程库的commit内容同步到本地库。

## 文件在工作目录、缓存区、本地仓库、远程仓库之间的差别
**关键命令：`git diff`**（参考：[Git: git diff 命令详解]  
**说明**：
- 以下命令可以不指定 <filename>，则对全部文件操作。
- 以下命令涉及和 Git仓库 对比的，均可指定 commit 的版本。
- HEAD 最近一次 commit
- HEAD^ 上次提交
- HEAD~100 上100次提交
- 每次提交产生的哈希值

### 工作目录 vs 暂存区
查看文件在工作目录与暂存区的差别。如果还没 add 进暂存区，则查看文件自身修改前后的差别。`<branch>`指定分支，默认当前分支。
```git
git diff <branch> <filename>
```
### 暂存区 vs Git仓库
添加参数：`--cached`。commit默认为最新一次提交。
```
git diff --cached <commit> <filename>
```
### 工作目录 vs Git仓库
查看工作目录同Git仓库指定 commit 的内容的差异。
`<commit>=HEAD`时：查看工作目录同最近一次 commit 的内容的差异。
```
git diff <commit> <filename>
```
### Git仓库 vs Git仓库
Git仓库任意两次 commit 之间的差别。
```
git diff <commit> <commit>
```

### 本地文件 vs 远程Git仓库
在pull之前，可以先比较本地仓库和远程仓库之间的差异，步骤为：
1. 添加需要比较的远程仓库：`git remote add foobar git://github.com/user/foobar.git`
2.  取回foobar的内容，fetch不会修改本地的内容: `git fetch foobar`
3. 比较本地分支和远程分支之间的差异: `git diff master foobar/master`
4. 远程分支已经修改，本地未同步的变更: `git diff HEAD...origin/master`
5. 本地分支已经修改，远程未同步的变更: `git diff origin/master...HEAD`

最后两步通用格式`git diff <local branch> <remote>/<remote branch>`或者更通用的`git diff <branch1> <branch2>`，即显示`branch1`相对于`branch2`的变动，所以`branch1 branch2`的前后位置变化，输出结果也会变化。
