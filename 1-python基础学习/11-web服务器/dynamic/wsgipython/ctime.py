# coding:utf-8

import time

# "/ctime.py?timezone=e8"
# "/ctime.py?timezone=e1"


def application(env, start_response):
    '''app提供的一个接口，给服务器调用'''

    # env.get("Method")
    # env.get("PATH_INFO")
    # env.get("QUERY_STRING")

    status = "200 OK"

    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, headers)

    return time.ctime()      # str 类型 







