import json
from random import randint

from fastapi import HTTPException

from schemas.subtasks_schema import Subtask, SubtaskCreate

all_subtasks: list[dict] = [
    {
        "proj_id": 75
    },
    {
        "proj_id": 381,
    }
]

class subtaskManagment:
    def __init__(self, subtask_data: list[dict]) -> None:
        self.subtask_data = subtask_data

    def get_subtasks(self) -> list[Subtask]:
        items = []
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        for item in data["all_subtasks"]:
            items.append(
                Subtask(
                    subtask_id = item['subtask_id'],
                   task_id=item['task_id'],
                    owner_id=item['owner_id'],
                    title=item['title']
                )
            )
        return items

    def make_subtask(self, payload: SubtaskCreate):
        new_subtask = {
            "subtask_id": randint(3, 500),
            "task_id": payload.task_id,
            "owner_id": payload.owner_id,
            "title": payload.title,
        }
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        flag = 0
        for item in data["all_users"]:
            if item["id"] == payload.owner_id:
                flag = 1
        if flag == 0:
            raise HTTPException(status_code=400, detail="There is no such user")
        for item in data["all_subtasks"]:
            while item["subtask_id"] == new_subtask["subtask_id"]:
                new_subtask["subtask_id"] = randint(10, 500)

        data["all_subtasks"].append(new_subtask)
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {'status': 200, 'info': 'subtask added successfully'}

    def delete_subtask(self, subtask_id: int):
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)

        for i in range(len(data["all_subtasks"])):
            if data["all_subtasks"][i]["subtask_id"] == subtask_id:
                data["all_subtasks"].pop(i)
                break

        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {'status': 200, 'info': 'subtask was deleted successfully'}


subtask_service: subtaskManagment = subtaskManagment(all_subtasks)
