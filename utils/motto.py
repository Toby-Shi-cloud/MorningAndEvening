# coding=utf-8
from random import randint
from authorization.config import get_config


def get_motto():
    index = randint(1, int(get_config('motto_num')))
    with open('utils/motto.txt', encoding='utf-8') as f:
        while True:
            s = f.readline()
            if s == '':
                return None
            if len(s) < 5:
                continue
            if int(s.split('、')[0]) == index:
                return s.split('、')[1]
