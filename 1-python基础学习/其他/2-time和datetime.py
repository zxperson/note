UTC是协调世界时（以前称为格林威治标准时间，或GMT）。缩写UTC不是错误，而是英语和法语之间的妥协。

一、time模块

1. time.sleep()
    延时
    time.sleep(1)

2. time.time()
    获取当前时间，返回值为 unix时间戳。 (北京时间)
        In [3]: time.time()
        Out[3]: 1496819635.6071963

3. time.ctime()
    时间戳转换为字符串格式的时间。     (北京时间)
        In [6]: time.ctime()
        Out[6]: 'Wed Jun  7 15:25:54 2017'

        从左到右，依次是：星期，月、日、时、分、秒、年
        可以接收一个时间戳参数，如果不写这个参数，就代表当前时间的unix时间戳
    
4. time.localtime()
    以元组方式返回 本地 当前 时间.     (北京时间)
        In [10]: time.localtime()
        Out[10]: time.struct_time(tm_year=2017, tm_mon=6, tm_mday=7, tm_hour=15, tm_min=40, tm_sec=43, tm_wday=2, tm_yday=158, tm_isdst=0)

    既然是元祖，那一定可以支持切片和索引操作。
    元组中每个参数都是什么意思呢？可以使用help函数进行查看,比如你可以把元组时间保存为变量a，然后help(a)
    tm_isdst = 0,代表夏令时 无效，=1 代表 有效。 =-1 代表，未知

5.  time.gmtime()
    以元组方式返回格林威治时间.        (UTC时间)   北京时间领先UTC时间 8个小时
        In [24]: time.gmtime()
        Out[24]: time.struct_time(tm_year=2017, tm_mon=6, tm_mday=7, tm_hour=7, tm_min=54, tm_sec=0, tm_wday=2, tm_yday=158, tm_isdst=0)
    
    和localtime()一样。只不过，时区不同。

6.  time.mktime()    
    将元组时间转换为时间戳

        In [31]: a = time.localtime()

        In [32]: a
        Out[32]: time.struct_time(tm_year=2017, tm_mon=6, tm_mday=7, tm_hour=16, tm_min=17, tm_sec=26, tm_wday=2, tm_yday=158, tm_isdst=0)

        In [33]: time.mktime(a)
        Out[33]: 1496823446.0

        In [37]: time.mktime((2017,6,7,16,17,26,2,158,0))
        Out[37]: 1496823446.0

7. time.strftime()
    将元组时间转换为字符串格式(数字形式)时间
        In [50]: a = time.localtime()

        In [52]: time.strftime('%Y-%m-%d %H:%M:%S', a)
        Out[52]: '2017-06-07 16:30:46'

        help(time.strftime)   查看格式化参数的意思

8.  time.strptime()
    将字符串格式时间转换为元组格式时间.
        In [56]: time.strptime('2017-06-08 17:03:12','%Y-%m-%d %H:%M:%S')
        Out[56]: time.struct_time(tm_year=2017, tm_mon=6, tm_mday=8, tm_hour=17, tm_min=3, tm_sec=12, tm_wday=3, tm_yday=159, tm_isdst=-1)

9. time.asctime()
    元组格式时间转换为字符串格式时间
        In [57]: time.asctime()
        Out[57]: 'Wed Jun  7 16:57:42 2017'

        In [58]: a = time.localtime()

        In [59]: time.asctime(a)
        Out[59]: 'Wed Jun  7 16:59:38 2017'

二、datetime模块
    1.  datetime.datetime.now()
        获取当前日期和时间(本地时区)
            In [2]: datetime.datetime.now()
            Out[2]: datetime.datetime(2017, 6, 7, 17, 52, 54, 443680)

            最后一个值为，微秒。1秒等于1000毫秒，10的6次方 微秒。

    2.  datetime.datetime.utcnow()
        获取当前日期和时间(UTC时间)
            In [3]: datetime.datetime.utcnow()
            Out[3]: datetime.datetime(2017, 6, 7, 9, 56, 18, 706658)

    3.  datetime.date.today()
        获取当前的日期
            In [4]: datetime.date.today()
            Out[4]: datetime.date(2017, 6, 7)

    4.  datetime.timedelta()
        获取明天的日期
            In [6]: datetime.date.today() + datetime.timedelta(days=1,hours=1)
            Out[6]: datetime.date(2017, 6, 8)

            还可以有其他参数：
                seconds----秒
                microseconds----微秒
                milliseconds----毫秒
                minutes------分钟
                weeks-------周

        获取3天前的日期和时间
            In [10]: datetime.datetime.now() + datetime.timedelta(days=-3)
            Out[10]: datetime.datetime(2017, 6, 4, 18, 7, 33, 353766)
    
    5.  计算时间差
            In [15]: (datetime.datetime(2017,6,8,18,10,0) - datetime.datetime.now()).total_seconds()
            Out[15]: 86142.116551

            结果单位是 秒 

    6.  strftime()
        datetime对象转换为字符串格式
            In [16]: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            Out[16]: '2017-06-07 19:20:20'

    7.  strptime()
        字符串格式转换为datetime对象
            In [17]:  datetime.datetime.strptime("2017-6-7 19:20:20", "%Y-%m-%d %H:%M:%S")
            Out[17]: datetime.datetime(2017, 6, 7, 19, 20, 20)

    8.  datetime对象转换为元组时间
            In [18]: datetime.datetime.now().timetuple()
            Out[18]: time.struct_time(tm_year=2017, tm_mon=6, tm_mday=7, tm_hour=19, tm_min=24, tm_sec=8, tm_wday=2, tm_yday=158, tm_isdst=-1)

    9.  date()
        把datetime对象转换为date对象
            In [24]: datetime.datetime.now().date()
            Out[24]: datetime.date(2017, 6, 7)

    10. mktime()
        把datetime对象转化为unix时间戳
            In [3]: now = datetime.datetime.now()

            In [4]: time.mktime(now.timetuple())
            Out[4]: 1496836162.0

    11. fromtimestamp()
        把unix时间戳转换为 元组时间 
            In [5]: datetime.datetime.fromtimestamp(1496819635.6071963)
            Out[5]: datetime.datetime(2017, 6, 7, 15, 13, 55, 607196)


    12. 时区的转换

        date -- 日期对象
        datetime -- 日期时间对象
        time -- 时间对象
        timedelta -- 日期时间间隔对象
        timezone -- 时区对象
        
        #获取当前的utc时间，并且把时区换成utc+00:00
        In [9]: utc_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        In [10]: print(utc_time)
        2017-06-08 02:37:22.632604+00:00

        #把utc时间转换为对应的北京时间
        In [12]: bj_time = utc_time.astimezone(datetime.timezone(datetime.timedelta(hours=8)))

        In [13]: print(bj_time)
        2017-06-08 10:37:22.632604+08:00

        #把北京时间 转换为 东京时间
        In [14]: tokyo_time = bj_time.astimezone(datetime.timezone(datetime.timedelta(hours=9)))

        In [15]: print(tokyo_time)
        2017-06-08 11:37:22.632604+09:00



        
     
        
    


    



