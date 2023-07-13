# tutorial 1
**urls.py定义了当遇到某一个url时，该如何处理**
一般用urlpattern的list进行自定义
urlpattern里面的元素用path()来获得
`path(route,view,kwargs=None,name=None)`
- `route`是匹配的url形式，以字符串形式出现
- `view`为对应的函数，如`views.index`就是指的views.py中的`index`函数（在urls.py中import过，如`from . import views`）
- `kwargs`为附加的参数，它必须是字典类型，例如`path("blog/<int:year>/",views.year_archive,{"foo": "bar"})`，它在面对"/blog/2005"的时候就会调用`views.year_archive(request（默认的参数）,year=2005（通过转换器捕捉到的int参数）,foo='bar'（对应的字典）)`
- `name`为url模式命名，能让我们在任意地方唯一地引用它。
`include()`的使用：函数`include()`允许引用其它 URLconfs。每当 Django 遇到`include()`时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。
例如`path("polls/",include("polls.urls"))`，它遇到一个url为"/polls/blog/2005/"时，首先会匹配"/polls/"，然后将其截断，把"blog/2005/"发送给polls里的urls.py文件，再由这一文件进一步处理

处理逻辑：运行`>py manager.py runserver`->默认监听localhost的8000端口->接收"https://localhost:8000/polls/2005"->对url进行解析->在mysite.url中匹配->include将其截断，剩下部分在polls.url中匹配->解析出2005这一参数，并调用`polls.view.index`函数->将网页展现在浏览器中

# tutorial 2
在setting中更改DATABASE可以改变默认的数据库（SQLite）
可以更改`ENGINE`和`NAME`来确定可用后端已经数据库名称
设置`TIME_ZONE`可以改变对应时区，默认为`UTC`
文件头部的`INSTALLED_APPS`包括了会启用的Django应用
创建一个数据表：
`...\>py manage.py migrate`
`migrate`指令查看`INSTALLED_APPS`并根据setting.py中的数据库配置创建必要的数据库表

模型，即数据库结构设计和附加的其他元数据
此处创造了两个模型：问题`Question`和选项`Choice`->编辑models.py文件

Django 应用是可插拔的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，因为它们并不会被绑定到当前安装的 Django 上。

应用会写到apps.py中，我们需要在settings.py中的`INSTALLED_APPS`中添加对应的点式路径，在修改之后我们还要运行`>py manage.py makemigrations polls`，即提交我们的修改，并将我们的修改储存为一次迁移（在`/polls/migrations/`中可以看到迁移文件）。生成了迁移文件后再运行`>py manage.py migrate`应用数据库迁移。

**改变模型的三步：编辑models.py->运行`py manage.py makemigrations`命令生成迁移文件->运行`py manage.py migrate`命令来应用迁移**
## learning of MySQL
> 参考资料 https://www.runoob.com/mysql/mysql-tutorial.html
### 基本定义
数据库 Database 就是按照数据结构来组织、存储、管理数据的仓库
可以创建、访问、管理、搜索和复制
关系型数据库管理系统 RDBMS (Relational Database Management System)：数据以**表格**的形式出现，若干表单组成**database**

### RDBMS术语
- 列：同类型数据
- 行：一组相关数据
- 键：键的值在当前列中具有唯一性（用于标记不同行）
- 主键：一个数据表中唯一的
- 外键：用于关联两个表格
- 索引：根据一列/多列的值进行排序的结构（目录）
- 复合键：将多个列作为一个索引键，用于复合索引

### 基本操作
> 参考资料 https://github.com/jaywcjlove/mysql-tutorial/blob/master/docs/21-minutes-MySQL-basic-entry.md
- 登录MySQL
- 创建数据库
- 创建数据库表
- 删除数据库表
- 增删改查
- AND,OR和NOT
- ORDER BY
- GROUP BY
- IN
- UNION
- BETWEEN
- AS
- JOIN
- SQL函数
- 触发器
- 添加索引
- 创建后表的修改

# tutorial 3