from ..main import app

@app.task
def my_task_1(a, b):
    print("异步任务函数1正在执行....a+b=%s" % (a + b))