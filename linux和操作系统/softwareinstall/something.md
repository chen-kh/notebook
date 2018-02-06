# ubuntu14.04 中安装一些常用软件

## 安装vscode
参考：[在Ubuntu中安装Visual Studio Code](https://linux.cn/article-5423-1.html)

主要命令：
```bash
# 安装ubuntu-make
# 更新源
sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt-get update
sudo apt-get install ubuntu-make
# 安装vscode
umake web visual-studio-code
# 卸载vscode
umake web visual-studio-code --remove
```

## 安装git
使用`sudo apt-get install git`安装的是系统的默认版本，我自己安装的时候默认是1.9.1，有点老。网上有个更新的方法：
```bash
git --version
# git version 1.9.1
# 可以使用下面命令升级git（如果不是root用户，需在命令前加sudo）：
sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sduo apt-get install git
# 安装完成后，再查看git版本：
git --version
# git version 2.10.1
```