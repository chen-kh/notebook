---
title: Python 虚拟环境学习与使用
categories: [Python]
tags: [Python, 虚拟环境]
---
# Python 虚拟环境学习与使用

<!-- TOC -->

- [什么是python的虚拟环境](#什么是python的虚拟环境)
- [如何搭建python虚拟环境](#如何搭建python虚拟环境)
    - [virtualenv的安装](#virtualenv的安装)
    - [虚拟环境生命周期](#虚拟环境生命周期)
    - [Virtaulenvwrapper](#virtaulenvwrapper)
- [注意点](#注意点)
- [参考资料](#参考资料)

<!-- /TOC -->
## 什么是python的虚拟环境
&emsp;&emsp;Python虚拟环境指虚拟的独立运行环境。Python虚拟环境指独立的python运行环境，一般用于解决不同项目依赖不同，而又不希望互相干扰的问题。Python最长用的虚拟工具是virtualenv，它是一个第三方包。  
> 在一个 Python 环境下开发时间越久、安装依赖越多，就越容易出现依赖包冲突的问题。为了解决这个问题，开发者们开发出了 virtualenv，可以搭建虚拟且独立的 Python 环境。这样就可以使每个项目环境与其他项目独立开来，保持环境的干净，解决包冲突问题。

> 动态语言中Ruby、Python都有自己的虚拟环境，通过创建虚拟环境能够使不同的项目之间的运行环境保持独立性而相互不受影响。例如项目A依赖Django1.4，而项目B依赖Django1.5，这时它就能解决此类问题。Ruby有Vagrant，Python有virtualenv，本文讨论Python虚拟环境。virtualenv可用于创建独立的Python环境，它会创建一个包含项目所必须要的执行文件。
## 如何搭建python虚拟环境
### virtualenv的安装
&emsp;&emsp;virtualenv实际上是一个第三方包，是管理虚拟环境的常用方法之一。Python3 中还自带了虚拟环境管理包。virtualenv的安装可以用easy_install或者pip安装。推荐使用pip安装。
```sh
pip install virtualenv
```
### 虚拟环境生命周期
**创建：**  
```sh
virtualenv testvirdir  #创建名称为testvirdir的虚拟目录
cd testvirdir
source bin/activate #激活虚拟环境
python -V #测试python
which python #查看python位置（应该为testvirdir下面的python）此时命令行前面会多出一个括号，括号里为虚拟环境的名称。以后easy_install或者pip安装的所有模块都会安装到该虚拟环境目录里。
```
**使用：**  
- 只要在虚拟环境中执行命令就行，跟正常python一样。  
- 在虚拟环境安装Python packages时，Virtualenv 附带有pip安装工具，因此需要安装的packages可以直接运行pip命令  

**退出：**  
```
deactivate
```
**删除：**  
直接删除虚拟环境目录
```sh
rm -rf [virtual dir]
```
**补充：**  
- virtualenv 后加入 *--no-site-packages* 使得已经安装到系统Python环境中的所有第三方包都不会复制过来，这样就得到了一个不带任何第三方包的“干净”的Python运行环境。如果想依赖系统环境的第三方软件包，可以使用参数 *--system-site-packages*。  
### Virtaulenvwrapper
&emsp;&emsp;Virtaulenvwrapper是virtualenv的扩展包，提供了一系列命令，可以方便地<u>创建、删除、复制、切换</u>不同的虚拟环境。同时，使用该扩展后，所有虚拟环境都会被放置在同一个目录下。  
**安装：**
```sh
pip install virtualenvwrapper
```
&emsp;&emsp;此时还不能使用virtualenvwrapper，默认virtualenvwrapper安装在/usr/local/bin下面，实际上需要运行virtualenvwrapper.sh文件才行。  
**设置环境变量：**  
&emsp;&emsp;把下面两行添加到~/.bashrc（或者~/.zshrc）里。  
```sh
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
   export WORKON_HOME=$HOME/.virtualenvs 
   source /usr/local/bin/virtualenvwrapper.sh
fi
```
&emsp;&emsp;其中，.virtualenvs 是可以自定义的虚拟环境管理目录。可以事先 `mkdir` 。然后执行：`source ~/.bashrc`，就可以使用 virtualenvwrapper 了。Windows 平台的安装过程，请参考[官方文档](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)。  
**使用:** 
``` sh
lsvirtualenv -b # 列出虚拟环境
workon [虚拟环境名称] # 切换虚拟环境
lssitepackages # 查看环境里安装了哪些包
cdvirtualenv [子目录名] # 进入当前环境的目录
cpvirtualenv [source] [dest] # 复制虚拟环境
rmvirtualenv [虚拟环境名称] # 删除虚拟环境
deactivate # 退出虚拟环境
```
## 注意点
待补充

## 参考资料
[1] [Python虚拟环境](https://github.com/lzjun567/note/blob/master/note/python/virtualenv.md)  
[2] [Python开发必备神器之一：virtualenv](http://codingpy.com/article/virtualenv-must-have-tool-for-python-development/)
