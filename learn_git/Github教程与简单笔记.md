---
title: Github教程与简单笔记
categories: Github
tags: Github
---
# Github教程与简单笔记
<!-- TOC -->

- [1. Github简介](#1-github简介)
- [2. Github功能标签介绍](#2-github功能标签介绍)
    - [2.1. 关于watch](#21-关于watch)
    - [2.2. 关于star](#22-关于star)
    - [2.3. 关于Fork](#23-关于fork)
        - [2.3.1. Fork并且更新GitHub仓库的图表演示](#231-fork并且更新github仓库的图表演示)
        - [2.3.2. 同步一个fork](#232-同步一个fork)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->
## 1. Github简介

github是一个基于git的代码托管平台，付费用户可以建私人仓库，我们一般的免费用户只能使用公共仓库，也就是代码要公开。
Github 由Chris Wanstrath, PJ Hyett 与Tom Preston-Werner三位开发者在2008年4月创办。迄今拥有59名全职员工，主要提供基于git的版本托管服务。
目前看来，GitHub这场冒险已经胜出。根据来自维基百科关于GitHub的描述，我们可以形象地看出GitHub的增长速度：

![github库的数量](https://camo.githubusercontent.com/9df81964b288254547c6607fe29e55b0e7dcef6a/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f343438332f313830333636372f62306564363634652d366332342d313165332d393535392d6535373032323135633437612e706e67)

今天，GitHub已是：
- 一个拥有143万开发者的社区。其中不乏Linux发明者Torvalds这样的顶级黑客，以及Rails创始人DHH这样的年轻极客。
- 这个星球上最流行的开源托管服务。目前已托管431万git项目，不仅越来越多知名开源项目迁入GitHub，比如Ruby on Rails、jQuery、Ruby、Erlang/OTP；近三年流行的开源库往往在GitHub首发，例如：BootStrap、Node.js、CoffeScript等。
- alexa全球排名414的网站。
## 2. Github功能标签介绍
### 2.1. 关于watch
![watch示意图](https://upload-images.jianshu.io/upload_images/588640-7aaa5676402d4ece.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)

对于别人的项目，默认自己都处于 Not watching 的状态，当你选择 Watching，表示你以后会关注这个项目的所有动态，这个项目以后只要发生变动，如被别人提交了 pull request、被别人发起了issue等等情况，你都会在自己的个人通知中心，收到一条通知消息，如果你设置了个人邮箱，那么你的邮箱也可能收到相应的邮件。

如下，我 watching 了开源项目android-cn/android-discuss，那么以后任何人只要在这个项目下提交了 issue 或者在 issue 下面有任何留言，我的通知中心就会通知我。如果你配置了邮箱，你还可能会因此不断的收到通知邮件。

![消息列表](https://upload-images.jianshu.io/upload_images/588640-f9145de159c4c6be.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700)
### 2.2. 关于star
star 翻译过来是星，但这个翻译没任何具体意义，这里解释为`关注`或者`点赞`更合适，当你点击 star，表示你喜欢这个项目或者通俗点，可以把他理解成朋友圈的点赞吧，表示对这个项目的支持。

不过相比朋友圈的点赞，github 里面会有一个列表，专门收集了你所有 star 过的项目，点击 github 个人头像，可以看到 your stars 的条目，点击就可以查看你 star 过的所有项目了

### 2.3. 关于Fork
Fork 的本义是 ***叉子***（名词）    
![叉子](https://pic3.zhimg.com/50/37c8a551c139e20502088d978d4529cd_hd.jpg)

Git/GitHub 用户下面的图 来表达 Fork：分叉、克隆 出一个（仓库的）新拷贝。  
![github分支](https://pic4.zhimg.com/50/3c13b2d3ddbf178b4debfea57644e520_hd.jpg)

现在有这样一种情形：有一个叫做Joe的程序猿写了一个游戏程序，而你可能要去改进它。并且Joe将他的代码放在了GitHub仓库上。下面是你要做的事情：  
![图片](https://pic2.zhimg.com/50/dadbcef0bca3d2eb68ef6009f45361e2_hd.jpg)
#### 2.3.1. Fork并且更新GitHub仓库的图表演示

**Fork他的仓库**：这是GitHub操作，这个操作会复制Joe的仓库（包括文件，提交历史，issues，和其余一些东西）。复制后的仓库在你自己的GitHub帐号下。目前，你本地计算机对这个仓库没有任何操作。

**Clone你的仓库**：这是Git操作。使用该操作让你发送"请给我发一份我仓库的复制文件"的命令给GitHub。现在这个仓库就会存储在你本地计算机上。

**更新某些文件**：现在，你可以在任何程序或者环境下更新仓库里的文件。

**提交你的更改**：这是Git操作。使用该操作让你发送"记录我的更改"的命令至GitHub。此操作只在你的本地计算机上完成。

将你的更改push到你的GitHub仓库：这是Git操作。使用该操作让你发送"这是我的修改"的信息给GitHub。Push操作不会自动完成，所以直到你做了push操作，GitHub才知道你的提交。

**给Joe发送一个pull request**：如果你认为Joe会接受你的修改，你就可以给他发送一个pull request。这是GitHub操作，使用此操作可以帮助你和Joe交流你的修改，并且询问Joe是否愿意接受你的"pull request"，当然，接不接受完全取决于他自己。

如果Joe接受了你的pull request，他将把那些修改拉到自己的仓库。胜利！

#### 2.3.2. 同步一个fork
Joe和其余贡献者已经对这个项目做了一些修改，而你将在他们的修改的基础上，还要再做一些修改。在你开始之前，你最好"同步你的fork"，以确保在最新的复制版本里工作。下面是你要做的：  
![图片2](https://dn-linuxcn.qbox.me/data/attachment/album/201411/24/162416icr0h6wzr6ec2jze.png)
1. 从Joe的仓库中取出那些变化的文件：这是Git操作，使用该命令让你可以从Joe的仓库获取最新的文件。

2. 将这些修改合并到你自己的仓库：这是Git操作，使用该命令使得那些修改更新到你的本地计算机（那些修改暂时存放在一个"分支"中）。记住：步骤1和2经常结合为一个命令使用，合并后的Git命令叫做"pull"。

3. 将那些修改更新推送到你的GitHub仓库（可选）：记住，你本地计算机不会自动更新你的GitHub仓库。所以，唯一更新GitHub仓库的办法就是将那些修改推送上去。你可以在步骤2完成后立即执行push，也可以等到你做了自己的一些修改，并已经本地提交后再执行推送操作。

比较一下fork和同步工作流程的区别：当你最初fork一个仓库的时候，信息的流向是从Joe的仓库到你的仓库，然后再到你本地计算机。但是最初的过程之后，信息的流向是从Joe的仓库到你的本地计算机，之后再到你的仓库。
## 3. 参考资料
[1] [Github简明教程](http://www.runoob.com/w3cnote/git-guide.html)  
[2] [在Github和Git上fork之简单指南](https://linux.cn/article-4292-1-rss.html)  
[3] [如何用好 github 中的 watch、star、fork](https://www.jianshu.com/p/6c366b53ea41)