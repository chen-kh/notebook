---
title: java根类Object的说明
categories: [Java知识]
tags: [Java知识]
---
# Java根类Object的说明
<!-- TOC -->

- [1. 初识Object](#1-初识object)
- [2. 方法分析](#2-方法分析)
    - [2.1. registerNatives()](#21-registernatives)
    - [2.2. getClass()](#22-getclass)
    - [2.3. hashCode()](#23-hashcode)
    - [2.4. equals()](#24-equals)
    - [2.5. clone()](#25-clone)
    - [2.6. toString()](#26-tostring)
    - [2.7. notify()](#27-notify)
    - [2.8. notifyAll()](#28-notifyall)
    - [2.9. wait(long timeout) throws ...](#29-waitlong-timeout-throws-)
    - [2.10. finalize()](#210-finalize)

<!-- /TOC -->

参考资料：
- [Java根类Object的方法说明](https://fangjian0423.github.io/2016/03/12/java-Object-method/)
- [java object类详解](https://zhuanlan.zhihu.com/p/29511703)
## 1. 初识Object
- Object类是Java中其他所有类的父类。
- Object类位于java.lang包中，java.lang包包含着Java最基础和核心的类，在编译时会自动导入
- 可以使用类型为Object的变量指向任意类型的对象。
- Object类有一个默认构造方法pubilc Object()，在构造子类实例时，都会先调用这个默认构造方法。
- Object类的变量只能用作各种值的通用持有者。要对他们进行任何专门的操作，都需要知道它们的原始类型并进行类型转换。例如：
```java
Object obj = new MyObject();
MyObject x = (MyObject)obj;
```
- Object类没有定义属性，一共有13个方法，具体的类定义结构如下：
```java
// java.lang.Object

public class Object {

    private static native void registerNatives();
    static {
        registerNatives();
    }
    public final native Class<?> getClass();
    public native int hashCode();
    public boolean equals(Object obj) {
        return (this == obj);
    }
    protected native Object clone() throws CloneNotSupportedException;

    public String toString() {
        return getClass().getName() + "@" + Integer.toHexString(hashCode());
    }
    public final native void notify();
    public final native void notifyAll();
    public final native void wait(long timeout) throws InterruptedException;
    public final void wait(long timeout, int nanos) throws InterruptedException {
        if (timeout < 0) {
            throw new IllegalArgumentException("timeout value is negative");
        }

        if (nanos < 0 || nanos > 999999) {
            throw new IllegalArgumentException(
                                "nanosecond timeout value out of range");
        }

        if (nanos > 0) {
            timeout++;
        }

        wait(timeout);
    }
    protected void finalize() throws Throwable { }
}

```

## 2. 方法分析
分析Object最基本的方法是本文的主要内容。
### 2.1. registerNatives()
native方法。

native关键字修饰的函数表明该方法的实现并不是在Java中去完成，而是由C/C++去完成，并被编译成了.dll，由Java去调用

其主要作用是将C/C++中的方法映射到Java中的native方法，实现方法命名的解耦。所以类加载时首先执行的就是这个函数。

### 2.2. getClass()
native方法：返回此对象的类对象。

**类对象解释**
> 在Java中，类是是对具有一组相同特征或行为的实例的抽象并进行描述，对象则是此类所描述的特征或行为的具体实例。作为概念层次的类，其本身也具有某些共同的特性，如都具有类名称、由类加载器去加载，都具有包，具有父类，属性和方法等。于是，Java中有专门定义了一个类，Class，去描述其他类所具有的这些特性，因此，从此角度去看，类本身也都是属于Class类的对象。为与经常意义上的对象相区分，在此称之为"类对象"。

### 2.3. hashCode()
hashCode()具有如下约定：

1. 在Java应用程序执行期间，对于同一对象多次调用hashCode()方法时，其返回的哈希码是相同的，前提是将对象进行equals比较时所用的标尺信息未做修改。在Java应用程序的一次执行到另外一次执行，同一对象的hashCode()返回的哈希码无须保持一致；

2. 如果两个对象相等（依据：调用equals()方法），那么这两个对象调用hashCode()返回的哈希码也必须相等；

3. 反之，两个对象调用hasCode()返回的哈希码相等，这两个对象不一定相等。

### 2.4. equals()
默认是同一个对象才能相等，但是可以进行覆盖啊。覆盖equals需要遵守一些规定：

- 自反性 (reflexive)：对于任何一个非null的引用值x，x.equals(x)为true。
- 对称性 (symmetric)：对于任何一个非null的引用值x和y，x.equals(y)为true时y.equals(x)为true。
- 传递性 (transitive)：对于任何一个非null的引用值x、y和z，当x.equals(y)为true 且 y.equals(z)为true 则 x.equals(z)为true。
- 一致性 (consistent)：对于任何一个非null的引用值x和y，只要equals的比较操作在对象中所用的信息没有被修改，多次调用x.equals(y)的结果依然一致。
(PS：对于任何非null的引用值x，x.equals(null)必须返回false。)

**Java中的约定：重写equals()方法必须重写hasCode()方法**。其关键问题在于，`public V get(Object key)`使用get等方法的时候，这里的key是Object类型，而不是泛型K。至于原因，参见[StackOverFlow: What are the reasons why Map.get(Object key) is not (fully) generic
](https://stackoverflow.com/questions/857420/what-are-the-reasons-why-map-getobject-key-is-not-fully-generic)。因此，如果equals重写了，但是hashCode没有重写的话，很有可能造成equals相等，但是hashcode不相同。

参考：
- [Java - 谨慎覆盖equals](http://www.cnblogs.com/kavlez/p/4185547.html)：提到了很多注意点，以及建议覆盖equals和hashCode的技巧。
- [重写equal()时为什么也得重写hashCode()之深度解读equal方法与hashCode方法渊源](https://blog.csdn.net/javazejian/article/details/51348320)
### 2.5. clone()
native方法。

protected修饰：在同一个包内或者不同包的子类可以访问。（不同包的情况下，必须是子类的引用主动调用方法，原父类调用是不行的）

java语法规定：clone()的正确调用是需要实现Cloneable接口，如果没有实现Cloneable接口，并且子类直接调用Object类的clone()方法，则会抛出CloneNotSupportedException异常。

### 2.6. toString()
### 2.7. notify()
### 2.8. notifyAll()
### 2.9. wait(long timeout) throws ...
### 2.10. finalize()
finalize方法主要与Java垃圾回收机制有关。