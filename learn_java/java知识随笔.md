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
