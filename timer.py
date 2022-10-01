# coding=utf-8

import sys
import time
import schedule
import subprocess


def send_message_now():
    print("running...")
    subprocess.run([f"{sys.executable}", "main.py"])
    return


if __name__ == '__main__':
    print("开始运行，等待定时触发...")

    schedule.every().day.at("08:00").do(send_message_now)

    while True:
        schedule.run_pending()
        time.sleep(50)  # wait
