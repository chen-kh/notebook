# Python面试整理
[Python程序员面试，这些问题你必须提前准备！](https://mp.weixin.qq.com/s?__biz=MjM5MDAxNjkyMA==&mid=2650731809&idx=1&sn=48a7b8464ee7a18688bc6a87a75ce3b2&chksm=be4161d68936e8c0fb741603401d4951749b6faeed008dc7e26d4665b7515736bfe2a9aed481&scene=0#rd)

# what-how-difference-practice篇
## What？
1. 什么是Python？
一种面向对象的解释型计算机程序设计语言，是一种广泛使用的高级编程语言
2. 什么是Python自省？
> 这个机制被称为反射（反过来让对象告诉我们他是什么），或是自省（让对象自己告诉我们他是什么，好吧我承认括号里是我瞎掰的- -#），用于实现在运行时获取未知对象的信息。反射是个很吓唬人的名词，听起来高深莫测，在一般的编程语言里反射相对其他概念来说稍显复杂，一般来说都是作为高级主题来讲；但在Python中反射非常简单，用起来几乎感觉不到与其他的代码有区别，使用反射获取到的函数和方法可以像平常一样加上括号直接调用，获取到类后可以直接构造实例；不过获取到的字段不能直接赋值，因为拿到的其实是另一个指向同一个地方的引用，赋值只能改变当前的这个引用而已。

其实就是python提供的一些查看对象的内容的工具。如下示例：
```python
dir([obj]): 
hasattr(obj, attr): 
getattr(obj, attr): 
setattr(obj, attr, val): 

print Cat.__doc__           # None
print Cat.__name__          # Cat
print Cat.__module__        # __main__
print Cat.__bases__         # (<type>,)
print Cat.__dict__          # {'__module__': '__main__', ...}</type>


```
3. 什么是PEP？
[百度百科]：PEP是Python Enhancement Proposals的缩写。一个PEP是一份为Python社区提供各种增强功能的技术规格，也是提交新特性，以便让社区指出问题，精确化技术文档的提案。
4. 什么是pickling和unpick？
Python中可以使用pickle 模块将对象转化为文件保存在磁盘上，在需要的时候再读取并还原
5. 什么是Python装饰器？

6. 什么是Python的命名空间？

7. 什么是字典推导式和列表推导式？

8. Lambda函数是什么？

9. *Argos，**warthogs参数是什么？

10. 什么是Pass语句？

11. unittest是什么？

11. 构造器是什么？

12. doc string是什么？

13. 负索引是什么？

14. 模块和包是什么？

15. 垃圾回收是什么？

16. CSRF是什么？



How？


1. 如何让你的程序更具可读性？

2. Python是如何被解释的？

3. 如何在Python中拷贝一个对象？

4. 如何用Python删除一个文件？

5. 如何将一个数字转换成一个字符串？

6. Python是如何进行内存管理的？

7. 如何实现duple和list的转换？

8. Python里面如何生成随机数？

9. 如何在一个function里面设置一个全局的变量

10. Python如何实现单例模式？其他23种设计模式python如何实现？

11. Deepcopy如何实现？

12. 算法排序在最坏情况下如何优化？

13. 如何判断单向链表中是否有环？

14. 如何遍历一个内部未知的文件夹？

15. 数据库如何分区、分表？

16. 如何对查询命令进行优化？

17. 如何理解开源？

18. 如何用MVC/MTV的缓存？

19. Mys的死锁是如何产生的？

20. Sql注入是如何产生的，如何防止？

21. xxs如何预防？

22. 如何生成共享秘钥？ 如何防范中间人攻击？

23. 如何管理不同版本的代码？


Different


1. 数组和元组之间的区别？

2. _new_和_init_的区别？
- __init__为初始化方法，__new__方法是真正的构造函数。
- __new__是实例创建之前被调用，它的任务是创建并返回该实例，是静态方法
- __init__是实例创建之后被调用的，然后设置对象属性的一些初始值。 

总结：__new__方法在__init__方法之前被调用，并且__new__方法的返回值将传递给__init__方法作为第一个参数，最后__init__给这个实例设置一些参数。

3. Python中单下划线和双下划綫的区别？
- __name__是一种约定，Python内部的名字，用来与用户自定义的名字区分开，防止冲突
- _name：一种约定，用来指定变量私有
- __name：解释器用_classname__name来代替这个名字用以区别和其他类相同的命名
4. 浅拷贝与深拷贝的区别是？

5. 使用装饰器的单例和使用其他方法的单例，在后续使用中，有何区别？

6. 多进程与多线程的区别？

7. select和epoll的区别？

8. TCP和UDP的区别？边缘触发和水平触发的区别？

9. HTTP连接：get和post的区别？

10. varchar与char的区别？

11. BTree索引和hash索引的区别？

12. 在判断object是否是class的instances时，type和Constance函数的区别？

13. primary key和unique的区别？

14. ecb和cbc模式有什么区别？

15. 对称加密与非对称加密的区别？

16. staticmethod和装饰器的区别？

17. Xrange和range的区别？

18. deepcopy 和 copy的区别？

19. os.path和sys.path的区别？

20. 生成器(generator)与函数的区别？

21. os与sys模块的区别？

官方文档： 
- os模板提供了一种方便的使用操作系统函数的方法
- sys模板可供访问由解释器使用或维护的变量和与解释器交互的函数

另一种回答：

os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口。sys模块负责程序与Python解释器的交互，提供了一系列的函数和变量用户操作Python运行时的环境。

22. NoSQL和关系数据库的区别？

## 参考资料
1. [常见面试题整理--Python概念篇](https://zhuanlan.zhihu.com/p/23526961?refer=passer)
