import json
from random import randint

from fastapi import HTTPException

from schemas.projects_schema import Project

all_projects: list[dict] = [
    {
        "id": 75
    },
    {
        "id": 381,
    }
]


class ProjectManagment:
    def __init__(self, project_data: list[dict]) -> None:
        self.project_data = project_data

    def get_projects(self) -> list[Project]:
        items = []
        with open("D:\PycharmProjects\MyMultiprojecter\services\data.json", "r") as f:
            data = json.load(f)
        for item in data["all_projects"]:
            items.append(
                Project(
                    id=item['id'],
                    owner_id=item['owner_id'],
                    title=item['title'],
                    importance=item['importance'],
                    executor=item['executor'],
                    description=item['description']
                )
            )
        return items

    def make_project(self, payload: Project):
        new_project = {
            "id": randint(3, 500),
            "owner_id": payload.owner_id,
            "title": payload.title,
            "importance": payload.importance,
            "executor": payload.executor,
            "description": payload.description
        }
        with open("D:\PycharmProjects\MyMultiprojecter\services\data.json", "r") as f:
            data = json.load(f)
        flag = 0
        for item in data["all_users"]:
            if item["id"] == payload.owner_id:
                flag = 1
        if flag == 0:
            raise HTTPException(status_code=400, detail="There is no such user")
        for item in data["all_projects"]:
            while item["id"] == new_project["id"]:
                new_project["id"] = randint(10, 500)

        data["all_projects"].append(new_project)
        with open("D:\PycharmProjects\MyMultiprojecter\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {"message": "project added successfully"}

    def delete_project(self, id: int):
        with open("D:\PycharmProjects\MyMultiprojecter\services\data.json", "r") as f:
            data = json.load(f)

        for i in range(len(data["all_projects"])):
            if data["all_projects"][i]["id"] == id:
                data["all_projects"].pop(i)
                break

        with open("D:\PycharmProjects\MyMultiprojecter\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {"message": "project was deleted successfully"}


project_service: ProjectManagment = ProjectManagment(all_projects)
