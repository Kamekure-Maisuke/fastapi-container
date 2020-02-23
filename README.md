# fast-api container template
- fastapiのdocker template
- 基本的なtodo CRUD 機能

## start

```bash
$ docker-compose up -d --build
```

## use
- 下記にアクセスして、初期タスク確認
  - localhost:8000/tasks
    - get all tasks
  - localhost:8000/tasks/{task_id}
    - get custom task

- 各種取得・登録・更新・削除はこちらで可能
  - localhost:8000/docs
    - swagger api document
  - localhost:8000/redoc
    - redoc api document