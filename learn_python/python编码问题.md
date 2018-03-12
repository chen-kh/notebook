# Python 编码问题
**Python encode and decode just like shit !!!!!!!!!!**

参考博文：[Python2.x 字符编码终极指南](http://selfboot.cn/2016/12/28/py_encode_decode/#str-%E7%B1%BB%E5%9E%8B)

总结起来就是：
## 1. Python中的两个类型：`<type 'str'>` 和 `<type 'unicode'>`
简单来说：

- str：是字节串（container for bytes），由 Unicode 经过编码(encode)后的字节组成的。
- unicode：真正意义上的字符串，其中的每个字符用 Unicode 中对应的 Code Point 表示。
![unicode<=>str](http://xuelangzf-github.qiniudn.com/20161228_encode_decode_3.png)


## 2. 总结
- str可以看作是unicode字符串经过某种编码后的字节组成的数组
- unicode是真正意义上的字符串
- 通过 encode 可以将unicode类型编码为str类型
- 通过 decode 可以将str类型解码为unicode类型
- python 会隐式地进行编码、解码，默认采用 ascii
- 所有的编码、解码错误都是由于所选的编码、解码方式无法表示某些字符造成的