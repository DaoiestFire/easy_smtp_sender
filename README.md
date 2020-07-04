# send training results to your mailbox in remote machine
`easy_smtp_sender`这个python文件，定义了一个简单的smtp邮件发送类
它利用**QQ邮箱提供的第三方服务**，来发送简单的邮件。
目前它仅支持的功能有：
* 发送邮件到指定的邮箱
* 邮件正文只能包含简单文本(一段字符串)
* 附件支持文本，图片，视频的批量发送
# Demo
我来演示一下如何使用这个模块

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-04_19-07-03.png)

如上所示的导入了类以后，就可以使用with关键字来方便的使用它。上面的这段代码会发送包含一批附件的邮件
下图展示了我正确的收到了邮件：

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-04_19-12-21.png)

![image](https://github.com/DaoiestFire/easy_smtp_sender/blob/master/images/Snipaste_2020-07-04_19-12-38.png)
