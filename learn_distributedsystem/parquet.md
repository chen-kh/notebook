# parquet

## dremel data model

### repetition and definition level
根据论文解释，repetition level和definition level分别被定义为
- repetition level:『at what repeated field in the field’s path the value has repeated.』该字段在他的路径里的哪个level重复了。
- definition level:『how many fields in p that could be undefined (because they are optional or repeated) are actually present』该字段的路径p里面有多少个字段是optional或者是repeated的。

[Google Dremel数据模型详解(上)](https://blog.csdn.net/dc_726/article/details/41627613)上面有很清晰明了的图形+文字解释。

## 参考资料
- [深入分析Parquet列式存储格式](https://my.oschina.net/u/2306127/blog/665432)
- [Google Dremel数据模型详解(上)](https://blog.csdn.net/dc_726/article/details/41627613)
- [Google Dremel数据模型详解(下)](https://blog.csdn.net/dc_726/article/details/41777619)