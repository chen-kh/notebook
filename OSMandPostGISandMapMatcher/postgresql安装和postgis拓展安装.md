<link rel="stylesheet" type="text/css" href="auto-number-title.css" />

-------------------------------
    PostGIS 学习笔记
    @author： 陈凯恒
    @createtime： 2017-12-29
-------------------------------
# PostGIS 学习笔记
## postgresql安装
安装过程参见[博客](http://www.cnblogs.com/z-sm/archive/2016/07/05/5644165.html),其中涉及到的主要问题： 
- postgresql的版本选择问题
- postgresql安装之后修改配置、添加用户、添加用户权限更改等等问题

## postgis扩展安装
### 安装过程参见[博客](https://www.howtoing.com/how-to-install-and-configure-postgis-on-ubuntu-14-04)  
**注意**：很多博客中的安装过程只需要 `apt-get install postgis`，实际测试发现 `apt-get install postgis*` 最好。第一种安装方式可能没有postgis-scripts，导致在数据库中`create extension`执行时出现*[ERROR: could not open extension control file "/usr/share/postgresql/9.3/extension/ postgis.control": No such file or directory]*的错误。  
### PostGIS使用
创建扩展：postgis安装后在使用时，需要在使用的数据库中添加拓展，在相应数据库执行
```sql
create extension postgis
```
出现`CREAT EXTENSION`表示安装成功，可使用一下命令查看版本。
```sql
select PostGIS_version()
```
### 具体使用见[博客](https://www.howtoing.com/how-to-install-and-configure-postgis-on-ubuntu-14-04)