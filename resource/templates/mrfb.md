PhoenixBuilder 修改版
==========

------
> PhoenixBuilder（修改版）（以下简称修改版）是由部分fastbuilder用户自发组织对fastbuilder开源客户端进行修改和拓展的项目。
>
>随官方项目使用的GPL v3协议，本项目的开源地址：[Click me](github.com/TwosbBot/PhoenixBuilder)

----
## 声明
+ 修改版增加了插件系统，允许用户扩展自己想要的功能。
如
+ 与原版的插件系统不同的是，由第三方开发者制作的插件可以有更大的权限，但同时带来了危险性和不确定性，而这些风险需要您自己承担。 如果您使用未经验证的插件，造成的损失我们概不负责。
+ 我们提供开源免费的修改版fastbuilder客户端（仍然需要fastbuilder账号），但有些插件可能是付费的噢

---
## 教程
由于开发者技术力有限，目前此版本只能运行于linux x86_64.
如果您使用的是windows 10（或更高）， 可以在Microsoft Store中下载[Ubuntu 20.04 LTS](https://zhuanlan.zhihu.com/p/405329231)支持运行此修改版。
果您使用的是Android Termux等终端工具，抱歉，请等待笨蛋开发者学会怎么交叉编译吧。

+ linux
    安装：
    ```shell
    wget -O ./mr-fastbuilder 101.43.179.210/download/mr-fastbuilder
    
    chmod +x ./mr-fastbuilder
``

+ 插件目录位于 **~/.config/fastbuilder/plugins_beta/** 
您可以将已经购买的插件放到此文件夹。 如果您没有购买，插件将不会加载。
+ 我们不能保证没有经过验证的插件的安全性。 您可以[联系我们](1758489207@qq.com) 以验证您自己编写的插件（不过有这个技术已经可以不通过插件了吧~）。

+ 运行
   ``
   ./mr-fastbuilder
   ``


## 随附
+ 技术力超强的 [2401PT](github.com/CMA2401PT) dalao很早就做出了ta的插件框架 [OmeGo](github.com/CMA2401PT/OmeGo), 它比本框架稳定得多. 我们在制作本框架时, 2401PT 给予了我们莫大的帮助, 很多思路和难题都是这位dalao提供和帮我们解答的(可以说ta就是这个项目的开发者之一噢). 在此特别感谢这位dalao提供的支持.
+ [OmeGo](github.com/CMA2401PT/OmeGo): 更稳定强大的插件框架. 要多多支持呀!