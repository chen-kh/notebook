---------------------------------
    如何在github上添加数学公式
    @author chenkh
    @createtime 2018-01-02
---------------------------------
# 如何在github上添加数学公式
github上添加数学公式有很多种方法，总结起来两种形式：  
- 使用公式编辑器生成公式图片链接，直接放在markdown文件中作为公式的图片链接。
- 使用MathJax等高级公式编辑器进行数学公式直接书写和显示  

目前只会使用第一种方法，第二种方法不是github直接支持的，比较复杂。另外github基于简单，快速，安全的理念，推荐使用第一种方法。  
下面介绍第一种方法的使用。第二种方法待补充。
## 生成公式图片链接
CodeCogs 提供了一个[在线 LaTeX 编辑器](https://link.jianshu.com/?t=https://www.codecogs.com/latex/eqneditor.php)，可以将输入的数学公式转换为图片，并自动生成 HTML 代码（也支持其他格式）。
比如输入下面的代码：  
ax^{2} + by^{2} + c = 0
便可以得到：  
![](https://latex.codecogs.com/png.latex?ax^{2}&space;&plus;&space;by^{2}&space;&plus;&space;c&space;=&space;0)  
由于 Markdown 允许嵌入 HTML，所以直接把生成的代码粘贴过去就可以了。
另例如：  
质能方程：<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;E=mc^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\normal&space;E=mc^{2}" title="\huge E=mc^{2}" /></a>  
此在线编辑器功能欠打，可以选择文件输出格式，支持png,gif等多种；还支持多种表现写法，支持html, url等。

