'''
日期
'''
import calendar
import datetime

'''
输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。
'''
mmonthRange = calendar.monthrange(2018, 7)
print(mmonthRange)


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


print(getYesterday())
