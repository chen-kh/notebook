# markdown语法笔记  
**注**：Markdown 并没有一个整体规范的写法，markdown只是提供了一些基本的规则，复杂的功能需要开发者自己实现。markdown有很多种，比如github使用github favorable markdown，基本语法大致相同，但是有些差别存在。需要用户自己发现。
## 1. 标题
- # 一级标题
- ## 二级标题
- ### 三级标题


## 2. 粗体和斜体
- 斜体效果：*VSCODE*  
- 加粗效果：**VSCODE**  
- 斜体加粗效果：***VSCODE***  
- ~~删除线~~：删除线  
- 居中：<p align="center">我是居中</p>
- 左对齐：<p align="left">我是左对齐</p>
- 右对齐：<p align="right">我是右对齐</p>
- Markdown没有下划线原生语法，因为会和链接的默认样式产生混淆。解决方法是使用行内 HTML. 比如：<u>Underlined Text</u>和<span style="border-bottom:2px dashed yellow;">所添加的需要加下划线的行内文字</span>，其中后者三个参数分别为[border-bottom-width](http://www.w3school.com.cn/cssref/pr_border-bottom_width.asp), [border-bottom-style](http://www.w3school.com.cn/cssref/pr_border-bottom_style.asp), [border-bottom-color](http://www.w3school.com.cn/cssref/pr_border-bottom_color.asp)
- 首行缩进：可以在段首加入\&ensp;来输入一个空格。加入\&emsp;来输入两个空格。  
&emsp;&emsp;一语未了，只听后院中有人笑声，说：“我来迟了，不曾迎接远客！"  


## 3. 引用
### 3.1 文本引用
> 我是引用  
>> 我是嵌套引用  
我是引用  

> 我是引用


### 3.2 代码引用
#### 单行代码引用  
Java中使用 `System.out.println("Hello World!")` 作为输出
#### 多行代码引用
```python 
# 代码高亮，在引用前写上语言就行了
a = 10
b = 20
c = a +b
print('The result of a + b = ' + str(c))
```

## 4. 列表
- VSCODE  
Hello world
- VSCODE
* RED
* RED
+ BAD
+ BAD

1. 文本  
我是谁
2. 文本  
需要换行在换行前多写两个空格
10. 注意这里是10，所以并没有考虑序号的正确性  
1968\. 如果遇到开头是数字的话，可以用 \ 处理

## 5. 表格
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
## 6. 分割线
***
这是分割线
***
这是分割线
* * *
这是分割线
**********
这是分割线
- - - - - 
这是分割线
----------------- - -
## 7. 区段元素
- 行内链接This is [an example](http://example.com/ "Title") inline link.  
- See my [About](/about/) page for details. // 这里是相对路径  
- This is [Google][link] reference-style link.  
- 连接到本地的文件，例如[分类图](E:\\毕业设计\\微信图片_20171214203534.png)  
- [Google][link]  
- 自动链接<http://www.google.com/>

## 8. 插入图片
- 行内式：![GitHub](https://avatars2.githubusercontent.com/u/3265208?v=3&s=100 "GitHub,Social Coding")就是这样
- 参考式：![GitHub][github]就是这样
## 9. 链接标题与生成目录
### 9.1 链接到标题
可以直接使用 <u>\[内容](#标题地址)</u> 的形式, 例如链接到[3. 引用](#3-引用)， 注意括号里面\(#链接到的地方)不能有英文句号。因此无法链接到带有“.”的次级标题，如“3.1 文本应用”是无法链接到的。
### 9.1 生成目录
示例如下：  
> * [1. 生成目录](#1)
>     * [1.1 第二级1](#1.1)
>     * [1.2 第二级2](#1.2)
> * [2.结语](#2)
> <h2 id="1">1. 生成目录</h2>
> 这是一个自动生成目录的语法。下面是下一级目录：
> <h3 id="1.1">1.1 第二级说明1</h3>
> 这是二级目录的一个测试文本。
> <h3 id="1.2">1.2 第二级说明2</h3>
> 这是二级目录的第二个测试文本。
> <h2 id="2">2. 结语</h2>

## 参考链接

[1] [Markdown 语法说明 (简体中文版)](http://wowubuntu.com/markdown/)  
[2] [Learning-Markdown (Markdown 入门参考)](http://xianbai.me/learn-md/article/about/readme.html)  


[github]: https://avatars2.githubusercontent.com/u/3265208?v=3&s=100 "GitHub,Social Coding"
[link]: https://avatars2.githubusercontent.com/u/3265208?v=3&s=100 "GitHub,Social Coding"