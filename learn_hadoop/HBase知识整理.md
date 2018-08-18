---
title: HBase面试整理
categories: [分布式系统, HBase]
tags: [分布式系统, HBase, 面试]
---
# HBase面试整理
<!-- TOC -->

- [HBase面试整理](#hbase)
    - [1. 总结性介绍](#1)
    - [2. 存储形式-表结构](#2)
    - [3. 存储结构-HRegion, HStore, HFile](#3--hregion--hstore--hfile)
    - [4. region 定位问题](#4-region)
        - [4.1. -ROOT- 和 .META. 怎么来的](#41--root---meta)
        - [4.2. -ROOT- 和 .META. 的存储结构](#42--root---meta)
    - [5. 一致性问题：HBase的读写一致性是怎么保证的？做到了什么程度？](#5-hbase)

<!-- /TOC -->
参考资料：
- [列式存储hbase系统架构学习](http://www.ixirong.com/2015/07/16/learn-about-hbase/)
- [HBase笔记：存储结构](http://blog.javachen.com/2013/06/15/hbase-note-about-data-structure.html)
- [HBase region查找过程](https://blog.csdn.net/qq_26222859/article/details/80257298)
## 1. 总结性介绍
- HBase是一个构建在HDFS上的分布式列存储系统，是基于Google BigTable模型开发的，典型的key/value系统。
- 与传统mysql、Oracle数据库的主要区别就是列式存储和行式存储的区别。
- Hbase适合大量插入同时又有读的情况。输入一个Key获取一个value或输入一些key获得一些value。
- Hbase目标主要依靠横向扩展，通过不断增加廉价的商用服务器，来增加计算和存储能力。
- Hbase表的特点
    - 大：一个表可以有数十亿行，上百万列；
    - 无模式：每行都有一个可排序的主键和任意多的列，列可以根据需要动态的增加，同一张表中不同的行可以有截然不同的列；
    - 面向列：面向列（族）的存储和权限控制，列（族）独立检索；
    - 稀疏：空（null）列并不占用存储空间，表可以设计的非常稀疏；
    - 数据多版本：每个单元中的数据可以有多个版本，默认情况下版本号自动分配，是单元格插入时的时间戳；
    - 数据类型单一：Hbase中的数据都是字符串，没有类型。

## 2. 存储形式-表结构
- table:
- rowkey
- column family
- column

## 3. 存储结构-HRegion, HStore, HFile
![HBase架构1](hbase_structure.png)

Zookeeper：
- 保证任何时候，集群中只有一个master
- 存贮所有Region的寻址入口。
- 实时监控Region Server的状态，将Region server的上线和下线信息实时通知给Master
- 存储Hbase的schema,包括有哪些table，每个table有哪些column family

HMaster: 
- 为Region server分配region，负责region server的负载均衡
- 管理用户对Table的增、删、改、查操作
- 发现失效的region server并重新分配其上的region
- GFS上的垃圾文件回收
- 在HRegionServer停机后，负责失效HRegionServer 上的Regions迁移
> client访问Hbase上数据的过程并不需要master参与(寻址访问zookeeper和region server，数据读写访问regione server)，master仅仅维护着**table**和**region**的元数据信息，负载很低。

HRegion Server
- Region server维护Master分配给它的region，处理对这些region的IO请求
- Region server负责切分在运行过程中变得过大的region


## 4. region 定位问题
### 4.1. -ROOT- 和 .META. 怎么来的
如果要insert一个数据，需要找到相应的Region，如何找呢？就需要一个所有region的meta信息，但是region可能很多，那就分级来搞，先有一个-ROOT-索引.META.的内容，.META.再索引Region的内容。不需要再多级别了，因为这两个级别就可以存储2^34个region了，足够使用，再多了反而增加复杂度和网络开销。

### 4.2. -ROOT- 和 .META. 的存储结构
可以视为一般的region，存储形式都是相同的。只不过rowkey不太一样。

## 5. 一致性问题：HBase的读写一致性是怎么保证的？做到了什么程度？
参考：
- [HBase-强一致性详解](https://www.cnblogs.com/captainlucky/p/4720986.html)
- [LSM 算法的原理是什么？](http://www.open-open.com/lib/view/open1424916275249.html)

> 从一开始就知道hbase是CAP中的CP系统,即hbase是强一致性的.我原来一直以为hbase的强一致性是因为底层的HDFS写入时,必须所有副本都写入成功才能返回.最近才想明白,hbase之所以是CP系统,实际和底层HDFS无关,它是CP系统,是因为对每一个region同时只有一台region server为它服务,对一个region所有的操作请求,都由这一台region server来响应,自然是强一致性的.在这台region server fail的时候,它管理的region failover到其他region server时,需要根据WAL log来redo,这时候进行redo的region应该是unavailable的,所以hbase降低了可用性,提高了一致性.设想一下,如果redo的region能够响应请求,那么可用性提高了,则必然返回不一致的数据(因为redo可能还没完成),那么hbase就降低一致性来提高可用性了.