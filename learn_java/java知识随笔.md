# Java 知识随笔

## 等待线程结束的方法有哪些？
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
    }  
}  
```

## Java中对应数据结构中的队列、栈、双向队列等的内容

### 队列与双向队列

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
### 链表与双向链表
链表不用多说，肯定有`LinkedList`，而且是一个双向队列和双向链表。
- 链表的插入和删除操作比`ArrayList`要高，但是查询\随机访问的效率比`ArrayList`要差。
- 一般说法中强调：链表要避免计算长度，因为需要遍历一遍。但是`java`的实现中，每一次`add,offer,remove`等操作都记录并修改了`size`的值。

### 栈
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

### 树及红黑树实现的结构
可惜了，java中就没有树的结构。跟树有关的可能就只有`TreeSet`和`TreeMap`了吧。

- `TreeSet`和`TreeMap`都是为了集合和映射的排序而实现。都是为了实现有序的集合和映射。
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