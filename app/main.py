from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session
from model import TaskTable, Task

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# 全タスク
@app.get("/tasks")
def read_tasks():
  tasks = session.query(TaskTable).all()
  return tasks

# 個別タスク
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
  task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
  return task

# タスク作成
@app.post("/task")
async def create_task(title: str):
  task = TaskTable()
  task.title = title
  session.add(task)
  session.commit()

# タスク更新
@app.put("/tasks")
async def update_tasks(tasks: List[Task]):
  for new_task in tasks:
    task = session.query(TaskTable).filter(TaskTable.id == new_task.id).first()
    task.title = new_task.title
    session.commit()

# タスク削除
@app.delete("/tasks/{task_id}")
def read_task(task_id: int):
  task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
  session.delete(task)
  session.commit()
