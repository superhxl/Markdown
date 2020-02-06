# 主要内容

本课程的主要内容为

- Python进行数据控制、处理、整理、分析等方面的具体细节和基本要点，

- 利用Pyhton进行科学计算

- 用于高效解决各种数据分析问题的Python语言和库

  ## 结构化数据（Structured data）
  
- 数组、矩阵

- 表格型数据
  
- 通过关键列相互联系的多个表
  
- 间隔平均或不平均的时间序列


# Python语言介绍及其应用简介

## Python语言简介

Python是一种广泛使用的解释型、高级编程、通用型编程语言，由吉多·范罗苏姆创造，第一版发布于1991年。Python的设计哲学强调代码的可读性和简洁的语法（尤其是使用空格缩进划分代码块，而非使用大括号或者关键词）。相比于C++或Java，Python让开发者能够用更少的代码表达想法。不管是小型还是大型程序，该语言都试图让程序的结构清晰明了。

### Python的前世今生

Python的创始人: Guido van Rossum；之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是因为他是一个叫Monty Python的喜剧团体的爱好者。

![Guido van Rossum](https://i.loli.net/2020/01/31/DAykjNwJEQl8Sa1.png)

诞生于1989年。作者前身也是C++程序员，之前也参加设计了一种叫ABC的教学语言，就Guido本人看来，ABC 这种语言非常优美和强大，是专门为非专业程序员设计的。但是ABC语言并没有成功，究其原因，Guido 认为是其非开放造成的（相对封闭的开发语言、扩展性、推广性相对不太成功。）。Guido 决心在Python 中避免这一错误。同时，他还想实现在ABC 中闪现过但未曾实现的东西。

![Python的前世今生](https://i.loli.net/2020/01/31/g5CTQSNGKOsyhMp.png)

### 最流行的编程语言排行

Python有能运行的伪代码之称，是最适合初学者学习的语言。随着人工智能的爆发，所有人学习Python的热度与日俱增。编程语言在升学中的比重逐渐加大，将要成为高考提分的一大利器。

![热度排行](https://i.loli.net/2020/01/31/qYJwlMtCXcgWmKd.png)

- 浙江省信息技术课程改革方案出台，Python 确定进入浙江省信息技术高考，从2018年起浙江省信息技术教材编程语言将会从 VB 更换为Python。
- 山东省最新出版的小学信息技术六年级教材也加入了 Python 内容，**小学生都开始接触 Python 语言了**！！
- **2018年起，Python 列入全国计算机等级考试**

### Python编写的著名应用

- NASA：美国航天局(NASA)1994年起把python作为主要开发语言(使用Python进行数据分析和运算)
- Google：Google App Engine 、code.google.com 、Google earth 、谷歌爬虫、Google广告等项目都在大量使用Python开发
- Facebook：大量的基础库均通过Python实现的
- YouTube：世界上最大的视频网站YouTube就是用Python开发的
- Dropbox：美国最大的在线云存储网站，全部用Python实现，每天网站处理10亿个文件的上传和下载
- Instagram：美国最大的图片分享社交网站，每天超过3千万张照片被分享，全部用python开发
- 豆瓣：公司几乎所有的业务均是通过Python开发的
- 知乎：国内最大的问答社区，通过Python开发(国外Quora)

## Python语言特点

编程语言主要从以下几个角度为进行分类，编译型和解释型、静态语言和动态语言、强类型定义语言和弱类型定义语言。

### 解释型编程语言

CPU不能直接认识并执行我们写的语句,它只能认识机器语言(CPU指令集；二进制的形式)；因此我们开发语言的Virtual Machine要将识别的开发语言转换成机器语言让CPU去执行；那么就有两种以下两种方式:

1. **编译器**是把源程序的每一条语句都编译成机器语言,并保存成二进制文件,这样运行时计算机可以直接以机器语言来运行此程序,速度很快;
2. **解释器**则是只在执行程序时,才一条一条的解释成机器语言给计算机来执行,所以运行速度是不如编译后的程序运行的快的.

| 编译型 | 解释型      |
| ------ | ----------- |
| C/C++  | Java Script |
| Go     | Python      |
| C#     | Perl        |

### 动态类型语言

通常我们所说的动态语言、静态语言是指动态类型语言和静态类型语言。

1. **动态类型语言**：指在运行期间才去做数据类型检查的语言，也就是说，在用动态类型的语言编程时，永远也不用给任何变量指定数据类型，该语言会在你第一次赋值给变量时，在内部将数据类型记录下来。**Python是一种典型的动态类型语言**。
2. **静态类型语言**：与动态类型语言刚好相反，它的数据类型是在编译其间检查的，也就是说在写程序时要声明所有变量的数据类型，C/C++是静态类型语言的典型代表。

## What is Python

### Python哲学

> Python开发者的哲学是“用一种方法,最好是只有一种方法来做一件事”。在设计Python语言时,如果面临多种选择,Python开发者一般会拒绝花俏的语法,而选择明确没有或者很少有歧义的语法。这些准则被称为“Python格言”。在Python解释器内运行import this可以获得完整的列表。
>

- **优雅**：语法简短干练，没有多于的语法结构
- **明确**：对格式进行强制限制；格式整齐划一、优雅美丽
- **简单**：要实现任何一件事情，都应该有一种并且我们认为是最好的一种方式去实现。

### Python的优缺点

优点：

- 简单易学
- 开发效率高
- 可移植性
- 可扩展性
- 可嵌入性

缺点：

- 速度慢
- 代码不能加密
- 多线程问题

## Python应用场景及常用库

### Python应用场景

- Web开发
- GUI开发
- 操作系统
- 科学计算

### Python常用库

数据处理、分析和可视化已经成为Python近年来最重要的应用之一。

1. Numpy库

   NumPy 是 Numerical Python 的简称，是高性能计算和数据分析的基础包。其主要功能如下：

   - ndarray，快速和节省空间的多维数组，提供数组化的算术运算和高级的广播功能。
   - 使用标准数学函数对整个数组的数据进行快速运算，而不需要编写循环。
   - 读取/写入磁盘上的阵列数据和操作存储器映像文件的工具。
   - 线性代数，随机数生成，和傅里叶变换的能力。
   - 集成C，C++，Fortran代码的工具。

2. SciPy库

   SciPy是一种使用NumPy来做高等数学、信号处理、优化、统计和许多其它科学任务的语言扩展。SciPy是用子模块的形式来组织的，这些子模块涵括了不同科学计算领域的内容。右表对他们进行了总结。

   | 子模块      | 描述                   |
   | ----------- | ---------------------- |
   | constans    | 无理和数学常数         |
   | cluster     | 聚类算法               |
   | fftpack     | 快速傅立叶变换程序     |
   | integrate   | 积分和常微分方程求解器 |
   | interpolate | 拟合平滑曲线           |
   | io          | 输入和输出             |
   | linalg      | 线性代数               |
   | maxentropy  | 最大熵法               |
   | ndimage     | N维图像处理            |
   | odr         | 正交距离回归           |
   | optimize    | 优化模块               |
   | signal      | 信号处理               |
   | sparse      | 稀疏矩阵               |
   | spatial     | 空间                   |
   
3. Pandas库

   Pandas 是基于NumPy 的一种工具，该工具是为了**解决数据分析任务**而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法，它是使Python成为强大而高效的数据分析环境的重要因素之一。

4. Matplitlib库

   atplotlib 是 Python 的一个绘图库。它包含了大量的工具，你可以使用这些工具创建各种图形，包括简单的散点图，正弦曲线，甚至是三维图形。
   Python 科学计算社区经常使用它完成数据可视化的工作。

   <img src="https://i.loli.net/2020/02/05/YIfRqdQ7UANxHi2.png" alt="image-20200205093259691" style="zoom:80%;" /><img src="https://i.loli.net/2020/02/05/MeIsglv7ShGZ26i.png" style="zoom:80%;" />

   

   更多示例，请查看[Matplotlib图库](https://matplotlib.org/gallery.html)

5. 爬虫类

   - Requests: HTTP for humans，Python基于Apache2 Licensed许可证的人性化HTTP库
   - Beautiful Soup：Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据。
   - [爬虫做过有趣的事情](https://www.zhihu.com/question/27621722)

6. [Scikit-Learn](https://scikit-learn.org/)

   SciKit-Learn是开源的Python机器学习库，它基于Numpy、Scipy和matplotlib，提供了大量用于数据挖掘和分析的工具：分类，回归，聚类，数据降维，模型选择，数据预处理。

   ![](https://i.loli.net/2020/02/05/LxBGbF2oas9Rqtn.png)

7. [statsmodels库](https://www.statsmodels.org/stable/index.html)

   is a Python module that provides classes and functions for the estimation of many different statistical models, as well as for conducting statistical tests, and statistical data exploration. 

8. [更多Python库](https://github.com/vinta/awesome-python)

   中文版地址：[https://github.com/jobbole/awesome-python-cn](https://github.com/jobbole/awesome-python-cn)

   ![](https://i.loli.net/2020/02/05/TQCjMgcPykeYVB7.png)

# 如何学习Python

## Python安装

此处介绍两种安装python的方式，一种是基本安装，即安装python的基本库，需要第三方库是根据需要安装；第二种方式是集成式一站安装，把常用的python库和工具都安装好。

### 基本安装

1. [Python官网](  https://www.python.org/)下载安装程序，选择合适版本进行安装。    安装完成后，此时python只有自带基本库，还需安装第三方库。  ![](https://i.loli.net/2020/02/05/Zc8gGrF4HKQjBoe.png)

2. 安装第三方库，譬如numpy、pandas等。可以在控制台窗口下通过`pip install package`命令进行安装。

   ```bash
   pip install numpy
   pip install pandas
   ```

   pip是python自带的包管理工具，如果你的python没有pip命令，则需安装：从[get-pip.py](https://bootstrap.pypa.io/get-pip.py)下载*get-pip.py*，在命令窗口下运行：

   ```bash
   python get-pip.py
   ```

### 集成环境安装

集成式安装我们采用Anaconda（自称为Solutions for Data Science Practitioners and Enterprise Machine Learning），在其官方[下载地址](https://www.anaconda.com/distribution/)下载合适版本进行安装。

![](https://i.loli.net/2020/02/05/boO3GT64v2p1eNR.png)

## 工具

Python语言支持交互式和常用的Python工具有：

- Ipython：增强型Python shell，支持自动补全

- Jupyter-notebook：可理解为基于浏览器的Ipython，本课程主要采用的工具。Google chrome浏览器支持较好。

- Spyder：Anaconda孪生兄弟，集成编辑器和IPython

  ![](https://i.loli.net/2020/02/05/VwnQiml63IuBrFq.png)

- [Pycharm](https://www.jetbrains.com/pycharm/)专业的集成开发环境，分专业版和社区版以及教育版(ree for students: Professional developer tools from JetBrains，需要edu邮箱)

  ![](https://i.loli.net/2020/02/05/JvU5se7DtFgSLHT.png)

- VsCode：Microsoft在2015年4月30日Build 开发者大会上正式宣布的项目：一个运行于 Mac OS X、Windows和 Linux 之上的，针对于编写现代 Web 和云应用的跨平台源代码编辑器，安装Python扩展后支持Python开发。新版支持jupyter-noebook：![](https://i.loli.net/2020/02/05/EvWoDjZVYwA1syU.png)

  本课程推荐使用欧冠Jupyter-notebook和spyder，有能力的同学可以探索其他工具。

## 学习资源

### 教材

- Python编程从入门到实践，作者:[美]埃里克·马瑟斯（Eric Matthes）出版社:人民邮电出版社出版时间:2016年07月 

- 利用Python进行数据分析，作者:  Wes McKinney 出版社: 机械工业出版社，原作名: Python for Data Analysis 译者: 唐学韬 

- 机器学习实战，作者：Peter Harrignton，人民邮电出版社 Machine Learning in Action，译者：李锐、李鹏等

  ![](https://i.loli.net/2020/02/05/1glBwJp9or5zDZx.png)![](https://i.loli.net/2020/02/05/VnUDxjcIiFQE7Ak.png)![](https://i.loli.net/2020/02/05/LJ7Hd9EhMzfwrTY.png)

### 网络资源

- [www.brucehan.top](https://brucehan.top)
- [Python for Data Analysis, 2nd Edition on Github](https://github.com/wesm/pydata-book)
- Google(Baidu)

### Suggestions

- Coding more， learn more
- 阅读别人的代码
- 兴趣是最好的老师

### 计划

根据进度可能会适当增删

1. Python入门，6课时
2. NumPy基础，4课时
3. Pandas入门，4课时
4. Padas数据规整化：清理、转换、合并，6课时
5. 绘图和可视化，4课时
6. 数据聚合与分组运算，4课时
7. 时间序列，4课时

# 参考：

1. BruceLiu1，[Python简介和入门](https://www.jianshu.com/p/56ac30b842ef)，简书，

