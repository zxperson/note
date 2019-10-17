# 此案例中 windows 充当 客户端, broker 和 worker 都在 乌班图中。


from celery import Celery

# 我们这里案例使用redis作为broker
# broker 就是中间人，其实就是队列，用来保存 需要异步执行的任务
# broker 参数中 123 是 reids访问密码
# backend 指定 异步任务执行结果保存的 位置。
app = Celery(
    'demo',
    broker='redis://:123@192.168.9.10/1',
    backend='redis://:123@192.168.9.10/2'
)

# 4 版本 默认使用 json模块序列化 ，3 版本默认使用 pickle模块序列化
# 详细配置参考：http://docs.celeryproject.org/en/master/userguide/configuration.html#
app.conf['CELERY_TASK_SERIALIZER'] = 'pickle'
app.conf['CELERY_RESULT_SERIALIZER'] = 'pickle'
app.conf['CELERY_ACCEPT_CONTENT'] = ['json', 'pickle']


# 创建异步任务函数,通过加上装饰器app.task, 将其注册到broker的队列中。
@app.task
def my_task(a, b):
    print("异步任务函数正在执行....a+b=%s" % (a + b))

    return a + b


"""
1. 
    1.1 把 当前这个tasks.py 上传到 ubuntu中。例如上传到用户家目录下。
    1.2 打开乌班图中的 代码文件,添加如下代码：
    
        app.conf['CELERY_TASK_SERIALIZER'] = 'pickle'
        app.conf['CELERY_RESULT_SERIALIZER'] = 'pickle'
        app.conf['CELERY_ACCEPT_CONTENT'] = ['json', 'pickle']
        
        win10 中 只能使用 3版本的 Celery。
        win10 中的 Celery 是 3版本的,ubuntu中的是 4版本的。3 版本和 4版本 进行序列化 会报错，所以需要添加配置。
        
2. 
    进入ubuntu用户家目录下，然后执行：celery -A tasks worker --loglevel=info
    创建 worker, 等待处理异步任务。
    
    
3.  

    执行 app.py

"""
