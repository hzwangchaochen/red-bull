import datetime
import time

#获取当天的时间
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_str)

#获取当天的日期
now1 = datetime.datetime.now().date()
now2 = datetime.date.today()

#str转日期
begin_date_str  = "20180717"
begin_date = datetime.datetime.strptime(begin_date_str, '%Y%m%d')
#begin_date = time.strptime(begin_date_str, '%Y%m%d')
print(type(begin_date))
print(begin_date)

#从当前天开始算，得到五天前的date
end_date = begin_date - datetime.timedelta(days=5)
print(type(end_date))
print(end_date)
end_date_str = end_date.strftime('%Y-%m-%d')
print(type(end_date_str))
print(end_date_str)

#获取两个日期之间隔了多少天
start_sec = time.mktime(time.strptime(begin_date_str, '%Y%m%d'))
end_sec = time.mktime(time.strptime(end_date_str, '%Y-%m-%d'))
print((end_sec-start_sec)/(3600*24))
