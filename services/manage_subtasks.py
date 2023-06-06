import json
from random import randint

from fastapi import HTTPException

from schemas.subtasks_schema import Subtask

all_subtasks: list[dict] = [
    {
        "id": 75
    },
    {
        "id": 381,
    }
]


class SubtaskManagment:
    def __init__(self, subtask_data: list[dict]) -> None:
        self.subtask_data = subtask_data

    def get_subtasks(self) -> list[Subtask]:
        items = []
        with open("D:\PycharmProjects\MyMultisubtasker\services\data.json", "r") as f:
            data = json.load(f)
        for item in data["all_subtasks"]:
            items.append(
                Subtask(
                    id=item['id'],
                    owner_id=item['owner_id'],
                    title=item['title'],
                    importance=item['importance'],
                    executor=item['executor'],
                    description=item['description']
                )
            )
        return items

    def make_subtask(self, payload: Subtask):
        new_subtask = {
            "id": randint(3, 500),
            "owner_id": payload.owner_id,
            "title": payload.title,
            "importance": payload.importance,
            "executor": payload.executor,
            "description": payload.description
        }
        with open("D:\PycharmProjects\MyMultisubtasker\services\data.json", "r") as f:
            data = json.load(f)
        flag = 0
        for item in data["all_users"]:
            if item["id"] == payload.owner_id:
                flag = 1
        if flag == 0:
            raise HTTPException(status_code=400, detail="There is no such user")
        for item in data["all_subtasks"]:
            while item["id"] == new_subtask["id"]:
                new_subtask["id"] = randint(10, 500)

        data["all_subtasks"].append(new_subtask)
        with open("D:\PycharmProjects\MyMultisubtasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {"message": "subtask added successfully"}

    def delete_subtask(self, id: int):
        with open("D:\PycharmProjects\MyMultisubtasker\services\data.json", "r") as f:
            data = json.load(f)

        for i in range(len(data["all_subtasks"])):
            if data["all_subtasks"][i]["id"] == id:
                data["all_subtasks"].pop(i)
                break

        with open("D:\PycharmProjects\MyMultisubtasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {"message": "subtask was deleted successfully"}


subtask_service: SubtaskManagment = SubtaskManagment(all_subtasks)
