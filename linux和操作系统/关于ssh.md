---
title: 关于ssh的知识
categories: [ssh]
tags: [ssh]
---
# 关于ssh的知识

## 配置ssh免秘钥登录
- ssh -vvv ip-address  
-vvv的意思是给出debug信息，信息会比较全。如果配置过程中出错了，可以看一下debug信息，看下具体哪里有问题。
- ssh7之后默认不支持dsa加密  
最好使用rsa加密。但是同样可以手动支持dsa，参见[How to Re-enable DSA keys when using OpenSSH 7.0 and above](https://centrify.force.com/support/Article/KB-7050-How-to-Re-enable-DSA-keys-when-using-OpenSSH-7-0-and-above)，在/etc/ssh/sshd_config和/etc/ssh/ssh_config文件中添加`PubkeyAcceptedKeyTypes=+ssh-dss`。实际测试发现:使用ssh7的服务端可以通过设置以上内容使得客户端可以免密码登录，但是服务端无法免密码登录客户端（即便客户端有服务端的dsa公钥）