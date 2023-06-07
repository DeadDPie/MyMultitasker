import json
from random import randint

from fastapi import HTTPException

from schemas.projects_schema import Project, ProjectCreate

all_projects: list[dict] = [
    {
        "proj_id": 75
    },
    {
        "proj_id": 381,
    }
]


class ProjectManagment:
    def __init__(self, project_data: list[dict]) -> None:
        self.project_data = project_data

    def get_projects(self) -> list[Project]:
        items = []
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        for item in data["all_projects"]:
            items.append(
                Project(
                    proj_id=item['proj_id'],
                    owner_id=item['owner_id'],
                    title=item['title'],
                    tasks = item['tasks']
                )
            )
        return items

    def make_project(self, payload: ProjectCreate):
        new_project = {
            "proj_id": randint(3, 500),
            "owner_id": payload.owner_id,
            "title": payload.title,
            "tasks": []
        }
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        flag = 0
        for item in data["all_users"]:
            if item["id"] == payload.owner_id:
                flag = 1
        if flag == 0:
            raise HTTPException(status_code=400, detail="There is no such user")
        for item in data["all_projects"]:
            while item["proj_id"] == new_project["proj_id"]:
                new_project["proj_id"] = randint(10, 500)

        data["all_projects"].append(new_project)
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {'status': 200, 'info': 'Project added successfully'}

    def delete_project(self, proj_id: int):
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)

        for i in range(len(data["all_projects"])):
            if data["all_projects"][i]["proj_id"] == proj_id:
                data["all_projects"].pop(i)
                break

        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(data, f, indent=2)

        return {'status': 200, 'info': 'Project was deleted successfully'}


project_service: ProjectManagment = ProjectManagment(all_projects)
