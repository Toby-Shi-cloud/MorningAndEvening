# coding=utf-8

import sys
import random
from wechatpy.client.api import WeChatMessage
from wechatpy import WeChatClient, WeChatClientException
from utils.motto import get_motto
from utils.call_input import *
from utils.date import *


def get_random_color() -> str:
    r = random.randint(0, 0xFF)
    g = random.randint(0, 0xFF)
    b = random.randint(0, 0xFF)
    if r + g + b >= 500 or g >= 180:
        return get_random_color()
    return "#%02x%02x%02x" % (r, g, b)


def send_msg(user_name, data, template_id, no_copy=False):
    try:
        client = WeChatClient(get_config('appID'), get_config('appSecret'))
    except WeChatClientException as e:
        print('微信获取 token 失败，请检查 APP_ID 和 APP_SECRET，或当日调用量是否已达到微信限制。')
        return 502

    wm = WeChatMessage(client)
    try:
        print(f'正在发送给 {user_name}, 数据如下：')
        print(json.dumps(data, indent=4, ensure_ascii=False))
        res = wm.send_template(get_config(user_name)['userID'], template_id, data)
    except WeChatClientException as e:
        print(f'微信端返回错误：{e.errmsg}。错误代码：{e.errcode}')
        return 502

    if no_copy:
        return 200
    # 发送一份拷贝给自己
    try:
        print(f'正在发送数据拷贝...')
        res = wm.send_template(
            get_config('copyTo'), template_id, data)
    except WeChatClientException as e:
        print(f'微信端返回错误：{e.errmsg}。错误代码：{e.errcode}')
        return 502
    
    return 200


def yuyu(reminders='', greeting='', send_to_me=False):
    print('Good Morning For yu-yu:')
    user_name = 'yu-yu'
    user_dict = get_config(user_name)
    all_weather = get_weather()
    classes = get_classes()
    if_rains = '今天有大概率下雨，记得带雨伞哦～' if float(all_weather['rain']) > 0.4 else ''
    festivals = get_festival_countdown()
    data = {
        "city": {
            "value": user_dict['city'],
            "color": get_random_color()
        },
        "date": {
            "value": get_date(),
            "color": get_random_color()
        },
        "weather": {
            "value": all_weather['weather'],
            "color": get_random_color()
        },
        "humidity": {
            "value": all_weather['humidity'],
            "color": get_random_color()
        },
        "feeling_temperature": {
            "value": all_weather['feel'],
            "color": get_random_color()
        },
        "max_temperature": {
            "value": all_weather['high'],
            "color": get_random_color()
        },
        "min_temperature": {
            "value": all_weather['low'],
            "color": get_random_color()
        },
        "rain_probability": {
            "value": all_weather['rain'],
            "color": get_random_color()
        },
        "reminders": {
            "value": reminders + classes + if_rains,
            "color": get_random_color()
        },
        "greeting": {
            "value": greeting,
            "color": get_random_color()
        },  # todo ?
        "love_day": {
            "value": get_countup(user_name)['ceremony'],
            "color": get_random_color()
        },
        "birthday": {
            "value": get_countdown(user_name)['birthday'],
            "color": get_random_color()
        },
        "festival_name": {
            "value": festivals['festival_name'],
            "color": get_random_color()
        },
        "festival_countdown": {
            "value": festivals['festival_countdown'],
            "color": get_random_color()
        },
        "motto": {
            "value": get_motto(),
            "color": get_random_color()
        }
    }
    if send_to_me:
        send_msg('rui-rui', data, user_dict['templateID'], True)
    else:
        send_msg(user_name, data, user_dict['templateID'])


if __name__ == '__main__':
    yuyu(greeting=random.choice([
        '早安～又是美好的一天！',
        '报告！今天也很爱你！',
        '早睡身体好，晚睡人会飘～',
        '早啊！要和可莉一起去炸鱼吗？虽然被抓住就是一整天的禁闭，但是🐟很好吃，所以值得！',
        '我还在梦中想你哦～'
    ]))
    # yuyu(send_to_me=True)
