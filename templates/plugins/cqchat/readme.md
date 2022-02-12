cq-chatlogger
=============================

-------------------------

## 简介
> cq-chatlogger 是基于fastbuilder和go-cqhttp协议以实现双方通信的插件.
> 
> 它可以把QQ群中的消息转发至游戏,以及将游戏聊天框消息转发至QQ群.
> 
> 你也可以借助它来实现在QQ中使用minecraft 基岩版命令的效果,
> 
> 如果你有一套和go-cqhttp差不多的协议端, 你也可以模仿两者间的通信格式来连接更多东西.
>
> btw,现在的(修改的)插件框架和插件仍然很不完善,有很多bug
> 
> 希望大家多多谅解,bug请反馈至 1758489207@qq.com , 我们会尽快修补.
-----------------

## 使用教程
> **暂时只支持linux x86_64**
> 
> 在这之前 请先确保你已经拥有了[魔改后的fastbuilder](101.43.179.210/download/fastbuilder)噢!
> 
> 另外, 希望你在面对繁琐的安装步骤时, 还能保持如初的耐心 :)

+ 安装插件
  - Windows
    
    抱歉, 暂时不支持Windows系统. 您可以在Microsoft Store中下载[Ubuntu UWP](https://www.microsoft.com/zh-cn/p/ubuntu-2004-lts/9n6svws3rx71#activetab=pivot:overviewtab)以运行Ubuntu子系统. 

    安装教程可见[Windows10开启Ubuntu子系统简易步骤](https://zhuanlan.zhihu.com/p/34133795).


  - iOS
    
    支持吗? 我也不知道. 期待dalao们愿意帮助我们实现更多平台.

  - Linux x86_64(fastbuilder官方推荐的平台)
    
    ```shell
    mkdir ~/.config/fastbuilder/plugins_beta/

    wget -O ~/.config/fastbuilder/plugins_beta/cq-chatlogger.so  101.43.179.210/download/plugin/cq-chatlogger
    ```
    

  - Android
    尚未支持(为什么交叉编译全报错啊啊啊啊啊)
    

+ 安装go-cqhttp
    - 下载
      - Android termux
        ```shell
        wget -O go-cqhttp.tar.gz https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc1/go-cqhttp_linux_armv7.tar.gz
        ```
      
      - Linux
        ```shell
        wget -O go-cqhttp.tar.gz https://github.com/Mrs4s/go-cqhttp/releases/download/v1.0.0-rc1/go-cqhttp_linux_amd64.tar.gz
        ```
    - 初始化  
      ```shell 
      tar -zxvf ./go-cqhttp.tar.gz
      ```
    - 运行
      ```shell
      ./go-cqhttp
      ```
      按照提示选择"反向websocket连接"
      
    - 配置文件
      
      **注意配置项键后面要加个空格!(比如uin, password等)**
      ```shell
      sed -i '4c [[:space:]][[:space:]]uin: 机器人绑定的QQ帐号(建议使用小号)' ./config.yml

      sed -i '5c [[:space:]][[:space:]]password: "小号的QQ密码"' ./config.yml

      sed -i '96c [[:space:]][[:space:]][[:space:]][[:space:]][[:space:]][[:space:]]universal: ws://127.0.0.1:5555/fastbuilder/cqchat'
      ```
      
      


+ 插件配置文件
  - 先运行一下mr-fastbuilder,让它生成配置文件.
    ```shell
    ./mr-fastbuilder
    ```
    按程序"配置文件已生成, 配置后重启生效"之类的提示退出.
  - 接着,简单的配置:
    ```shell
    sed '9c filtered_users: [你的机器人的名字, ]' ~/.config/fastbuilder/plugins_beta/cqchat-config.yml

    sed '12c default_group_id: 游戏消息转发到的qq群号' ~/.config/fastbuilder/plugins_beta/cqchat-config.yml
    ```
  - 或者更复杂的配置:
    
    使用vim或者nano
    ```shell
    vim ~/.config/fastbuilder/plugins_beta/cqchat-config.yml
    ```
    > tips: [这里](https://www.zhihu.com/question/432439521/answer/1653191042)有某位dalao对使用这两个工具的看法噢

+ 开始使用!

  希望在看到这里时, 你已经**正确完成**了如上所有的配置工作.
  
  请开启两个窗口分别运行go-cqhttp和fastbuilder.
  ```shell
    screen -S go-cqhttp
    ./go-cqhttp
    ```
    <br>
  <kbd>Ctrl</kbd>+<kbd>a</kbd>+<kbd>d</kbd>
  
  ```shell
  ./mr-fastbuilder
  ```
  - MC >>>> QQ :
    
    机器人将不会转发配置文件中 filtered_users 定义的玩家的消息.

    如果您定义了group_nickname, 你可以使用 设置的群号的代称 来将消息发送至特定群聊.

  - QQ >>>> MC :

    机器人将不会对拥有 配置文件中filtered_tag (默认为 filtered) 的玩家转发来自QQ的消息.