<link rel="stylesheet" type="text/css" href="auto-number-title.css" />

---------------------------------------
    如何给Markdown文件自动加上标题编号
    @author chenkh
    @createtime 2018-01-02
---------------------------------------
# 如何给Markdown文件自动加上标题编号
**转自参考资料[1]**  
<!-- TOC -->

- [如何给Markdown文件自动加上标题编号](#如何给markdown文件自动加上标题编号)
    - [问题描述](#问题描述)
    - [解决方法](#解决方法)
    - [进一步优化](#进一步优化)
    - [补充说明](#补充说明)
    - [参考资料](#参考资料)

<!-- /TOC -->
## 问题描述

我们都知道，MarkDown可以通过######等标记添加不同层次的标题，非常方便。但是问题来了：如何给标题加上编号呢？

像这样：

\# Title  
\## 1. sub-title  
\### 1.1 sub-sub-title  
\### 1.2 sub-sub-title  
\## 2. sub-title  
\## 3. sub-title  

为了给标题加上编号，手动加上11.11.223，很麻烦有没有？如果插入或删除章节，后面的编号都要重新修改一遍。。。

## 解决方法

其实，MarkDown是可以直接支持CSS的。在md文件中加入CSS代码，即可给章节自动加上编号。
```css
<style type="text/css">
    h1 { counter-reset: h2counter; }
    h2 { counter-reset: h3counter; }
    h3 { counter-reset: h4counter; }
    h4 { counter-reset: h5counter; }
    h5 { counter-reset: h6counter; }
    h6 { }
    h2:before {
      counter-increment: h2counter;
      content: counter(h2counter) ".\0000a0\0000a0";
    }
    h3:before {
      counter-increment: h3counter;
      content: counter(h2counter) "."
                counter(h3counter) ".\0000a0\0000a0";
    }
    h4:before {
      counter-increment: h4counter;
      content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) ".\0000a0\0000a0";
    }
    h5:before {
      counter-increment: h5counter;
      content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) "."
                counter(h5counter) ".\0000a0\0000a0";
    }
    h6:before {
      counter-increment: h6counter;
      content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) "."
                counter(h5counter) "."
                counter(h6counter) ".\0000a0\0000a0";
    }
</style>
```
## 进一步优化

每个MarkDown文件中都要加上上面这段CSS，还是有点麻烦。幸好，MarkDown也支持外部样式表。把上面的代码保存到一个独立的CSS文件中（去掉头尾的style标签），文件命名为 auto-number-title.css
```css
h1 { counter-reset: h2counter; }
h2 { counter-reset: h3counter; }
h3 { counter-reset: h4counter; }
h4 { counter-reset: h5counter; }
h5 { counter-reset: h6counter; }
h6 { }
h2:before {
  counter-increment: h2counter;
  content: counter(h2counter) ".\0000a0\0000a0";
}
h3:before {
  counter-increment: h3counter;
  content: counter(h2counter) "."
            counter(h3counter) ".\0000a0\0000a0";
}
h4:before {
  counter-increment: h4counter;
  content: counter(h2counter) "."
            counter(h3counter) "."
            counter(h4counter) ".\0000a0\0000a0";
}
h5:before {
  counter-increment: h5counter;
  content: counter(h2counter) "."
            counter(h3counter) "."
            counter(h4counter) "."
            counter(h5counter) ".\0000a0\0000a0";
}
h6:before {
  counter-increment: h6counter;
  content: counter(h2counter) "."
            counter(h3counter) "."
            counter(h4counter) "."
            counter(h5counter) "."
            counter(h6counter) ".\0000a0\0000a0";
}
```
接下来只要在md文件中加上引用外部样式表的代码就可以啦：
```html
<link rel="stylesheet" type="text/css" href="auto-number-title.css" />
```
是不是很方便呢？

## 补充说明

为了能用本文的方法实现标题自动编号，文章必须有主标题，且必须是一级标题“#”，然后在正文中依次使用二级、三级标题等。自动编号是从二级标题开始的。一级标题是主标题，只应该有一个，也不应加上编号。

## 参考资料
[1] [MarkDown标题自动添加编号](https://yanwei.github.io/misc/markdown-auto-number-title.html)
