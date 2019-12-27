# 虚拟茶话会

**电子信息与通信学院**

## 一、概述

### 1、背景分析

虚拟茶话会实际上是一个在线聊天室，它是一个古老而又现代的东西。从互联网初期星期的各种叫交友聊天室，到各种即时通讯应用，再到现在功能丰富的团队协作聊天工具，这些都可以算作是聊天室，这次我将实现一个功能较为简单的聊天室。

### 2、技术背景

整体技术栈采用了：

#### 1）Flask框架

Flask是一个使用Python编写的轻量级的Web应用框架，基于Werkzeug WSGI工具箱和jinja2模版引擎。Flask使用BSD授权。Flask被称为“microframework”，是因为它使用简单的核心，用extension增加其他功能。Flask没有预设使用的资料库，表单验证工具，然而Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、表单验证工具、档案上传、各种开放式身份验证技术。

#### 2）websocket

websocket为一次HTTP握手后，后续通讯为tcp协议的通讯方式。

WebSocket 使用一种被称作**“Upgrade handshake（升级握手）”的机制将标准的 HTTP 或HTTPS 协议转为 WebSocket**。因此，使用 WebSocket 的应用程序将始终以 HTTP/S 开始，然后进行升级。这种升级发生在什么时候取决于具体的应用;可以在应用启动的时候，或者当一个特定的 URL 被请求的时候。

在我们的应用中，仅当 URL 请求以“/ws”结束时，我们才升级协议为WebSocket。否则，服务器将使用基本的 HTTP/S。一旦连接升级，之后的数据传输都将使用 WebSocket 。

当然，和HTTP一样，websocket也有一些约定的通讯方式，http通讯方式为http开头的方式,e.g. http://xxx.com/path ,websocket通讯方式则为ws开头的方式,e.g. ws://xxx.com/path
![bg2017051502](C:\Users\CQY\Desktop\python_homework\img\bg2017051502.png)

它的最大特点就是，服务器可以主动向客户端推送信息，客户端也可以主动向服务器发送信息，是真正的双向平等对话，属于服务器推送技术的一种。 

#### 3）Flask_Login

Flask_Login为Flask提供了用户对话管理它处理了日常的登入，登出并且长时间记住用户的会话。

它会:

- 在会话中存储当前活跃的用户 ID，让你能够自由地登入和登出。
- 让你限制登入(或者登出)用户可以访问的视图。
- 处理让人棘手的 “记住我” 功能。
- 帮助你保护用户会话免遭 cookie 被盗的牵连。
- 可以与以后可能使用的 Flask-Principal 或其它认证扩展集成。

但是，它不会:

- 限制你使用特定的数据库或其它存储方法。如何加载用户完全由你决定。

- 限制你使用用户名和密码，OpenIDs，或者其它的认证方法。

- 处理超越 “登入或者登出” 之外的权限。

- 处理用户注册或者账号恢复。

#### 4）Flask_socketio

 flask-socketio赋予了flask程序支持服务端和客户端间双向低延迟通讯的能力，客户端可以使用 [SocketIO](http://socket.io/) 库或任何支持与服务端建立长链接的兼容库。 

## 二、需求分析

此次开发的网络聊天室可作为个人的即使聊天工具使用，通信的安全要求并没有那么高，但是我们要求让使用者能够即时发送即时就可以获得消息，以便于实现最基本的即时聊天功能。本聊天室由前后端两部分组成。主要包含以下功能：

### 1、用户端

需求描述：用户填写登入ID和密码，经服务器验证成功后进入聊天室主界面。

正常过程：

1）向服务器请求链接，发送登录信息

2）服务端处理并查询数据库中的用户信息

3）返回前端一个响应，提示登录成功，弹出聊天室主界面

4）聊天主界面即时接收消息并刷新聊天内容

异常过程：

1）用户填写的ID或者密码与数据库中的记录不匹配，前端提示登录失败

2）前端设置的服务器地址或者端口有误

3）服务器未启动或者出现异常

### 2、聊天室

需求描述：

通过系统颜值的用户可进入公共聊天室 的在线用户聊天界面，用户可以对当前的聊天系统发送消息，同时在线的用户可以即时收到消息

正常过程：

1）用户端和服务端建立通讯

2）用户端将用户发送的信息发送给服务端

3）服务端进行数据分析，并将用户的信息传给当前所有的用户

4）目的用户收到服务端的信息后，正确的显示并保存

## 三、程序功能设计

### 1、概述

虚拟茶话会实际上是一个在线聊天室，它是一个古老而又现代的东西。从互联网初期星期的各种叫交友聊天室，到各种即时通讯应用，再到现在功能丰富的团队协作聊天工具，这些都可以算作是聊天室，这次我将实现一个功能较为简单的聊天室，用户在注册账户之后就可以直接登陆进聊天室有其他在线的用户互相问候聊天。

### 2、注册界面

注册界面是聊天室访问时最开始的界面，页面中包含创建用户的表单框，以及进入登陆界面的按钮。页面底部包含程序的版权标识和编写者、源码等相关信息。

### 3、登录界面

登录界面是访问聊天室要经过的必要界面，页面中包含了登陆表单，以及简单清新的登陆注册按钮，页面底部同样包含程序的版权标识和编写者、源码等相关信息。

### 4、聊天室界面

聊天室界面是本软件设计程序中的主要部分，这个界面中主要包含了聊天消息接收部分和消息发送部分，每个用户发送到聊天室内的消息都会被反映出来。聊天消息接受部分的背景颜色要深一点，创建专门用于显示消息的聊天框。

### 5、登陆/注册表单

登陆以及注册表单，这个表单包含用户名和密码两个字段，其中用户名字段和密码字段是普通的文本字段<input type="text">，为了获得良好的样式效果，对这两个字段的输入值进行长度上的限制，用户名最长为20个字符，而密码字段也设置为最长为32个字符。

用户提交发布表单之后：

1）如果验证出错，错误消息以flash消息的形式显示在页面上方

2）如果通过验证，则在程序标题小猫显示一个提示消息，用户可以通过提示消息判断自己消息是否通过认证

### 6、消息表单

消息表单，这个表单包含用户名、头像、时间和消息内容四个字段，其中用户名字段是普通的文本字段<input type="text">，头像则是通过用户名字段从网络获取头像网站获取的字段，时间和消息内容字段也是普通的文本字段<input type="text">

### 7、错误页面

错误页面包括404错误页面和500错误页面，和主页包含相同的部分——程序标题。程序标题下显示错误信息和一个返回主页的“Go Back”链接。为了保持简单，错误页面加入页脚信息。

## 四、前端页面开发

### 1、草图及原型图制作

在前面列出的流程中，我们首先使用纸笔画出草图，然后使用原型设计软件画出原型图，最后编写对应的HTML页面。根据程序的页面数量和复杂程度，我们可以按需调整。我们直接用圆形工具画出原型图：

注册界面：


登陆界面：


聊天室界面：


### 2、前端界面编写

为了简化工作量，我们直接采用了Boostrap模版来编写HTML界面，最后的实现效果：

注册界面：


登录界面：


聊天室界面：


在传统的Flask程序中，后端完成功能后会操作HTML代码，在其中添加Jinja2语句。比如，将页面中的临时URL替换为url_for()函数调用，把虚拟数据换成通过试图函数传入模版的变了，或是使用模版继承等技术组织这些HTML文件。

## 五、后段程序开发

后端程序开发主要包含了几个方面：数据库建模、创建表单类、编写视图函数以及编写模版几部分。

### 1、数据库建模

我们在编写完功能规格书之后，我们也就确定了需要使用哪些表来存储数据，表中需要创建哪些字段以及各个表之间的关系。对于复杂的数据库结果，我们可以使用建模工具来辅助建立数据关系。

### 2、创建表单类

表单包括了用户名密码表单和消息接收发送表单，我们使用了文本区域字段TextAreaField，表示HTML中的<testarea>标签

### 3、编写视图函数

错误处理的函数比较简单，我们重点介绍一下index视图。index视图有两个作用：

1）处理GET请求，从数据库中查询所有的消息记录，返回渲染后的包括消息列表的主页模版index.html。

2）处理POST请求，问候表单提交之后，验证表单数据，通过验证后将数据保存到数据库中，使用flash()函数显示一条提示，然后重定向到index视图，渲染页面。

在获取消息记录是，我们可以使用order_by()过滤器对数据库记录进行过滤和排序，参数是排序的规则。我们根据Message模型的timestamp字段值排序，字段上附加的排序方法为desc()，代表降序（descending），同样还有一个asc()方法表示升序（ascending）。

### 4、编写模版

我们将index.html和404.html，以及500.html中的共有部分抽出合并为基模版base.html。基模版包含一个完整的HTML结构，我们在其中创建了几个块：title、content和footer。

我们可以在head标签和body标签内引入Boostrap所需的CSS和JavaScript文件，以及Boostrap所依赖的jQuery和Popper.js。另外，我们还可以引入我们自己所编写的CSS样式定义和JavaScript代码

利用模版，我们还可以直接编写出我们的login.html登录界面和注册界面

## 六、测试效果

### 1、注册


### 2、登陆


### 3、聊天室


## 七、报告总结

### 1、更多功能

在这次个人项目中，我仅仅是实现了最基本的聊天功能，但未能实现更多功能，一个完整的聊天室，一个完整的聊天室要实现的功能包括：权限管理，放开未登录也可以进入聊天室，对接自动聊天机器人，禁言功能，踢人功能，除此之外还应该优化代码逻辑框架，采用MVC架构，减少代码耦合度，实现更好的扩展和维护

### 2、总结和感想

在本次个人项目的实现过程中，我学习了很多关于前后端如何构建一个可用的网站的知识，从Boostrap到flask，有大量知识需要自己认真学习并运用在自己的聊天室中，实现虚拟茶话会的功能。

