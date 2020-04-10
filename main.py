#!/usr/bin/python3

import datetime
import time
import configparser
import os
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler

def timedTask(cmd):
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    os.system(cmd)

if __name__ == '__main__':
    cf = configparser.ConfigParser()
    cf.read("app.conf")
    secs = cf.sections()

    # 创建后台执行的 schedulers
    scheduler = BlockingScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    for job in secs:
        cmd = cf.get(job, "command")
        scheduler.add_job(timedTask,'cron', second=cf.get(job, "second"),minute=cf.get(job, "minute"), args=[cmd])
        #scheduler.add_job(timedTask,'cron', second=cf.get(job, "second"),minute=cf.get(job, "minute"),hour=cf.get(job, "hour"),day_of_week=cf.get(job, "day_of_week"),day=cf.get(job, "day"),week=cf.get(job, "week"),
        #        month=cf.get(job, "month"),year=cf.get(job, "year"),start_date=cf.get(job, "start_date"),end_date=cf.get(job, "end_date"),timezone=cf.get(job, "timezone"), args=[cmd])
    # 启动调度任务
    scheduler.start()
