# 启动异步任务

from celery_tasks.task_1.tasks import my_task_1
from celery_tasks.task_2.tasks import my_task_2

my_task_1.delay(1,2)
my_task_2.delay(4,5)



"""
启动之前，先要把 celery_tasks 传到 乌班图中，然后启动worker：

    celery -A celery_tasks.main worker --loglevel=info

"""