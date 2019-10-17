from tasks import my_task
import time


# 告诉 broker 可以执行 my_task 这个异步任务了
# 然后 broker 通知 worker 开始执行 异步任务。
# 传入的两个值, 是 异步任务函数的 值
# delay不会阻塞主线程,异步任务执行完，返回一个AsyncResult对象，这个对象可以用来检查任务的状态或者获得任务的返回值。
ret = my_task.delay(100, 200)

time.sleep(2)       # 等待异步任务执行完 方便我们看现象

print(ret.ready())   # 任务执行完成返回True,如果任务仍在运行，挂起或正在等待重试，则返回False
print(ret.failed())  # 异步任务如果执行失败，返回True
print(ret.result)    # 异步函数 return 返回值
ret.forget()     # 警告： 当我们获取到 异步函数的返回值之后，必须调用这个方法，释放资源，不然你的存储资源会越来越小
print(ret.result)  # 打印None, redis中 异步函数执行的返回值已经被删除了。


"""
默认 Celery 不会保存 任务的执行结果。
可以把 异步任务执行的结果保存到：SQLAlchemy/Django ORM, Memcached, Redis, RPC (RabbitMQ/AMQP), 也可以自己定义

"""