from celery import Celery
from datetime import datetime
import time

app = Celery('tasks', broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

@app.task
def show_time():
    time.sleep(10)
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
