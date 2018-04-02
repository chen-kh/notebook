---
title: Java 知识随笔
categories: [Java知识, 随笔]
tags: [Java, JVM, 随笔]
---
# Java 知识随笔
<!-- TOC -->

- [1. 等待线程结束的方法有哪些？](#1-等待线程结束的方法有哪些)
- [2. Java中对应数据结构中的队列、栈、双向队列等的内容](#2-java中对应数据结构中的队列栈双向队列等的内容)
    - [2.1. 队列与双向队列](#21-队列与双向队列)
    - [2.2. 链表与双向链表](#22-链表与双向链表)
    - [2.3. 栈](#23-栈)
    - [2.4. 树及红黑树实现的结构](#24-树及红黑树实现的结构)
- [3. Java 克隆](#3-java-克隆)
    - [3.1. 浅拷贝与深拷贝](#31-浅拷贝与深拷贝)
    - [3.2. `Cloneable`接口](#32-cloneable接口)
    - [3.3. `Serializable`接口](#33-serializable接口)
- [Java中的`final`关键字](#java中的final关键字)
    - [`final`关键字的含义](#final关键字的含义)
    - [`final`变量/引用](#final变量引用)
    - [`final`方法](#final方法)
    - [`final`类](#final类)
    - [`final`关键字的好处](#final关键字的好处)
- [Java中的`transient`关键字](#java中的transient关键字)
- [Java中的`ListIterator`](#java中的listiterator)
- [Java中的`HashMap`](#java中的hashmap)

<!-- /TOC -->
  
## 1. 等待线程结束的方法有哪些？
等待线程结束的方法，当然可以通过在`run()`函数里面更改标示位（或者变量），然后检测这个标示位（变量）来判断线程是否已经完成任务。但是，但是，以上都是多余的（而且是非常复杂，不实用的设计）。JDK本身就已经提供了判断线程结束的方法。参考文章：[Java主线程等待子线程、线程池](http://blog.csdn.net/xiao__gui/article/details/9213413)

- 最基本的方法：调用`thread.join()`
- 不太基本的方法：设置`CountDownLatch`成员
- 等待线程池所有线程执行完成的方法：`boolean awaitTermination(long timeout, TimeUnit unit)`

***代码1：join()方法调用***
```java
public class JoinTest {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(){
            public void run(){
                int i = 0;
                while(i < 10){
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread() + ": I am sleeping");
                    i++;
                }
            }
        };
        thread.start();
        thread.join();
        System.out.println("main done");		
	}
}
```
***代码2：线程池等待所有线程执行完成***
```java
public class TestThread extends Thread{  
    public void run(){  
        System.out.println(this.getName() + "子线程开始");  
        try{  
            // 子线程休眠五秒  
            Thread.sleep(5000);  
        }  
        catch (InterruptedException e)  {  
            e.printStackTrace();  
        }  
        System.out.println(this.getName() + "子线程结束");  
    }  
}  

public class Main{  
    public static void main(String[] args){  
        long start = System.currentTimeMillis();  
          
        // 创建一个同时允许两个线程并发执行的线程池  
        ExecutorService executor = Executors.newFixedThreadPool(2);  
        for(int i = 0; i < 5; i++){  
            Thread thread = new TestThread();  
            executor.execute(thread);  
        }  
        executor.shutdown();  
          
        try{  
            // awaitTermination返回false即超时会继续循环，返回true即线程池中的线程执行完成主线程跳出循环往下执行，每隔10秒循环一次  
            while (!executor.awaitTermination(10, TimeUnit.SECONDS));  
        }  
        catch (InterruptedException e){  
            e.printStackTrace();  
        }  
          
        long end = System.currentTimeMillis();  
        System.out.println("子线程执行时长：" + (end - start));  
```

## 2. Java中对应数据结构中的队列、栈、双向队列等的内容

### 2.1. 队列与双向队列

几点说明

- 队列是一种特殊的线性表，它只允许在表的前端进行删除操作，而在表的后端进行插入操作。
- `Queue`是一个接口，定义了`add,offer,remove,poll,element,peek`等方法，方法望文生义，只是针对同一种情况的不同设计。
- `Deque`是一个接口，继承自`Queue`，定义了`add,offer,remove,poll,element,peek`和`addFirst,addLast,offerFirst,offerLast,pollFirst,pollLast,...`等方法，方法望文生义，也是针对同一种情况的不同设计。

各种实现与源码

```java
public interface Queue<E> extends Collection<E>

public interface Deque<E> extends Queue<E>

public abstract class AbstractQueue<E> extends AbstractCollection<E>
    implements Queue<E>

public class LinkedList<E> extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable

public class PriorityQueue<E> extends AbstractQueue<E>
    implements java.io.Serializable

// package java.util.concurrent    
public class ConcurrentLinkedDeque<E> extends AbstractCollection<E>
    implements Deque<E>, java.io.Serializable
public class ConcurrentLinkedQueue<E> extends AbstractQueue<E>
        implements Queue<E>, java.io.Serializable

public interface BlockingQueue<E> extends Queue<E>
public interface BlockingDeque<E> extends BlockingQueue<E>, Deque<E>
public class DelayQueue<E extends Delayed> extends AbstractQueue<E>
    implements BlockingQueue<E>

public class LinkedBlockingDeque<E>
    extends AbstractQueue<E>
    implements BlockingDeque<E>, java.io.Serializable
public class LinkedBlockingQueue<E> extends AbstractQueue<E>
        implements BlockingQueue<E>, java.io.Serializable
public class LinkedTransferQueue<E> extends AbstractQueue<E>
    implements TransferQueue<E>, java.io.Serializable
public class PriorityBlockingQueue<E> extends AbstractQueue<E>
    implements BlockingQueue<E>, java.io.Serializable
public class SynchronousQueue<E> extends AbstractQueue<E>
    implements BlockingQueue<E>, java.io.Serializable

public class ArrayBlockingQueue<E> extends AbstractQueue<E>
        implements BlockingQueue<E>, java.io.Serializable

```
- 从上面可以大致梳理出每种队列形式的类扩展于和实现于哪些类，各种类也是按照不同功能进行命名的，主要出于`java.util`和`java.util.concurrent`两个包。
- `LinkedList`类实现了`Queue`和`Deque`接口，因此我们可以把`LinkedList`当成`Queue`来用。可以视为最普通的队列。
- `PriorityQueue`是优先队列设计，内部使用堆这个数据结构实现。可以通过配置`Comparator`配置最小堆（默认）还是最大堆。


最简单的示范代码
```java
import java.util.LinkedList;
import java.util.Queue;
 
public class Main {
    public static void main(String[] args) {
        //add()和remove()方法在失败的时候会抛出异常(不推荐)
        Queue<String> queue = new LinkedList<String>();
        //添加元素
        queue.offer("a");
        queue.offer("b");
        queue.offer("c");
        queue.offer("d");
        queue.offer("e");
        for(String q : queue){
            System.out.println(q);
        }
        System.out.println("===");
        System.out.println("poll="+queue.poll()); //返回第一个元素，并在队列中删除
        for(String q : queue){
            System.out.println(q);
        }
        System.out.println("===");
        System.out.println("element="+queue.element()); //返回第一个元素 
        for(String q : queue){
            System.out.println(q);
        }
        System.out.println("===");
        System.out.println("peek="+queue.peek()); //返回第一个元素 
        for(String q : queue){
            System.out.println(q);
        }
    }
}
```
### 2.2. 链表与双向链表
链表不用多说，肯定有`LinkedList`，而且是一个双向队列和双向链表。
- 链表的插入和删除操作比`ArrayList`要高，但是查询\随机访问的效率比`ArrayList`要差。
- 一般说法中强调：链表要避免计算长度，因为需要遍历一遍。但是`java`的实现中，每一次`add,offer,remove`等操作都记录并修改了`size`的值。

### 2.3. 栈
Java中有专门的针对“栈”这种数据结构的类，就是`java.util.Stack`，他就是一个类，扩展自`java.util.Vector`，所以本质上基于数组实现。主要提供了`push,pop,peek,empty`等方法。
类中的大部分方法都是同步（线程安全）的。以下是简略源码。
```java
public class Stack<E> extends Vector<E> {
    public Stack()
    public E push(E item)
    public synchronized E pop()
    public synchronized E peek()
    public boolean empty()
    public synchronized int search(Object o)
}

```

### 2.4. 树及红黑树实现的结构

可惜了，java中几乎没有树的结构。跟树有关的可能就只有`TreeSet`和`TreeMap`了吧。

另外，`HashMap`在设计的过程中使用了红黑树（since jdk1.8），当出现哈希碰撞的时候，我们都知道是使用链表来进行保存的，但是**当链表的长度超过8的时候就转换成了红黑树存储了**。

- `TreeSet`和`TreeMap`都是为了集合和映射的排序而实现。都是为了实现有序的集合和映射。内部结构使用的是红黑树。
- `TreeSet`的实现其实和`TreeMap`是很相似的，基本是基于`TreeMap`的方式实现的，毕竟很多集合都是通过映射实现的。

```java
public class TreeSet<E> extends AbstractSet<E>
    implements NavigableSet<E>, Cloneable, java.io.Serializable{
    private transient NavigableMap<E,Object> m;
}

public class TreeMap<K,V>
    extends AbstractMap<K,V>
    implements NavigableMap<K,V>, Cloneable, java.io.Serializable

public interface NavigableMap<K,V> extends SortedMap<K,V>
```

## 3. Java 克隆

### 3.1. 浅拷贝与深拷贝
- 浅克隆（shallow clone），浅拷贝是指拷贝对象时仅仅拷贝对象本身和对象中的基本变量，而不拷贝对象包含的引用指向的对象。 
- 深克隆（deep clone），深拷贝不仅拷贝对象本身，而且拷贝对象包含的引用指向的所有对象。

举例：对象A1中包含对B1的引用，B1中包含对C1的引用。浅拷贝A1得到A2，A2中依然包含对B1的引用，B1中依然包含对C1的引用。深拷贝则是对浅拷贝的递归，深拷贝A1得到A2，A2中包含对B2（B1的copy）的引用，B2中包含对C2（C1的copy）的引用。

拷贝最常用的就是`cloneable`和`serializable`。

- `Cloneable`和`Serializable`都是**标记型接口**，它们内部都没有方法和属性
- [Java中的标记接口（Tag or marker interfaces）](http://www.91yian.com/372.html)是为了声明该类在某个特定集合中的成员资格，JVM看到类标记时会做不同的处理。

### 3.2. `Cloneable`接口
`implements Cloneable`表示该对象能被克隆，能使用`Object.clone()`方法。如果没有`implements Cloneable`的类调用`Object.clone()`方法就会抛出`CloneNotSupportedException`。

`clone()`方法是使用`Object`类的`clone()`方法，但是该方法存在一个缺陷，它并不会将对象的所有属性全部拷贝过来，而是有选择性的拷贝，基本规则如下：

- 基本类型  
如果变量是基本很类型，则拷贝其值，比如 int、float 等。
- 对象  
如果变量是一个实例对象，则拷贝其地址引用，也就是说此时新对象与原来对象是公用该实例变量。
- String 字符串  
若变量为 String 字符串，则拷贝其地址引用。但是在修改时，它会从字符串池中重新生成一个新的字符串，原有紫都城对象保持不变。

所以在使用`implements cloneable`的时候，想要实现深拷贝的话，必须注意在`clone()`方法中对一些对象的引用也进行深拷贝。

### 3.3. `Serializable`接口
[Java 序列化](http://www.runoob.com/java/java-serialization.html)

> 把母对象写入到一个字节流中，再从字节流中将其读出来，这样就可以创建一个新的对象了，并且该新对象与母对象之间并不存在引用共享的问题，真正实现对象的深拷贝。

一个类的对象要想序列化成功，必须满足两个条件：
- 该类必须实现 java.io.Serializable 对象。
- 该类的所有属性必须是可序列化的。如果有一个属性不是可序列化的，则该属性必须注明是短暂的。

如果你想知道一个 Java 标准类是否是可序列化的，请查看该类的文档。检验一个类的实例是否能序列化十分简单， 只需要查看该类有没有实现`java.io.Serializable`接口。

## Java中的`final`关键字
参考：[深入理解Java中的final关键字](http://www.importnew.com/7553.html)
### `final`关键字的含义
final在Java中是一个保留的关键字，可以声明成员变量、方法、类以及本地变量。一旦你将引用声明作final，你将不能改变这个引用了，编译器会检查代码，如果你试图将变量再次初始化的话，编译器会报编译错误
### `final`变量/引用
```java
public static final String LOAN = "loan";
LOAN = new String("loan") //invalid compilation error
```
### `final`方法
方法不可以被子类的方法重写。
```java
class PersonalLoan{
    public final String getName(){
        return "personal loan";
    }
}
 
class CheapPersonalLoan extends PersonalLoan{
    @Override
    public final String getName(){
        return "cheap personal loan"; //compilation error: overridden method is final
    }
}
```
### `final`类
final类通常功能是完整的，它们不能被继承。
```java
final class PersonalLoan{}
class CheapPersonalLoan extends PersonalLoan{  //compilation error: cannot inherit from final class
}
```
### `final`关键字的好处
下面总结了一些使用final关键字的好处
- final关键字提高了性能。JVM和Java应用都会缓存final变量。
- final变量可以安全的在多线程环境下进行共享，而不需要额外的同步开销。
- 使用final关键字，JVM会对方法、变量及类进行优化。
- 不可变类：创建不可变类要使用final关键字。不可变类是指它的对象一旦被创建了就不能被更改了。String是不可变类的代表。不可变类有很多好处，譬如它们的对象是只读的，可以在多线程环境下安全的共享，不用额外的同步开销等等。

## Java中的`transient`关键字
参考：[Java transient关键字使用小记](https://mp.weixin.qq.com/s?subscene=23&__biz=MzIwMTY0NDU3Nw==&mid=2651934932&idx=1&sn=0110681e23e281953bd9b9efdf93a3c4&chksm=8d0f3f9aba78b68c4b265246667458175b767a5aec1e425c019bf6ae5f1f86ff867c6b1be878&scene=7#rd)

- 一旦变量被transient修饰，变量将不再是对象持久化的一部分，该变量内容在序列化后无法获得访问。
- transient关键字只能修饰变量，而不能修饰方法和类。注意，本地变量是不能被transient关键字修饰的。变量如果是用户自定义类变量，则该类需要实现Serializable接口。
- 被transient关键字修饰的变量不再能被序列化，一个静态变量不管是否被transient修饰，均不能被序列化。

第三点确实没错（一个静态变量不管是否被transient修饰，均不能被序列化），反序列化后类中static型变量username的值为当前JVM中对应static变量的值，这个值是JVM中的不是反序列化得出的

## Java中的`ListIterator`
参考：[JAVA中ListIterator和Iterator详解与辨析](http://blog.csdn.net/longshengguoji/article/details/41551491)

- 双向迭代器
- 拥有`add, set`等方法，可以在遍历的同时添加、删除和更改元素
- 可以定位当前的索引位置

`java.util.Collections`使用一个前向一个后向迭代器实现列表的翻转
```java
public static void reverse(List<?> list) {
        int size = list.size();
        if (size < REVERSE_THRESHOLD || list instanceof RandomAccess) {
            for (int i=0, mid=size>>1, j=size-1; i<mid; i++, j--)
                swap(list, i, j);
        } else {
            // instead of using a raw type here, it's possible to capture
            // the wildcard but it will require a call to a supplementary
            // private method
            ListIterator fwd = list.listIterator();
            ListIterator rev = list.listIterator(size);
            for (int i=0, mid=list.size()>>1; i<mid; i++) {
                Object tmp = fwd.next();
                fwd.set(rev.previous());
                rev.set(tmp);
            }
        }
    }
```

## Java中的`HashMap`
java中的`HashMap`是一直在发展变化的，从基本的思想出发到性能的逐渐优化。jdk8中的`HashMap`是有一些变化的。参考文章[Java 8系列之重新认识HashMap](https://tech.meituan.com/java-hashmap.html),有张图片讲的很好。

![jdk8-hashmap-put.png](https://tech.meituan.com/img/java-hashmap/hashMap%20put%E6%96%B9%E6%B3%95%E6%89%A7%E8%A1%8C%E6%B5%81%E7%A8%8B%E5%9B%BE.png)

- jdk8中链表长度超过8之后就转换成了一棵红黑树
- jdk8中rehash过程更简单，不用重新计算，只需要检测多出来的一位是1还是0就行，是1的话就移动oldCap的长度，否则与原来位置相同。而且resize之后链表不会倒过来。
