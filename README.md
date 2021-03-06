# WHU_MOOC
A Python script for answer MOOC questions of Wuhan University quickly by keyboard

- 这个程序现在只能帮助你：通过输入1、2、3、4的方式来避免鼠标点按，提高你的做题效率和答题的用户体验。并没有内置答案或者一键自动做题这些功能

## Requirements
First of all, you need a valid account, i.e., a user id for Mooc system in Wuhan University.
你需要Python 3.6+，其次你需要安装好selenium包和chrome自动测试版。

Second, you ought to install Python dependencies required by those python code:
* packages like selenium. 你可以通过`pip install -U selenium`快速安装它
* [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Chrome](https://www.google.com/chrome/browser/desktop/index.html)

## 使用方法

- 通过`python Answer_Mooc_questions.py`启动程序，然后不要关闭命令行！

- 关于[输入chrome的路径，绝对路径和相对路径随便你](https://www.jianshu.com/p/e987d8e74f11)

- 启动后自动化的浏览器会自动进入登录界面，需要你在命令行内输入用户名和密码（我不会收集他们，不信自己去看源码），然后他会自动选择毛概慕课（也就是你的第一个慕课）之后你需要手动选择章节。然后在命令行内使用1234来代表abcd回答问题，多选题只需要输入1234中的多个即可，比如答案为ABD，那就是124。

- 结束这一章之后，手动点击提交，手动切换到下一章节，然后在命令行中输入回车，再次开启做题模式。

- 总而言之，命令行只提供选择选项功能，不提供提交和切换章节的功能。
