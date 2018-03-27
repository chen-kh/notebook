# Hadoop面试内容整理

Hadoop的面试内容主要分为3各部分，首先接触过Hadoop的一定会问MapReduce编程模型的详细过程，然后可以问一些文件系统的东西，最后可能问一下与Hadoop相关的衍生品：HBase等。
- MapReduce
- Hadoop Distributed File System（HDFS）  
- HBase等  

参考资料： 
- [Hadoop 面试，有它就够了](https://www.jianshu.com/p/c97ff0ab5f49)、[同名另外一版本](http://k.sina.com.cn/article_1708729084_65d922fc034002mnt.html)
- [Hadoop MapReduce执行过程详解（带hadoop例子）](https://my.oschina.net/itblog/blog/275294)
- [Hadoop核心架构HDFS+MapReduce+Hbase+Hive内部机理详解](https://www.csdn.net/article/2014-02-17/2818431-HDFS+MapReduce+Hbase)

## Hadoop MapReduce
只要搞懂下面这个架构图就可以了。  
![MR架构](https://upload-images.jianshu.io/upload_images/697231-2fd012f3d2074e26)

下面把这个过程分为Mapper和Reducer两个阶段进行分析。

### Mapper任务的执行过程详解
每个Mapper是一个java进程，Mapper之间做的工作都一样，数量可以配置。任务执行过程如下。

1. **InputSplit**：把输入文件按照一定的标准分片，每个输入片的大小是固定的。默认情况下，输入片(InputSplit)的大小与数据块(Block)的大小是相同的，默认值64MB。输入文件有两个，一个是32MB，一个是72MB。那么小的文件是一个输入片，大文件会分为两个数据块，那么是两个输入片。一共产生三个输入片。每一个输入片由一个Mapper进程处理。这里的三个输入片，会有三个Mapper进程处理。

2. **Map Phase**：其实有两个阶段，如果我们看`WordCount`的源码就会发现，`Mapper`的输入包含`Object key, Text value, Context context`，输入已经包含了key-value对。根据第一步输入的分片，首先按行划分成key=行号，value=行内容的结构，然后Mapper使用map函数对没一个键值对进行处理，可以对value进行进一步的单词划分。其输出结果是单词-计数级别的键值对。

3. **Partition**：对第二步的输出进行基于key的分区，分区数量与reducer数量相当。这样相同key的数据就到了一个分区中。

4. **Sort**：相同分区中的键值对进行按照先键后值的比较方式排序。

5. **Combine**：排序完成后，相同key（也相邻）进行整合以减少网络开销。一次partition级别的reduce

注意：为了减少网络开销，每个Mapper设置一个缓冲区，并设置一个溢出值，分别为100M和0.8。当数据量大的时候会有多个溢出文件，在进入Reduce阶段会进行多个溢出文件整合。

### Reducer任务的执行过程详解
1. 第一阶段是Reducer任务会主动从Mapper任务复制其输出的键值对。Mapper任务可能会有很多，因此Reducer会复制多个Mapper的输出。

2. 第二阶段是把复制到Reducer本地数据，全部进行合并，即把分散的数据合并成一个大的数据。再对合并后的数据排序。这里复制的数据是某个`key.hash()`的partition数据，然后多个partition的数据进行融合。

3. 第三阶段是对排序后的键值对调用reduce方法。键相等的键值对调用一次reduce方法，每次调用会产生零个或者多个键值对。最后把这些输出的键值对写入到HDFS文件中。

注意：由于一次Reducer处理过程只处理某相同`key.hash()`的分区，因此多个reducer的结果数据不需要合并。

## Hadoop Distributed File System
![HDFS架构1](https://hadoop.apache.org/docs/r1.0.4/cn/images/hdfsarchitecture.gif)

参考：
- [Hadoop分布式文件系统：架构与设计](https://hadoop.apache.org/docs/r1.0.4/cn/hdfs_design.html)：这是很早的一个文档，不过也挺有参考价值。
- [HDFS_Architecture](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html#HDFS_Architecture)：上个文件比较新的版本，基本内容差不多。
- [HDFS·面试宝典](https://troywu0.gitbooks.io/spark/content/hdfs.html)：简略版面试总结，看完上面详细的文档之后可以看一下这个，梳理主要内容。

### 总结性介绍
- Hadoop分布式文件系统(HDFS)被设计成适合运行在通用硬件(commodity hardware)上的分布式文件系统。
- HDFS是一个高度容错性的系统，适合部署在廉价的机器上。
- HDFS能提供高吞吐量的数据访问，非常适合大规模数据集上的应用。

### 一些缺点
- 不适合低延迟数据访问
- 无法高效存储大量小文件
- 不支持多用户写入及任意修改文件。
> 副本系数可以在文件创建的时候指定，也可以在之后改变。HDFS中的文件都是一次性写入的，并且**严格要求在任何时候只能有一个写入者**
### 简化的一致性模型
HDFS应用需要一个“一次写入多次读取”的文件访问模型。一个文件经过创建、写入和关闭之后就不需要改变。这一假设简化了数据一致性问题，并且使高吞吐量的数据访问成为可能。Map/Reduce应用或者网络爬虫应用都非常适合这个模型。目前还有计划在将来扩充这个模型，使之支持文件的附加写操作。

## Hadoop DataBase
![HBase架构1](http://img.blog.csdn.net/20170528230853515?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemdfaG92ZXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

参考资料：
- [Hbase原理、基本概念、基本架构](https://blog.csdn.net/woshiwanxin102213/article/details/17584043)
- [HBase笔记：存储结构](http://blog.javachen.com/2013/06/15/hbase-note-about-data-structure.html)

### 总结性介绍
- HBase是一个构建在HDFS上的分布式列存储系统，是基于Google BigTable模型开发的，典型的key/value系统。
- 与传统mysql、Oracle数据库的主要区别就是列式存储和夯实存储的区别。
- Hbase适合大量插入同时又有读的情况。输入一个Key获取一个value或输入一些key获得一些value。
- Hbase目标主要依靠横向扩展，通过不断增加廉价的商用服务器，来增加计算和存储能力。
- Hbase表的特点
    - 大：一个表可以有数十亿行，上百万列；
    - 无模式：每行都有一个可排序的主键和任意多的列，列可以根据需要动态的增加，同一张表中不同的行可以有截然不同的列；
    - 面向列：面向列（族）的存储和权限控制，列（族）独立检索；
    - 稀疏：空（null）列并不占用存储空间，表可以设计的非常稀疏；
    - 数据多版本：每个单元中的数据可以有多个版本，默认情况下版本号自动分配，是单元格插入时的时间戳；
    - 数据类型单一：Hbase中的数据都是字符串，没有类型。

### 存储结构

