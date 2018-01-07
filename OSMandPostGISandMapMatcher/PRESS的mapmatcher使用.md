# PRESS系统使用的地图匹配程序MapMathcer使用说明

## 程序地址与说明
- PRESS系统有自己的Github仓库，地址：https://github.com/RenchuSong/PRESS
- MapMatcher使用的算法提交到了ACM SIGSPATIAL Cup 2012，获得了很好的成绩。程序源码没有公开。算法提出的论文应该是[Quick Map Matching Using Multi-Core CPUs](https://dl.acm.org/citation.cfm?doid=2424321.2424428)，文中提到传统的基于HMM的算法等已经有了**较高的匹配准确率**（论文中的误匹配率平均在1.6-2.0%），所以主要目标考虑如何**减少运行时间，加快匹配速度**。所以这个方法有两点贡献：
    1. **多线程**匹配技术：路段可以多线程索引，轨迹匹配可以多线程进行（竟然不是废话）
    2. **改进HMM算法**：主要添加了路段速度约束，避免在主干道上运行匹配到辅路上的问题。

## 程序使用说明
地图数据从OpenStreetMap获得，对华盛顿的数据来说，分成了三个文件

**WA_Nodes.txt**

该文本文件包含道路网络的节点。该文件定义了1283540个边，每行代表一个边。每行包含四个值，每个值由一个空格分隔。边缘行的形式是：
`<NodeId> <lat> <long>`
- `<NodeId>`：一个整数值，指定道路网络内节点的唯一标识号码。
- `<lat>`：该值以度为单位指定路网内节点的纬度位置。
- `<long>`：该值以度为单位指定道路网络内节点的经度位置。

**WA_Edges.txt**

这个文本文件包含道路网络的边结构。该文件定义了1283540个边，每行代表一个
单边。每行包含四个值，每个值由一个空格分隔。边缘行的形式是：
`<EdgeId> <from> <to> <cost>`

- `<EdgeId>`：整数值，指定道路网络内边缘的唯一标识号码。
- `<from>`：该值表示位于边缘的节点的id。如果边被定义为(v, w)，则`<from>`是v， 节点ID值对应于WA_Nodes.txt中的<NodeId>值。
- `<to>`：该值表示边缘尾部的节点的id。如果边被定义为(v, w)，则`<to>`是w。这些节点
id值对应于WA_Nodes.txt中的<NodeId>值。
- `<cost>`：该值定义车辆从边缘一端到另一端的实际成本。这是一个成本基于边的长度和边表示的路段上的速度限制的函数。请注意，道路网络图是一个有向图。从节点v到节点w的边有不同的`<EdgeId>`
沿着另一个方向（从节点w到节点v）的边。请确保您的算法与GPS读数匹配沿着正确的方向前进。

**WA_EdgeGeometry.txt**

该文本文件包含道路网络中每条边的几何数据(geometry data)。边缘几何形状定义边缘所代表的实际道路的多段线。该文件包含1,283,540个条目，每个网络边缘一个，每个条目在一行中。每行至少包含八个值，每个值由一个^符号分隔。每通过指定点的纬度和经度值，沿边缘定义了n个不同的点。边缘几何行的形式为：`<EdgeId> ^ <Name> ^ <Type> ^ <Length> ^ <Lat_1> ^ <Lon_1> ^ ... ^ <Lat_n> ^ <Lon_n>`

- `<EdgeId>`：整数值，指定道路网络中边缘的唯一标识号码。这个值会匹配WA_Edges.txt文件中定义的单个边。  
- `<name>`：该值描述了该特定边所代表的路段的实际名称。如果没有定义名字，属性将包含一个空字符串。
- `<type>`：该值描述了由边表示的道路的类型。一些常见的值是：
    ```
    motorway: motorway_link
    primary: primary_link
    secondary: secondary_link
    tertiary: residential
    living_street: service
    trunk: trunk_link
    unclassified
    ```
- `<Length>`：该值是边缘的长度（以米为单位）。
- `<Lat_1>`：该值是边缘第一个点的纬度。如果边缘被定义为(v, w)，那么<Lat_1>是纬度值
- `<Lon_1>`：这个值是边的第一个点的经度。如果边缘被定义为(v, w)，则<Lon_1>是经度值
- `<Lat_i> <Lon_i>`：边缘的第一点和最后点之间的若干点的纬度和经度值。这些点是可选的，并且可选点的数量根据所表示的边的几何形状而变化。
- `<Lat_n>`：该值是边缘最后一点的纬度。如果边缘被定义为(v, w)，那么<Lat_n>是纬度值w。
- `<Lon_n>`：该值是边缘最后一点的经度。如果边缘被定义为(v, w)，则<Lon_n>是经度值v。

## 程序执行顺序

mapmatch.exe接受三个命令行参数。 mapmatch.exe程序的用法如下：

    mapmatch  RoadNetworkInfo_Path] [Input_Path] [Output_Path]

- `RoadNetworkInfo_Path`：指定包含三个文本文件（WA_Nodes.txt，WA_Edges.txt和WA_EdgeGeometry.txt）的目录。

- `Input_Path`：指定包含n个文本文件的目录。每个文件都是单个测试用例，并包含一系列记录
在美国华盛顿州记录的GPS读数。文件被命名为：`input_01.txt`到`input_n.txt`，其中`input_i.txt`
是包含第i个测试用例的文件。输入测试案例的例子可以在训练数据集部分找到。

- `Output_Path`：指定程序预期放置输出文件的目录。对于每个输入文件 `input_i.txt`，mapmatch.exe 程序必须生成一个名为`output_i.txt`的相应输出文件。输出文件的例子可以也可以在训练数据集部分找到。

请注意，输出文件`output_i.txt`中的行数必须与输入文件`inut_i.txt`相同。这是为了每一个在输入文件中有一行，在输出文件中存在一个具有相同`<Time>`值的行，并指示GPS点匹配的`<EdgeId>`。此外，`<EdgeId>`必须用置信度值注释。 请注意，所有测试案例都包含使用GPS记录器以可变采样率记录的真实世界GPS数据。 采样率在1秒到30秒之间变化。 这个可变采样率旨在测试稀疏GPS跟踪下提交的地图匹配算法的弹性。

## 注意
的程序只能处理不超过10000个点的轨迹。 如果时间较长，请把轨迹进行切分。