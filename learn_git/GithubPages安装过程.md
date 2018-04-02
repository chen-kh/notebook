---
title: Gihub Pages安装过程
date: 2018-03-30 00:08:04
tags: [Github, hexo]
---
# GihubPages安装过程
记录下github pages的安装过程。安装环境为win7。
参考资料：
- [使用GitHub/GitLab/码云搭建个人博客](http://www.sunhome.org.cn/2017/11/15/hexonext/)

## 什么是github pages？
待补充

## 安装步骤

### 准备工作
- 安装git：不再多述
- 使用github并创建仓库
- 安装node.js：  
最新版的nodejs可以在[这里获取](https://nodejs.org/en/)，下载后直接安装即可，安装完后打开`cmd`，输入`npm -v`，如果能输出版本号则说明安装成功。

### 安装hexo
```cmd
npm install hexo-cli -g
hexo init blog
cd blog
npm install
hexo server -p 5000 [--debug]
```

## hexo使用命令
主要是以下几个，更多详细请参见博客：
```
hexo g[enerate]
hexo d[eploy]
```

## hexo效果配置
参考：
- [Hexo-NexT配置超炫网页效果](https://www.jianshu.com/p/9f0e90cc32c2)
- [hexo的next主题个性化教程:打造炫酷网站](http://shenzekun.cn/hexo%E7%9A%84next%E4%B8%BB%E9%A2%98%E4%B8%AA%E6%80%A7%E5%8C%96%E9%85%8D%E7%BD%AE%E6%95%99%E7%A8%8B.html)