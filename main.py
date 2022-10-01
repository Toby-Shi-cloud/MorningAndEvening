# coding=utf-8

import random
from wechatpy.client.api import WeChatMessage
from wechatpy import WeChatClient, WeChatClientException
from utils.motto import get_motto
from utils.weather import get_weather
from utils.date import *


def get_random_color():
    r = random.randint(0, 0xFF)
    g = random.randint(0, 0xFF)
    b = random.randint(0, 0xFF)
    if r + g + b >= 500 or g >= 180:
        return get_random_color()
    return "#%02x%02x%02x" % (r, g, b)


if __name__ == '__main__':
    user_name = 'yu-yu'
    # user_name = 'rui-rui'
    user_dict = get_config(user_name)
    all_weather = get_weather(user_dict['city'])
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
        "temperature": {
            "value": '%.1f' % (float(all_weather['temp'])),
            "color": get_random_color()
        },
        "max_temperature": {
            "value": '%.1f' % (float(all_weather['high'])),
            "color": get_random_color()
        },
        "min_temperature": {
            "value": '%.1f' % (float(all_weather['low'])),
            "color": get_random_color()
        },
        "reminders": {
            "value": '无',
            "color": get_random_color()
        },  # todo ?
        "greeting": {
            "value": '新的一天也要元气满满哦~',
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
    try:
        client = WeChatClient(get_config('appID'), get_config('appSecret'))
    except WeChatClientException as e:
        print('微信获取 token 失败，请检查 APP_ID 和 APP_SECRET，或当日调用量是否已达到微信限制。')
        exit(502)

    wm = WeChatMessage(client)
    try:
        print(f'正在发送给 {user_name}, 数据如下：')
        print(json.dumps(data, indent=4, ensure_ascii=False))
        res = wm.send_template(user_dict['userID'], user_dict['templateID'], data)
    except WeChatClientException as e:
        print(f'微信端返回错误：{e.errmsg}。错误代码：{e.errcode}')
        exit(502)
