-------------------------------
    OSM 学习笔记
    @author： 陈凯恒
    @createtime： 2017-12-29
-------------------------------

# OSM 学习笔记
## 什么是OSM?
    开放街道地图（OpenStreetMap，简称OSM）是一个网上地图协作计划，目标是创造一个内容自由且能让所有人编辑的世界地图[wiki：http://wiki.openstreetmap.org/wiki/Main_Page].尤其值得称道的是，osm数据开源，可以自由下载使用。

## 如何使用OSM?
### 获取地图数据
多种方式
### 地图数据解释
地图数据导入pg数据库，使用osm2pgsql（apt-get intall osm2pgsql）导入，命令类似于
```shell
osm2pgsql -s -U postgres -d osm /tmp/map.xml -H 192.168.6.133 -W。
```
**注**：osm2pgsql导入数据有两种模式， normal and slim mode。
- normal mode会在内存中产生如下三张中间表，并在导入结束后丢弃，因此速度较快。  
planet_osm_nodes  
planet_osm_ways  
planet_osm_rels

- 而slim mode则将中间结果完全放置到数据库中。slim模式的好处是方便更新。

两者使用的区别在于是否加“-s”，加了表示slim mode，本文使用slim mode。
使用slim mode导入数据后在数据库中会产生如下表。
        
## 参考资料
[OSM入门+搭建地图服务](http://www.cnblogs.com/LBSer/p/4451471.html) //讲的很详细，值得参考一看