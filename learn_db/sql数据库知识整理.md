---
title: 关系型数据库知识整理
categories: [关系型数据库, 数据库]
tags: [关系型数据库, 数据库, mysql]
---
# 关系型数据库知识整理

## 主键与外键
主键是能确定一条记录的唯一标识，比如，一条记录包括身份正号，姓名，年龄。身份证号是唯一能确定你这个人的，其他都可能有重复，所以，身份证号是主键。 

外键用于与另一张表的关联。是能确定另一张表记录的字段，用于保持数据的一致性。比如，A表中的一个字段，是B表的主键，那他就可以是A表的外键。

为什么用于保持数据一致性呢。举个例子：student包含id和name两列，id为主键；class包含id和name两列，id为主键；record包含sid，cid和record，sid和cid为主键。这样student中的id是record的外键，class中的id也是record中的外键。现在向record中插入一条数据，如果这条数据中的sid和cid在相应主键的表（也就是student和class）中不存在，那么无法插入。

示例代码：
```sql
-- create student table
create table student(stid int, stname varchar);
alter table student add primary key (stid);
-- create class table
create table class(clid int, clname varchar);
alter table class add primary key (clid);
-- create record table 
create table record(sstid int, cclid int, record int);
alter table record add FK_sstid foreign key(sstid) references student(stid);
alter table record add FK_cclid foreign key(cclid) references student(clid);
-- test
insert into record(sstid, cclid, record) values(1,1,100);
-- 结果为：
-- ERROR:  insert or update on table "record" violates foreign key constraint "fk_sstid"
-- DETAIL:  Key (sstid)=(1) is not present in table "student".
insert into student(stid, stname) values(1,'zhangsan');
insert into class(clid, clname) values(1,'yuwen');
insert into record(sstid, cclid, record) values(1,1,100);
select * from record;
-- 结果为：
--  sstid | cclid | record 
-- -------+-------+--------
--      1 |     1 |    100
-- (1 row)

```