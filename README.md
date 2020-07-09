# send training results to your mailbox in remote machine
`easy_smtp_sender`这个python文件，定义了一个简单的smtp邮件发送类
它利用**QQ邮箱提供的第三方服务**，来发送简单的邮件。当然也欢迎大家提交代码来扩展支持的平台。
目前它仅支持的功能有：
* 发送邮件到指定的邮箱
* 邮件正文只能包含简单文本(一段字符串)
* 附件支持文本，图片，视频的批量发送
* 因为和邮箱服务器连接的缘故，每次发生时最好实例化一下，像下图一样使用
# Demo
我来演示一下如何使用这个模块

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-09_15-57-33.png)

如上所示的导入了类以后，就可以方便的使用它。考虑到和邮箱服务的连接不稳定，所以还是像上图这样使用。每次实例化一下。
下图展示了我正确的收到了邮件：

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-04_19-12-21.png)

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-04_19-12-38.png)

每个附件发送一次：打印出发送成功，当然你可以选择静默操作。见代码接口部分

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-04_19-09-38.png)

# 接口用法
类的实例化接口为：

`EasySmtpSender(sender,password,receiver=None,msg_from=None,is_silent=True)`

* 其中sender与password是必选的参数。sender就是你的邮箱，password是qq邮箱第三方服务的授权码。授权码的申请方法参见下一节。
* receiver若是不指定的话邮件会被默认的发送到你的sender邮箱中。一般来说不需要指定。
* msg_form用来指定发件人的姓名，默认是你的邮箱，一般不用指定。
* 上面所述的参数都是字符串
* is_silent是一个布尔参数用来指定是否输出‘发送成功’之类的信息。默认是不输出这些消息。

实例化以后只有一个接口可以使用：

`object.send_mail(subject,main_body_text=None,attachment=None)`

* subject是一个字符串，指定邮件主题
* main_body_text是一个字符串，指定正文的文本。可以将本轮训练的loss放在正文。
* attachment既可以是一个文件路径的字符串，也可以是一个文件路径的列表。其中的文件会以附件的形式发送。

# 获取QQ邮箱的授权码

请参见CSDN教程 https://blog.csdn.net/qq_36528311/article/details/88616990
