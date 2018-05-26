---
title: 计算机网络中的面试问题随笔
categories: [计算机网络]
tags: [计算机网络, 面试随笔]
---
# 计算机网络中的面试问题随笔
### 网络中TCP/IP和http的关系
参考资料：
- [TCP/IP、Http、Socket的关系理解](https://blog.csdn.net/qq_35181209/article/details/75212533)
- [懵逼的HTTP、Socket与TCP](https://www.jianshu.com/p/a5410f895d6b)

TPC/IP协议是传输层协议，主要解决数据如何在网络中传输，而HTTP是应用层协议，主要解决如何包装数据。

![TCP/IP协议栈](https://raw.githubusercontent.com/zqjflash/tcp-ip-protocal/master/tcp-ip-protocal.png)

![TCP/IP协议族中的位置关系](https://upload-images.jianshu.io/upload_images/735757-e38faee729cc7dfc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/540)
### socket与session的区别
参考资料：
- [Cookie 与 Session 的区别](https://juejin.im/entry/5766c29d6be3ff006a31b84e)

总结来看：
- Session是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；
- Cookie是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现Session的一种方式。
