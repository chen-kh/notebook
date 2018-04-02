---
title: Java需要准备的考点
categories: [Java知识]
tags: [Java, JVM]
---
# Java需要准备的考点
<!-- TOC -->

- [Java源码结构与基础](#java源码结构与基础)
    - [Java集合（collection和map）](#java集合collection和map)
        - [List的逆向访问](#list的逆向访问)
        - [ArrayList 与 LinkedList 的区别](#arraylist-与-linkedlist-的区别)
        - [HashMap 与 HashTable 的区别](#hashmap-与-hashtable-的区别)
        - [LinkedHashSet，LinkedHashMap, ConcurrentHashMap](#linkedhashsetlinkedhashmap-concurrenthashmap)
            - [ConcurrentHashMap：其实属于java.util.concurrent包](#concurrenthashmap其实属于javautilconcurrent包)
            - [LinkedHashMap](#linkedhashmap)
            - [LinkedHashSet（与HashSet）](#linkedhashset与hashset)
    - [Java Collections](#java-collections)
    - [接口与抽象类的区别](#接口与抽象类的区别)
    - [异常Exceptions](#异常exceptions)
    - [Java并发工具类](#java并发工具类)
    - [比较两个相似的数据类型要考虑的方面](#比较两个相似的数据类型要考虑的方面)
    - [参考问题](#参考问题)
- [多线程与并发](#多线程与并发)
    - [volatile变量的理解](#volatile变量的理解)
    - [什么是线程安全](#什么是线程安全)
    - [Java的Runnable，Collable以及Future](#java的runnablecollable以及future)
    - [继承Thread和实现Runnable的区别是什么](#继承thread和实现runnable的区别是什么)
    - [Difference between notify and notifyAll in Java](#difference-between-notify-and-notifyall-in-java)
    - [线程池](#线程池)
    - [锁](#锁)
        - [可重入锁-`ReentrantLock`](#可重入锁-reentrantlock)
        - [读写锁-`ReadWriteLock`](#读写锁-readwritelock)
- [Java虚拟机](#java虚拟机)
    - [Java内存区域](#java内存区域)
        - [程序计数器](#程序计数器)
        - [JVM栈与本地方法栈](#jvm栈与本地方法栈)
        - [Java堆与方法区](#java堆与方法区)
        - [运行时常量池](#运行时常量池)
- [参考资料](#参考资料)

<!-- /TOC -->
## Java源码结构与基础
参考：[JDK基础概念及目录结构](https://www.jianshu.com/p/f98c3acd8df8)
### Java集合（collection和map）
![java 集合结构图](http://img.blog.csdn.net/20160121141321874)
![java 集合结构图2](http://www.runoob.com/wp-content/uploads/2014/01/java-coll.png)
![java 集合结构图3](https://i2.wp.com/p3lang.com/wp-content/uploads/2013/06/Java-Collections-Framework-List-Set-Queue.png)
![java Map结构图](https://i1.wp.com/p3lang.com/wp-content/uploads/2013/06/Java-Collections-Framwork-Map.png)

#### List的逆向访问
```java
// Substitute appropriate type.
ArrayList<...> a = new ArrayList<...>();// OR LinkedList
// Add elements to list.
// Generate an iterator. Start just after the last element.
ListIterator li = a.listIterator(a.size());
// Iterate in reverse.
while(li.hasPrevious()) {
  System.out.println(li.previous());
}
```
#### ArrayList 与 LinkedList 的区别
1) 因为Array是基于索引(index)的数据结构，它使用索引在数组中搜索和读取数据是很快的。Array获取数据的时间复杂度是O(1),但是要删除数据却是开销很大的，因为这需要重排数组中的所有数据。

2) 相对于ArrayList，LinkedList插入是更快的。因为LinkedList不像ArrayList一样，不需要改变数组的大小，也不需要在数组装满的时候要将所有的数据重新装入一个新的数组，这是ArrayList最坏的一种情况，时间复杂度是O(n)，而LinkedList中插入或删除的时间复杂度仅为O(1)。ArrayList在插入数据时还需要更新索引（除了插入数组的尾部）。

3) 类似于插入数据，删除数据时，LinkedList也优于ArrayList。

4) LinkedList需要更多的内存，因为ArrayList的每个索引的位置是实际的数据，而LinkedList中的每个节点中存储的是实际的数据和前后节点的位置。
#### HashMap 与 HashTable 的区别
> HashMap和Hashtable都实现了Map接口，但决定用哪一个之前先要弄清楚它们之间的分别。主要的区别有：线程安全性，同步(synchronization)，以及速度。

参考：[HashMap和HashTable到底哪不同？](http://zhaox.github.io/2016/07/05/hashmap-vs-hashtable)
1. HashMap几乎可以等价于Hashtable，除了HashMap是非synchronized的，并可以接受null(HashMap可以接受为null的键值(key)和值(value)，而Hashtable则不行)。  
>HashMap是支持null键和null值的，而HashTable在遇到null时，会抛出NullPointerException异常。这并不是因为HashTable有什么特殊的实现层面的原因导致不能支持null键和null值，这仅仅是因为HashMap在实现时对null做了特殊处理，将null的hashCode值定为了0，从而将其存放在哈希表的第0个bucket中。
2. HashMap是非synchronized，而Hashtable是synchronized，这意味着Hashtable是线程安全的，多个线程可以共享一个Hashtable；而如果没有正确的同步的话，多个线程是不能共享HashMap的。**Java 5提供了ConcurrentHashMap，它是HashTable的替代，比HashTable的扩展性更好。**  我们能否让HashMap同步？HashMap可以通过下面的语句进行同步：
```java
Map m = Collections.synchronizeMap(hashMap);
```
HashTable对线程安全的实现基本也就是给方法加了同步描述符：
```java
public synchronized V get(Object key) {
    Entry tab[] = table;
    int hash = hash(key);
    int index = (hash & 0x7FFFFFFF) % tab.length;
    for (Entry<K,V> e = tab[index] ; e != null ; e = e.next) {
        if ((e.hash == hash) && e.key.equals(key)) {
            return e.value;
        }
    }
    return null;
}

public Set<K> keySet() {
    if (keySet == null)
        keySet = Collections.synchronizedSet(new KeySet(), this);
    return keySet;
}

```
3. 另一个区别是HashMap的迭代器(Iterator)是fail-fast迭代器，而Hashtable的enumerator迭代器不是fail-fast的。所以当有其它线程改变了HashMap的结构（增加或者移除元素），将会抛出ConcurrentModificationException，但迭代器本身的remove()方法移除元素则不会抛出ConcurrentModificationException异常。但这并不是一个一定发生的行为，要看JVM。这条同样也是Enumeration和Iterator的区别。  
4. 由于Hashtable是线程安全的也是synchronized，所以在单线程环境下它比HashMap要慢。如果你不需要同步，只需要单一线程，那么使用HashMap性能要好过Hashtable。  
5. HashMap不能保证随着时间的推移Map中的元素次序是不变的。[漫画：高并发下的HashMap](https://mp.weixin.qq.com/s?subscene=23&__biz=MjM5MDcxMTU2Nw==&mid=2650577125&idx=2&sn=adc4d9613b1ece8e824baf83818e61b2&chksm=be489285893f1b93afe2607ce029126dd8323d606e3aea5e21b9569b90205f1739158bedbc7e&scene=7#rd)
6. HashTable已经被淘汰了，不要在代码中再使用它。
> - 简单来说就是，如果你不需要线程安全，那么使用HashMap，如果需要线程安全，那么使用ConcurrentHashMap。HashTable已经被淘汰了，不要在新的代码中再使用它。  
> - 虽然HashMap和HashTable的公开接口应该不会改变，或者说改变不频繁。但每一版本的JDK，都会对HashMap和HashTable的内部实现做优化，比如上文曾提到的JDK 1.8的红黑树优化。所以，尽可能的使用新版本的JDK吧，除了那些炫酷的新功能，普通的API也会有性能上有提升。  
> - 为什么HashTable已经淘汰了，还要优化它？因为有老的代码还在使用它，所以优化了它之后，这些老的代码也能获得性能提升
#### LinkedHashSet，LinkedHashMap, ConcurrentHashMap
##### ConcurrentHashMap：其实属于java.util.concurrent包
参考：

- [漫画：什么是ConcurrentHashMap？](https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653192083&idx=1&sn=5c4becd5724dd72ad489b9ed466329f5&chksm=8c990d49bbee845f69345e4121888ec967df27988bc66afd984a25331d2f6464a61dc0335a54&scene=21#wechat_redirect)
- [ConcurrentHashMap 的实现原理](http://wiki.jikexueyuan.com/project/java-collection/concurrenthashmap.html)
- [探索 ConcurrentHashMap 高并发性的实现机制](https://www.ibm.com/developerworks/cn/java/java-lo-concurrenthashmap/index.html)、
- [ConcurrentHashMap总结](http://www.importnew.com/22007.html)：最重要！！！jdk6、7和8的实现有很大差别！！！
- [Java进阶（六）从ConcurrentHashMap的演进看Java多线程核心技术](http://www.jasongj.com/java/concurrenthashmap/)：主讲java8，图画的很好

![concurrenthashmap segment](http://wiki.jikexueyuan.com/project/java-collection/images/concurrenthashmap3.jpg)

> 在实际的应用中，散列表一般的应用场景是：除了少数插入操作和删除操作外，绝大多数都是读取操作，而且读操作在大多数时候都是成功的。正是基于这个前提，ConcurrentHashMap 针对读操作做了大量的优化。通过 HashEntry 对象的不变性和用 volatile 型变量协调线程间的内存可见性，使得 大多数时候，读操作不需要加锁就可以正确获得值。这个特性使得 ConcurrentHashMap 的并发性能在分离锁的基础上又有了近一步的提高。
>
> ConcurrentHashMap 是一个并发散列映射表的实现，它允许完全并发的读取，并且支持给定数量的并发更新。相比于 HashTable 和用同步包装器包装的 HashMap（Collections.synchronizedMap(new HashMap())），ConcurrentHashMap 拥有更高的并发性。在 HashTable 和由同步包装器包装的 HashMap 中，使用一个全局的锁来同步不同线程间的并发访问。同一时间点，只能有一个线程持有锁，也就是说在同一时间点，只能有一个线程能访问容器。这虽然保证多线程间的安全并发访问，但同时也导致对容器的访问变成串行化的了。
>
> ConcurrentHashMap 的高并发性主要来自于三个方面：
>
> - 用分离锁实现多个线程间的更深层次的共享访问。
>- 用 HashEntery 对象的不变性来降低执行读操作的线程在遍历链表期间对加锁的需求。
> - 通过对同一个 Volatile 变量的写 / 读访问，协调不同线程间读 / 写操作的内存可见性。
> 使用分离锁，减小了请求 同一个锁的频率。
>
> 通过 HashEntery 对象的不变性及对同一个 Volatile 变量的读 / 写来协调内存可见性，使得 读操作大多数时候不需要加锁就能成功获取到需要的值。由于散列映射表在实际应用中大多数操作都是成功的 读操作，所以 2 和 3 既可以减少请求同一个锁的频率，也可以有效减少持有锁的时间。通过减小请求同一个锁的频率和尽量减少持有锁的时间 ，使得 ConcurrentHashMap 的并发性相对于 HashTable 和用同步包装器包装的 HashMap有了质的提高。

##### LinkedHashMap
参考：[LinkedHashMap 的实现原理](http://wiki.jikexueyuan.com/project/java-collection/linkedhashmap.html)

JAVA 在 JDK1.4 以后提供了 LinkedHashMap 来帮助我们实现了**有序的 HashMap**！

> LinkedHashMap 是 HashMap 的一个子类，它**保留插入的顺序**，如果需要输出的顺序和输入时的相同，那么就选用 LinkedHashMap。

根据链表中元素的顺序可以分为：按插入顺序的链表，和按访问顺序(调用 get 方法)的链表。默认是按插入顺序排序，如果指定按访问顺序排序，那么调用get方法后，会将这次访问的元素移至链表尾部，不断访问可以形成按访问顺序排序的链表。

![linkedhashmap](https://cloud.githubusercontent.com/assets/1736354/6981649/03eb9014-da38-11e4-9cbf-03d9c21f05f2.png)
##### LinkedHashSet（与HashSet）
参考：[LinkedHashSet 的实现原理](http://wiki.jikexueyuan.com/project/java-collection/linkedhashset.html)、[Java LinkedHashSet工作原理及实现](http://yikun.github.io/2015/04/09/Java-LinkedHashSet%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86%E5%8F%8A%E5%AE%9E%E7%8E%B0/)
1. LinkedHashSet 是 Set 的一个具体实现，其维护着一个运行于所有条目的双重链接列表。此链接列表定义了迭代顺序，该迭代顺序可为插入顺序或是访问顺序。
1. LinkedHashSet 继承与 HashSet，并且其内部是通过 LinkedHashMap 来实现的。有点类似于我们之前说的LinkedHashMap 其内部是基于 Hashmap 实现一样，不过还是有一点点区别的（具体的区别大家可以自己去思考一下）。
1. 如果我们需要迭代的顺序为插入顺序或者访问顺序，那么 LinkedHashSet 是需要你首先考虑的。
1. 关键代码
```java
public class LinkedHashSet<E>
    extends HashSet<E>
    implements Set<E>, Cloneable, java.io.Serializable{
      
}

HashSet(int initialCapacity, float loadFactor, boolean dummy) {
    map = new LinkedHashMap<>(initialCapacity, loadFactor);
}
```
- HashSet实现原理图：基于HashMap，PRESENT是补充的value
![HashSet实现原理](https://cloud.githubusercontent.com/assets/1736354/7060522/0bcfd890-deb5-11e4-97b3-d4e811766893.png)
- LinkedHashSet实现原理图
![LinkedHashSet实现原理图](https://cloud.githubusercontent.com/assets/1736354/7082382/14d44b8e-df86-11e4-8e50-1e925f430b6e.png)
### Java Collections
[Collections (java.util.Collections)](https://docs.oracle.com/javase/7/docs/api/java/util/Collections.html) 工具类包含了大量针对Collection/Map操作的**静态方法**，使用这些方法能帮我们简化代码。
1. 排序操作（主要针对List接口相关）
- reverse(List list)：反转指定List集合中元素的顺序
- shuffle(List list)：对List中的元素进行随机排序（洗牌）
- sort(List list)：对List里的元素根据自然升序排序
- sort(List list, Comparator c)：自定义比较器进行排序
- swap(List list, int i, int j)：将指定List集合中i处元素和j出元素进行交换
- rotate(List list, int distance)：将所有元素向右移位指定长度，如果distance等于size那么结果不变
2. 查找和替换（主要针对Collection接口相关）
- binarySearch(List list, Object key)：使用二分搜索法，以获得指定对象在List中的索引，前提是集合已经排序
- max(Collection coll)：返回最大元素
- max(Collection coll, Comparator comp)：根据自定义比较器，返回最大元素
- min(Collection coll)：返回最小元素
- min(Collection coll, Comparator comp)：根据自定义比较器，返回最小元素
- fill(List list, Object obj)：使用指定对象填充
- frequency(Collection Object o)：返回指定集合中指定对象出现的次数
- replaceAll(List list, Object old, Object new)：替换
3. 同步控制
- Collections工具类中提供了多个`synchronizedXxx`方法，该方法返回指定集合对象对应的同步对象，从而解决多线程并发访问集合时线程的安全问题。HashSet、ArrayList、HashMap都是线程不安全的，如果需要考虑同步，则使用这些方法。这些方法主要有：`synchronizedSet、synchronizedSortedSet、synchronizedList、synchronizedMap、synchronizedSortedMap`。
- 特别需要指出的是，在使用迭代方法遍历集合时需要手工同步返回的集合。
4. 设置不可变集合  
Collections有三类方法可返回一个不可变集合：
- emptyXxx()：返回一个空的不可变的集合对象
- singletonXxx()：返回一个只包含指定对象的，不可变的集合对象。
- unmodifiableXxx()：返回指定集合对象的不可变视图
5. 其它  
- disjoint(Collection<?> c1, Collection<?> c2) - 如果两个指定 collection 中没有相同的元素，则返回 true。
- addAll(Collection<? super T> c, T... a) - 一种方便的方式，将所有指定元素添加到指定 collection 中。示范： 
Collections.addAll(flavors, "Peaches 'n Plutonium", "Rocky Racoon");
- Comparator<T> reverseOrder(Comparator<T> cmp) - 返回一个比较器，它强行反转指定比较器的顺序。如果指定比较器为 null，则此方法等同于 reverseOrder()（换句话说，它返回一个比较器，该比较器将强行反转实现 Comparable 接口那些对象 collection 上的自然顺序）。
### 接口与抽象类的区别
- 一个子类只能继承一个抽象类，但能实现多个接口
- 抽象类可以有构造方法，接口没有构造方法
- 抽象类可以有普通成员变量，接口没有普通成员变量
- 抽象类和接口都可有静态成员变量，抽象类中的静态成员变量访问类型任意，接口只能public staic final （默认）
- 抽象类可以没有抽象方法，抽象类可以有普通方法，接口中都是抽象方法
- 抽象类可以有静态方法，接口不能有静态方法
- 抽象类中的方法可以是public，protected，接口只有public abstract
### 异常Exceptions
### Java并发工具类
### 比较两个相似的数据类型要考虑的方面
- 接口实现的不同
- 存储形式的不同（随机还是连续）
- 针对的应用场景不同
- 线程安全角度的不同
- 共同操作的开销问题（效率问题，时间开销和内存开销）
### 参考问题
1. [为什么链表按照index访问比较慢？](https://stackoverflow.com/questions/37769428/why-is-accessing-an-item-by-index-slower-in-a-linked-list-than-an-array)
2. [为什么Java.util.LinkedList不方便访问元素的下一个（next和preview的直接调用）？](https://stackoverflow.com/questions/4927858/java-util-linked-list-how-to-find-next)
>我不知道你使用的是什么 Node 类，但 LinkedList<T> 有它自己的内部节点类，你不能访问。 调用 add值添加到列表——你不能显式地插入一个节点值,或以任何其他方式访问节点本身。 是的有时候会很痛苦。
>如果你需要具有节点 public 封装的链接列表，则需要找到另一个实现或者滚动你自己的列表。
3. [HashMap和HashTable到底哪不同？](http://zhaox.github.io/2016/07/05/hashmap-vs-hashtable)
## 多线程与并发
参考：[Java并发编程：Callable、Future和FutureTask](http://www.cnblogs.com/dolphin0520/p/3949310.html)
### volatile变量的理解

参考[Java中volatile变量的理解与正确使用](https://mp.weixin.qq.com/s?subscene=23&__biz=MjM5NzM0MjcyMQ==&mid=2650072057&idx=3&sn=0eb6dd4be610de53293d124c4e0498b3&chksm=bedb389789acb181347f0867d234b5ef500afff2d986248cf53ea1e4b866afd1ace51da7faba&scene=7#rd)，[漫画：什么是 volatile 关键字？](https://mp.weixin.qq.com/s?subscene=23&__biz=MzIxMjE5MTE1Nw==&mid=2653192450&idx=2&sn=ad95717051c0c4af83923b736a5bc637&chksm=8c99f3d8bbee7aceb123e4f6aa9a220630b5aa17743ba812d82308bfb6a8ed8303bdd181f144&scene=7#rd)

> - volatile标示的变量保证了可见性，也就是线程用到该变量时必须从内存读取新值，在更改该变量时必须将指刷新到主内存中。  
> - volatile变量适用于那些一写多读的应用场景，而多写的场景并不能保证线程安全

Java语言提供了一种稍弱的同步机制，即volatile变量。作用与说明有三：
- 用来确保将变量的更新操作通知到其它线程，保证了新值能够立即同步到主内存，以及每次使用前立即从主内存刷新。
- volatile的另一个语义是禁止指令重排序优化。
- volatile并不保证原子性，也就是不能保证线程安全。
### 什么是线程安全
如果代码有多个线程同时运行，而这些线程可能会同时运行这段代码，如果运行结果和单线程运行结果一样，就是线程安全的。java.util.concurrent包里面的类，就是为并行线程安全提供的类型包。
### Java的Runnable，Collable以及Future
- Runnable应该是我们最熟悉的接口，它只有一个run()函数，用于将耗时操作写在其中，该函数**没有返回值**。
- Callable与Runnable的功能大致相似，Callable中有一个call()函数，**但是call()函数有返回值**，而Runnable的run()函数不能将结果返回给客户程序。
- Executor就是Runnable和Callable的调度容器，Future就是对于具体的Runnable或者Callable任务的执行结果进行取消、查询是否完成、获取结果、设置结果操作。get方法会阻塞，直到任务返回结果。
- FutureTask则是一个RunnableFuture<V>，而RunnableFuture实现了Runnbale又实现了Futrue<V>这两个接口
```java
public interface Runnable {    
    public abstract void run();  
}  

public interface Callable<V> {  
    V call() throws Exception;  
}  

public interface Future<V> {  
    boolean cancel(boolean mayInterruptIfRunning);  
    boolean isCancelled();  
    boolean isDone();  
    V get() throws InterruptedException, ExecutionException;  
    V get(long timeout, TimeUnit unit)  
        throws InterruptedException, ExecutionException, TimeoutException;  
}  

public class FutureTask<V> implements RunnableFuture<V>  {}
public interface RunnableFuture<V> extends Runnable, Future<V> {  
    void run();  
}  
```
- 简单示例
```java
import java.util.concurrent.Callable;  
import java.util.concurrent.ExecutionException;  
import java.util.concurrent.ExecutorService;  
import java.util.concurrent.Executors;  
import java.util.concurrent.Future;  
import java.util.concurrent.FutureTask;  
  
/** 
 *  
 * @author mrsimple 
 * 
 */  
public class RunnableFutureTask {  
  
    /** 
     * ExecutorService 
     */  
    static ExecutorService mExecutor = Executors.newSingleThreadExecutor();  
  
    /** 
     *  
     * @param args 
     */  
    public static void main(String[] args) {  
        runnableDemo();  
        futureDemo();  
    }  
  
    /** 
     * runnable, 无返回值 
     */  
    static void runnableDemo() {  
  
        new Thread(new Runnable() {  
  
            @Override  
            public void run() {  
                System.out.println("runnable demo : " + fibc(20));  
            }  
        }).start();  
    }  
  
    /** 
     * 其中Runnable实现的是void run()方法，无返回值；Callable实现的是 V 
     * call()方法，并且可以返回执行结果。其中Runnable可以提交给Thread来包装下 
     * ，直接启动一个线程来执行，而Callable则一般都是提交给ExecuteService来执行。 
     */  
    static void futureDemo() {  
        try {  
            /** 
             * 提交runnable则没有返回值, future没有数据 
             */  
            Future<?> result = mExecutor.submit(new Runnable() {  
  
                @Override  
                public void run() {  
                    fibc(20);  
                }  
            });  
  
            System.out.println("future result from runnable : " + result.get());  
  
            /** 
             * 提交Callable, 有返回值, future中能够获取返回值 
             */  
            Future<Integer> result2 = mExecutor.submit(new Callable<Integer>() {  
                @Override  
                public Integer call() throws Exception {  
                    return fibc(20);  
                }  
            });  
  
            System.out  
                    .println("future result from callable : " + result2.get());  
  
            /** 
             * FutureTask则是一个RunnableFuture<V>，即实现了Runnbale又实现了Futrue<V>这两个接口， 
             * 另外它还可以包装Runnable(实际上会转换为Callable)和Callable 
             * <V>，所以一般来讲是一个符合体了，它可以通过Thread包装来直接执行，也可以提交给ExecuteService来执行 
             * ，并且还可以通过v get()返回执行结果，在线程体没有执行完成的时候，主线程一直阻塞等待，执行完则直接返回结果。 
             */  
            FutureTask<Integer> futureTask = new FutureTask<Integer>(  
                    new Callable<Integer>() {  
                        @Override  
                        public Integer call() throws Exception {  
                            return fibc(20);  
                        }  
                    });  
            // 提交futureTask  
            mExecutor.submit(futureTask) ;  
            System.out.println("future result from futureTask : "  
                    + futureTask.get());  
  
        } catch (InterruptedException e) {  
            e.printStackTrace();  
        } catch (ExecutionException e) {  
            e.printStackTrace();  
        }  
    }  
  
    /** 
     * 效率底下的斐波那契数列, 耗时的操作 
     *  
     * @param num 
     * @return 
     */  
    static int fibc(int num) {  
        if (num == 0) {  
            return 0;  
        }  
        if (num == 1) {  
            return 1;  
        }  
        return fibc(num - 1) + fibc(num - 2);  
    }  
  
} 
```
### 继承Thread和实现Runnable的区别是什么
1. Thread和Runnable都可以实现多线程 
2. Thread是类，而Runnable是接口，这就是类和接口区别，类只能继承一次，而接口可以实现多个接口。 
3. Thread实现Runnable接口，这个可以查看Thread的源代码。 
4. 最重要的分享资源功能，一般我们使用多线程就是快速解决资源问题。Runnable可以实现资源分享，类实现Runnable并不具备线程功能，必须通过new Thread(runabble子类)调用start()启动线程，所以我们通常new一个runnable的子类，启动多个线程解决资源问题。Thread是类所以我们每次new一个对象时候资源已经实例化了，不能资源共享，Thread类要实现资源共享，可以声明变量为static，类共享的可以解决。 
5. 通过以上建议最好实现Runnable接口 实现多线程。 
6. 这2种方式都有一个**缺陷**就是：**在执行完任务之后无法获取执行结果。**

所以我们需要有Future
### Difference between notify and notifyAll in Java

>Java provides two methods notify and notifyAll for waking up threads waiting on some condition and you can use any of them but there is a subtle difference between notify and notifyAll in Java which makes it one of the popular multi-threading interview questions in Java. <u>When you call notify only **one of waiting** for the thread will be woken and it's not guaranteed which thread will be woken, it depends on upon Thread scheduler. While if you call notifyAll method, **all threads waiting** on that lock will be woken up, but again all woken thread will fight for lock before executing remaining code</u> and that's why **wait is called on loop** because if multiple threads are woken up, the thread which will get lock will first execute and it may reset waiting for condition, which will force subsequent threads to wait. So key difference between notify and notifyAll is that notify() will cause only one thread to wake up while notifyAll method will make all thread to wake up.

### 线程池

### 锁
参考
- [Java中的锁分类](http://www.cnblogs.com/qifengshi/p/6831055.html)
- [Java可重入锁详解](https://www.jianshu.com/p/f47250702ee7)
- [Java同步框架AbstractQueuedSynchronizer](https://www.jianshu.com/p/853b203a8d93)
#### 可重入锁-`ReentrantLock`
如果当前线程已经获得了某个监视器对象所持有的锁，那么该线程在该方法中调用另外一个同步方法也同样持有该锁。如果锁不具有可重入性特点的话，那么线程在调用同步方法、含有锁的方法时就会产生死锁。
#### 读写锁-`ReadWriteLock`
其读锁是共享锁，其写锁是独享锁。
读锁的共享锁可保证并发读是非常高效的，读写，写读 ，写写的过程是互斥的。

## Java虚拟机
### Java内存区域
参考：[Java运行时数据区域](https://www.jianshu.com/p/6173a467165e)

Java运行时的数据区域：程序计数器（Program Counter Register）、JVM栈、本地方法栈（Native Method Stack）、Java堆（Heap）、方法区（Method Area）以及运行时常量池、直接内存

![java运行时数据区](java运行时的数据区.png)

#### 程序计数器
程序计数器占用较小的内存空间，可以看做是**当前线程所执行的字节码的行号指示器**，由于Java虚拟机的多线程是通过线程轮流切换并分配处理器执行时间的方式来实现的，在任何一个确定的时刻，一个处理器（对于多核处理器来说就是一个内核）都只会执行一条线程中的指令。因此，为了**线程切换后能够恢复到正确的执行位置**，每条线程都需要有一个独立的程序计数器。

如果线程正在执行Java方法，则计数器记录的是正在执行的虚拟机字节码指令的地址；如果正在执行的是Native方法，则这个计数器则为空。

#### JVM栈与本地方法栈
- 虚拟机栈

![虚拟机栈](虚拟机栈.png)

#### Java堆与方法区
- Java堆

对大多数应用来说，Java堆（Heap）是Java虚拟机所管理的**内存中最大的一块**，Java堆是**被所有线程共享**的一块内存区域，在虚拟机启动时创建。该内存区域唯一的目的就是存放对象实例，**Java对象实例以及数组**都在堆上分配（随着JIT编译器发展等技术成熟，所有对象分配在堆上也渐渐不是那么“绝对”了）。

Java堆是**垃圾收集器管理的主要区域**，因此Java堆也常被称为“GC堆”，由于现在收集器基于分代收集算法，Java堆还可以细分为：新生代和老年代。

根据Java虚拟机规范的规定，Java堆可以处于物理上不连续的内存空间中，只要逻辑上是连续的即可，就像我们的磁盘空间一样（或者说，像链表一样虽然内存上不一定连续，但逻辑上是连续）。如果在堆中没有内存完成实例分配，而且堆也没办法再扩展时，将会抛出**OutOfMemoryError异常**。

- 方法区

方法区与Java堆一样，是各个线程共享的内存区域，用于存储已被虚拟机加载的**类信息、常量、静态变量、即时编译器编译后的代码**等数据。Java虚拟机规范对方法区的限制非常宽松，除了和Java堆一样不需要连续的内存和可以选择固定大小或者可拓展外，还可以选择不实现垃圾收集。相对而言，垃圾收集行为在这个区域是比较少出现的，但并非数据进入了方法区就成为了永久代。该区域的内存回收目标主要是针对常量池的回收和对类型的卸载。

Java虚拟机规范规定，当方法区无法满足内存分配需求时，讲抛出OutOfMemoryError异常。

#### 运行时常量池
运行时常量池与class文件的常量池不同，应该是运行时常量池包含class文件中的常量池。

**运行时常量池是方法区**的一部分，Class文件中除了有关类的版本、字段、方法、接口等描述信息外，还有一项信息是常量池，用于存放编译期生成的各种字面量和符号引用，这部分内容将在类加载后进入方法区的运行时常量池中存放。

运行时常量池相对于Class文件常量池的另一个重要特征是具备动态性，Java语言并非不要求常量一定只有编译期才能产生，也就是并非预置入Class文件中常量池的内容才能进入方法区运行时常量池，运行期间也可以将新的常量池放入池中。


## 参考资料
0. [Java线程面试题 Top 50](http://www.cnblogs.com/dolphin0520/p/3958019.html)
1. [Java源码分析](http://blog.csdn.net/column/details/java-source-study.html)
2. [HashMap和HashTable到底哪不同？](http://zhaox.github.io/2016/07/05/hashmap-vs-hashtable)
3. [ConcurrentHashMap 的实现原理](http://wiki.jikexueyuan.com/project/java-collection/concurrenthashmap.html)
4. [探索 ConcurrentHashMap 高并发性的实现机制](https://www.ibm.com/developerworks/cn/java/java-lo-concurrenthashmap/index.html)
5. [LinkedHashMap 的实现原理](http://wiki.jikexueyuan.com/project/java-collection/linkedhashmap.html)
6. [JDK基础概念及目录结构](https://www.jianshu.com/p/f98c3acd8df8)
