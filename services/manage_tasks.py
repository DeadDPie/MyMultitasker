import json
from random import randint

from fastapi import HTTPException

from schemas.schemas import Task, TaskCreate
from services.service import UserService
all_tasks: list[dict] = [
    {
        "id": 75
    },
    {
        "id": 381,
    }
]


class TaskManagment:
    def __init__(self, task_data: list[dict]) -> None:
        self.task_data = task_data

    def get_tasks(self) -> list[Task]:
        items = []
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        for item in data["all_tasks"]:
            items.append(
                Task(
                    id=item['id'],
                    owner_id=item['owner_id'],
                    title=item['title'],
                    importance=item['importance'],
                    executor=item['executor'],
                    description=item['description']
                )
            )
        return items

    def make_task(self, payload: TaskCreate):
        new_task = {
            "id": randint(3, 500),
            "owner_id": payload.owner_id,
            "title": payload.title,
            "importance": payload.importance,
            "executor": payload.executor,
            "description": payload.description
        }
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        flag = 0
        for item in data["all_users"]:
            if item["id"] == payload.owner_id:
                flag = 1
        if flag == 0:
            raise HTTPException(status_code=400, detail="There is no such user")
        for item in data["all_tasks"]:
            while item["id"] == new_task["id"]:
                new_task["id"] = randint(10, 500)

        data["all_tasks"].append(new_task)
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {"message": "Task added successfully"}

    def delete_task(self, id: int, mail: str, password: str):
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)

        for item in data["all_users"]:
            if item['email'] != mail or item['password'] != password:
                raise HTTPException(status_code=400, detail="You are not registered")
        for i in range(len(data["all_tasks"])):
            if data["all_tasks"][i]["id"] == id:
                data["all_tasks"].pop(i)
                break

        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {"message": "Task was deleted successfully"}


task_service: TaskManagment = TaskManagment(all_tasks)
