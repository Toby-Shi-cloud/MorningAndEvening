# coding=utf-8
import json
import requests
from authorization.config import get_config
from datetime import date, datetime, timedelta


def get_today():
    now_time = datetime.utcnow() + timedelta(hours=8)  # 东八区时间
    today = datetime.strptime(str(now_time.date()), "%Y-%m-%d")  # 今天的日期
    return today


def get_date(today=get_today()):
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week_day = week_list[datetime.date(today).weekday()]
    return today.strftime('%Y年%m月%d日') + ' ' + week_day


def get_festival(today=get_today()):
    # return [
    #     {'startday': '2022-1-1', 'name': '元旦节'},
    #     {'startday': '2022-1-31', 'name': '除夕'},
    #     {'startday': '2022-2-1', 'name': '春节'},
    #     {'startday': '2022-4-5', 'name': '清明节'},
    #     {'startday': '2022-5-1', 'name': '劳动节'},
    #     {'startday': '2022-6-3', 'name': '端午节'},
    #     {'startday': '2022-9-10', 'name': '中秋节'},
    #     {'startday': '2022-10-1', 'name': '国庆节'}
    # ]
    url = "https://api.topthink.com/calendar/year"
    params = {'year': str(today.year), 'appCode': get_config('thinkAPI')}
    res = requests.get(url, params=params)
    res = res.json()
    if res is None:
        return None
    if res['code'] != 0:
        return None
    return res['data']['holiday_list']


def get_festival_countdown(today=get_today()):
    festivals = get_festival(today)
    if festivals is None:
        return None
    festival_date = date(today.year + 1, 1, 1)
    festival_name = "元旦节"
    for fest in festivals:
        start_day = fest['startday'].split('-')
        start_day = date(int(start_day[0]), int(start_day[1]), int(start_day[2]))
        if today.date() <= start_day < festival_date:
            festival_date = start_day
            festival_name = fest['name']
    return {
        'festival_name': festival_name,
        'festival_countdown': (festival_date - today.date()).days,
        'festival_date': festival_date.strftime("%Y-%m-%d")
    }


def get_countdown(user_name, today=get_today().date()):
    try:
        countdowns: dict = get_config(user_name)['countdown']
    except KeyError:
        return {}
    d = {}
    for k, v in countdowns.items():
        v = v.split('-')
        if len(v) == 2:
            day = date(today.year, int(v[0]), int(v[1]))
            if day < today:
                day = date(day.year + 1, day.month, day.day)
        else:
            day = date(int(v[0]), int(v[1]), int(v[2]))
        d[k] = (day - today).days
    return d


def get_countup(user_name, today=get_today().date()):
    try:
        countups: dict = get_config(user_name)['countup']
    except KeyError:
        return {}
    d = {}
    for k, v in countups.items():
        v = v.split('-')
        day = date(int(v[0]), int(v[1]), int(v[2]))
        d[k] = (today - day).days
    return d


