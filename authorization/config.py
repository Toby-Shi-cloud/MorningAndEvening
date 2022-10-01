# coding=utf-8
import json


def get_config(name):
    with open("authorization/config.json", encoding='utf-8') as f:
        return json.load(f)[name]
