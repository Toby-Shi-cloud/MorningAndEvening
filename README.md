## 前言
目前本版本还非常不完善，仅仅是达到了能用的程度。后续可能会持续更新。

## 用法
1. 前往[微信测试号平台](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)注册账号。
2. 把二维码发给你希望推送的人，让ta关注。
3. 添加一个模板，示例如下：
    ```text
    早上好！今天是：{{date.DATA}}
    
    {{greeting.DATA}}
    
    下面是今日の{{city.DATA}}的天气播报(/^~^/)
    
    今天的天气：{{weather.DATA}}
    湿度：{{humidity.DATA}}
    温度：{{temperature.DATA}}
    最低气温：{{min_temperature.DATA}}
    最高气温：{{max_temperature.DATA}}
    
    提醒事项：
    {{reminders.DATA}}
    
    我们已经在一起{{love_day.DATA}}天啦
    距离***的生日还有{{birthday.DATA}}天
    距离{{festival_name.DATA}}还有{{festival_countdown.DATA}}天
    
    每日一言：{{motto.DATA}}
    ```
4. 填写`config_template.json`并更名为`config.json`。
5. `main.py`的第21行，把`user_name`改为你在`config.json`中填写的`自定义用户名称`。
6. 运行`main.py`即可发送信息。
7. 运行`timer.py`可以自动在8:00发送信息。
