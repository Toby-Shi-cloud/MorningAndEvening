# coding=utf-8
import requests


def get_weather(city):
    if not isinstance(city, str):
        return None
    url = "http:" + "//autodev.openspeech.cn/csp/api/v2.1/weather?"
    suffix = "openId=aiuicus&clientType=android&sign=android&city=" + city
    res = requests.get(url + suffix, timeout=200).json()
    if res is None:
        return None
    if res['code'] != 0:
        return None
    weather = res['data']['list'][0]
    return weather
