# coding=utf-8
import re
from functools import reduce


def get_weather():
    return {
        'weather': input(),
        'high': input(),
        'low': input(),
        'feel': input(),
        'humidity': input(),
        'rain': input()
    }


def get_classes():
    n = int(input())
    if n == 0:
        return '今日无课程！\n'
    names = [input() for _ in range(n)]
    starts = [input() for _ in range(n)]
    ends = [input() for _ in range(n)]
    locations = [input() for _ in range(n)]

    def get_where(x: str):
        match = re.search(r'[A-Z]-\d*', x)
        return x if match is None else match.group()
    locations = list(map(get_where, locations))

    return '课程提醒:\n' + \
        reduce(lambda x, y: x + y,
               [names[i] + ': ' + starts[i] + '-' + ends[i] + ' ' + locations[i] + '\n'
                for i in range(n)])
