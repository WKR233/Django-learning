# tutorial 1
urls.py定义了当遇到某一个url时，该如何处理
一般用urlpattern的list进行自定义
urlpattern里面的元素用path()来获得
path(route,view,kwargs=None,name=None)
- route是匹配的url形式，以字符串形式出现
- view为对应的函数，如views.index就是指的views.py中的index函数（在urls.py中import过，如from . import views）
- kwargs为附加的参数，它必须是字典类型，例如path("blog/<int:year>/",views.year_archive,{"foo": "bar"})，它在面对"/blog/2005"的时候就会调用views.year_archive(request（默认的参数）,year=2005（通过转换器捕捉到的int参数）,foo='bar'（对应的字典）)
- name为url模式命名，能让我们在任意地方唯一地引用它。
include()的使用：函数 include() 允许引用其它 URLconfs。每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。
例如path("polls/",include("polls.urls"))，它遇到一个url为"/polls/blog/2005/"时，首先会匹配"/polls/"，然后将其截断，把"blog/2005/"发送给polls里的urls.py文件，再由这一文件进一步处理

处理逻辑：运行>py manager.py runserver->默认监听localhost的8000端口->接收"https://localhost:8000/polls/2005"->对url进行解析->在mysite.url中匹配->include将其截断，剩下部分在polls.url中匹配->解析出2005这一参数，并调用polls.view.index函数->将网页展现在浏览器中