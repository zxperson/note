# 此案例中 windows 充当 客户端, broker 和 worker 都在 乌班图中。


from celery import Celery

app = Celery('demo')
app.config_from_object('celery_tasks.config')

app.autodiscover_tasks(['celery_tasks.task_1', 'celery_tasks.task_2'])
