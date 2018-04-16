---
title: PostGIS 学习笔记
categories: [postgres]
tags: [postgres, postgis]
---
# postgresql和postgis拓展

<!-- TOC -->

- [1. postgresql安装](#1-postgresql安装)
- [2. postgresql使用](#2-postgresql使用)
- [3. postgis扩展安装](#3-postgis扩展安装)
    - [3.1. ubuntu 安装](#31-ubuntu-安装)
    - [3.2. centos 7 安装](#32-centos-7-安装)
    - [3.3. 创建扩展](#33-创建扩展)
- [4. 什么是 PostGIS](#4-什么是-postgis)
- [5. 如何使用 PostGIS](#5-如何使用-postgis)
    - [5.1. 简单示例](#51-简单示例)
    - [5.2. PostGIS的Geometry数据类型](#52-postgis的geometry数据类型)
    - [5.3. PostGIS函数的分类](#53-postgis函数的分类)
        - [5.3.1. 字段处理函数](#531-字段处理函数)
        - [5.3.2. 几何关系函数](#532-几何关系函数)
        - [5.3.3. 几何分析函数](#533-几何分析函数)
        - [5.3.4. 读写函数](#534-读写函数)
    - [5.4. 使用PostGIS扩展函数](#54-使用postgis扩展函数)
        - [5.4.1. 管理类函数](#541-管理类函数)
        - [5.4.2. 数据类型的输入输出函数](#542-数据类型的输入输出函数)
        - [5.4.3. 量算函数](#543-量算函数)
        - [5.4.4. 几何操作函数](#544-几何操作函数)
        - [5.4.5. PostGIS函数使用示例](#545-postgis函数使用示例)
    - [5.5. 建立PostGIS索引](#55-建立postgis索引)
- [6. 参考资料](#6-参考资料)

<!-- /TOC -->
## 1. postgresql安装
安装过程参见[博客](http://www.cnblogs.com/z-sm/archive/2016/07/05/5644165.html),其中涉及到的主要问题： 
- postgresql的版本选择问题
- postgresql安装之后修改配置、添加用户、添加用户权限更改等等问题

## 2. postgresql使用

## 3. postgis扩展安装

### 3.1. ubuntu 安装
参考：[博客](https://www.howtoing.com/how-to-install-and-configure-postgis-on-ubuntu-14-04)  

**注意**：很多博客中的安装过程只需要 `apt-get install postgis`，实际测试发现 `apt-get install postgis*` 最好。第一种安装方式可能没有postgis-scripts，导致在数据库中`create extension`执行时出现*[ERROR: could not open extension control file "/usr/share/postgresql/9.3/extension/ postgis.control": No such file or directory]*的错误。  

### 3.2. centos 7 安装
参考博客：[CentOS 7 源码安装PostGIS](https://my.oschina.net/freegis/blog/781657)：文章写得算是很不错了，只是需要注意一下postgres这个目录，有的时候指的是你自己的postgres的安装目录。

### 3.3. 创建扩展
创建扩展：postgis安装后在使用时，需要在使用的数据库中添加拓展，在相应数据库执行
```sql
create extension postgis
```
出现`CREAT EXTENSION`表示安装成功，可使用一下命令查看版本。
```sql
select PostGIS_version()
```
- 具体使用见[博客](https://www.howtoing.com/how-to-install-and-configure-postgis-on-ubuntu-14-04)

## 4. 什么是 PostGIS
参考：[PostGIS官网](https://postgis.net/)  
**Wiki定义**：  
PostGIS 是一个开源程序，它为对象－关系型数据库PostgreSQL提供了存储空间地理数据的支持，使PostgreSQL成为了一个空间数据库，能够进行空间数据管理、数量测量与几何拓扑分析。PostGIS 实现了Open Geospatial Consortium所提出的基本要素类（点、线、面、多点、多线、多面等）的SQL实现参考。

## 5. 如何使用 PostGIS
### 5.1. 简单示例
```sql
CREATE DATABASE demo TEMPLATE=template_postgis;
CREATE TABLE cities ( id int4, name varchar(50) );
select AddGeometryColumn('cities','the_geom',-1,'GEOMETRY',2);
/* SELECT * from cities; */
INSERT INTO cities (id, the_geom, name) VALUES (1,ST_GeomFromText('POINT(-0.1257 51.508)',4326),'London, England');
INSERT INTO cities (id, the_geom, name) VALUES (2,ST_GeomFromText('POINT(-81.233 42.983)',4326),'London, Ontario');
INSERT INTO cities (id, the_geom, name) VALUES (3,ST_GeomFromText('POINT(27.91162491 -33.01529)',4326),'East London,SA');
/* 简单查询 */
SELECT * FROM cities;
```
结果显示为下表:
        
        id |      name       |                      the_geom
        ----+-----------------+----------------------------------------------------
        1 | London, England | 0101000020E6100000BBB88D06F016C0BF1B2FDD2406C14940
        2 | London, Ontario | 0101000020E6100000F4FDD478E94E54C0E7FBA9F1D27D4540
        3 | East London,SA  | 0101000020E610000040AB064060E93B4059FAD005F58140C0
        (3 rows)
```sql
SELECT id, ST_AsText(the_geom), ST_AsEwkt(the_geom), ST_X(the_geom), ST_Y(the_geom) FROM cities;
```
结果显示为下表:

        id |          st_astext           |               st_asewkt                |    st_x     |   st_y
        ----+------------------------------+----------------------------------------+-------------+-----------
        1 | POINT(-0.1257 51.508)        | SRID=4326;POINT(-0.1257 51.508)        |     -0.1257 |    51.508
        2 | POINT(-81.233 42.983)        | SRID=4326;POINT(-81.233 42.983)        |     -81.233 |    42.983
        3 | POINT(27.91162491 -33.01529) | SRID=4326;POINT(27.91162491 -33.01529) | 27.91162491 | -33.01529
```sql
/*空间查询*/
SELECT p1.name,p2.name,ST_Distance_Sphere(p1.the_geom,p2.the_geom) FROM cities AS p1, cities AS p2 WHERE p1.id > p2.id;
```
            name       |      name       | st_distance_sphere
        -----------------+-----------------+--------------------
        London, Ontario | London, England |   5875766.85191657
        East London,SA  | London, England |   9789646.96784908
        East London,SA  | London, Ontario |   13892160.9525778
        (3 rows)

### 5.2. PostGIS的Geometry数据类型
Geometry可以说是PostGIS最重要的一个概念，是“几何体”的意思，由于PostGIS很好地遵守OGC的”Simple Feature for Specification for SQL”规范，目前支持的几何体类型包含其实例有：
```
POINT(1 1)
MULTIPOINT(1 1, 3 4, -1 3)
LINESTRING(1 1, 2 2, 3 4)
POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))
MULTIPOLYGON((0 0, 0 1, 1 1, 1 0, 0 0), (5 5, 5 6, 6 6, 6 5, 5 5))
MULTILINESTRING((1 1, 2 2, 3 4),(2 2, 3 3, 4 5))
```
而geometry具体表现又有两种形式，一种叫做WKT(Well Known Text)形式，如上面的例子。或者使用如下SQL语句浏览：
```sql
select AsText(pt) from test1;
select AddGeometryColumn('test1','pt',-1,'GEOMETRY',2);
```
另一种叫做“Canonical Form”形式，看上去是一串古怪的数字，其实是一种增强的十六进制编码，使用如下SQL语句就可以浏览了：
```sql
select pt from test1;
```

### 5.3. PostGIS函数的分类
PostGIS函数大致可以分为以下四类:
#### 5.3.1. 字段处理函数
这类函数当前一共有3个，分别是：
- `AddGeometryColumn(var1,var2,var3,var4,var5,var6)`：  
为已有的数据表增加一个地理几何数据字段。Var1代表数据表的模式(schema)的名字，一般是public，也可以省略，则使用当前的缺省模式；var2是已有的数据表的名字；var3是新的地理数据字段的名字；var4是SRID值，不确定的话就取-1吧；var5是地理数据的类型，可以是POINT等；var6是指该几何数据是二维还是三维数据。  
前面的SQL语句`create table test1 (myID int4, pt geometry, myName varchar)`更规范的写法为：
    ```sql
    create table test1 (myID int4, myName varchar );
    select AddGeometryColumn('test1','pt',-1,'GEOMETRY',2);
    ```
- `DropGeometryColumn` 函数：  
显然是删除一个地理数据字段的；
- `SetSRID` 函数：  
显然是设置SRID值的。
#### 5.3.2. 几何关系函数
这类函数目前共有10个，分别是：  
`Distance Equals Disjoint Intersects Touches Crosses Within Overlaps Contains Relate`
#### 5.3.3. 几何分析函数
这类函数目前共有12个，分别是：  
`Centroid Area Lenth PointOnSurface Boundary Buffer ConvexHull Intersection SymDifference Difference GeomUnion MemGeomUnion`
#### 5.3.4. 读写函数
这类函数很多，主要是用于在各种数据类型之间的转换，尤其是在于Geometry数据类型与其他如字符型等数据类型之间的转换，函数名如`AsText、GeomFromText`等，其作用是显然的。
### 5.4. 使用PostGIS扩展函数
除了上述遵循OpenGIS的函数之外，PostGIS还自行扩展了一些当前OpenGIS规范之外的函数，主要包括以下几类：
#### 5.4.1. 管理类函数
扩展的管理类函数主要包括一些软件版本查询函数，如postgis_version()、postgis_geos_version()、postgis_proj_version()函数等，分别查询当前的PostGIS的版本及其使用的Geos和Proj库的版本。
#### 5.4.2. 数据类型的输入输出函数
除了OpenGIS定义的地理数据类型之外，PostGIS还对数据类型进行了扩展，这种扩展主要是两方面的扩展，一是把二维的数据向三维和四维扩展；二就是在WKT和WKB数据类型基础上扩展出EWKT和EWKB数据类型。PostGIS提供了在这些地理数据类型和常用数据类型如字符型、浮点型数据之间进行转换的函数。
#### 5.4.3. 量算函数
如length3d函数是对length2d函数的扩展。
#### 5.4.4. 几何操作函数
如addBBox(geometry)函数给所给的几何体加上一个边框。如simplify(geometry,tolerance)函数可以对折线和多边形利用Douglas-Peuker算法进行一些节点进行删除，从而使表现的图形更简单而清晰，在网络传输数据时具有更高的效率。
#### 5.4.5. PostGIS函数使用示例
- integer ST_NPoints(geometry g1); 返回geometry中包含多少个point
    ```sql
    SELECT ST_NPoints(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
    --result: 4
    ```
- geometry ST_PointN(geometry a_linestring, integer n); 返回linestring中的第n个point
    ```sql
    SELECT ST_AsText(ST_PointN(ST_GeomFromText('CIRCULARSTRING(1 2, 3 2, 1 2)'),2));
    --result:POINT(3 2)
    ```
### 5.5. 建立PostGIS索引
当数据库的记录增大的时候，如果没有建立索引的话，操作的效率就显著下降。POstGIS建议当记录数超过几千的时候就应该建立索引，而GIS数据库一般都是海量数据，所以对PostGIS而言，索引就非常重要。 


## 6. 参考资料
- [PostGIS维基百科介绍](https://zh.wikipedia.org/wiki/PostGIS)  
- [PostGIS快速入门](https://live.osgeo.org/zh/quickstart/postgis_quickstart.html)  
- [PostGIS简介](http://blog.csdn.net/shixiaoguo90/article/details/30034429)  
- [PostGIS管理函数](http://www.cnblogs.com/LCGIS/archive/2013/03/08/2949119.html)