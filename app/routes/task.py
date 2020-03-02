from fastapi.routing import APIRouter
from typing import List
from database import session
from models.task import TaskTable, Task

router = APIRouter()

# 全タスク
@router.get("/tasks")
def read_tasks():
  tasks = session.query(TaskTable).all()
  session.close()
  return tasks

# 個別タスク
@router.get("/tasks/{task_id}")
def read_task(task_id: int):
  task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
  session.close()
  return task

# タスク作成
@router.post("/task")
async def create_task(title: str):
  task = TaskTable()
  task.title = title
  session.add(task)
  session.commit()
  session.close()

# タスク更新
@router.put("/tasks")
async def update_tasks(tasks: List[Task]):
  for new_task in tasks:
    task = session.query(TaskTable).filter(TaskTable.id == new_task.id).first()
    task.title = new_task.title
    session.commit()
    session.close()

# タスク削除
@router.delete("/tasks/{task_id}")
def read_task(task_id: int):
  task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
  session.delete(task)
  session.commit()
  session.close()