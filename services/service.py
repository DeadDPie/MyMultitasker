from fastapi import HTTPException

from schemas.schemas import User, Credentials, UserCreate, UserRestore
from random import randint
import json

user_data: list[dict] = [
    {
        'id': 1,
        "email": 'Allah',
        'role': 'admin',
        "password": '123'
    },
    {
        'id': 2,
        'email': 'Jesus',
        'role': 'client',
        'password': 'TheBestPasswordOfEver'
    }
]


class UserService:
    def __init__(self, user_data: list[dict]) -> None:
        self.user_data = user_data

    def get_users(self) -> list[User]:
        items = []
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        for item in data["all_users"]:
            items.append(
                User(
                    id=item['id'],
                    email=item['email'],
                    username=item['username']
                )
            )
        return items

    def update_user(self, payload: UserRestore): # -> User:
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        # Check if user already exists
        flag = 0
        for item in data["all_users"]:
            if item["email"] == payload.email:
                flag += 1
        if flag != 1:
            raise HTTPException(status_code=400, detail="The email was entered incorrectly")

        if payload.password != payload.password2:
            raise HTTPException(status_code=400, detail="The password was entered incorrectly")

        for item in data["all_users"]:
            if item["email"] == payload.email:
                item['password'] = payload.password
                #print(payload.password)
            with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
                json.dump(data, f, indent=2)

                return {'status': 200, 'info': 'User upd successfully'}#User(name=data["name"],id=data["id"])#Вот так делать pydentic schema

        raise HTTPException(status_code=400, detail="User is not found")

    def register_user(self, payload: UserCreate):# -> User or str:
        new_user = {
            "id": randint(3, 500),
            "email": payload.email,
            "username": payload.username,
            "role": "client",
            "password": payload.password2,
        }
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            users = json.load(f)
        # Check if user already exists

        for item in users["all_users"]:
            if item["email"] == payload.email:
                raise HTTPException(status_code=400, detail="You are already registered")
        for item in users["all_users"]:
            while item["id"] == new_user["id"]:
                new_user["id"] = randint(10,500)

        if payload.password != payload.password2:
            raise HTTPException(status_code=400, detail="The password was entered incorrectly")

        users["all_users"].append(new_user)
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
            json.dump(users, f, indent=2)

        return User(id = new_user["id"],
                    email= payload.email,
        username= payload.username)#{"message": "User registered successfully"}

    def auth(self, credentials: Credentials) -> User :
        with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
            data = json.load(f)
        flag = 0
        for item in data["all_users"]:
            if item['email'] == credentials.email and item['password'] == credentials.password:
                flag = 0
                return User(id=item["id"], email=item["email"], username= item["username"])#{"message": "User auth successfully"}#
            else:
                flag = 1
        if flag:
            raise HTTPException(status_code=400, detail="You are not registered")




user_service: UserService = UserService(user_data)


#def get_users(self) -> list[User]:
# items = []
# for item in self.user_data:
#     items.append(
#         User(
#             id=item['id'],
#             email=item['email']
#         )
#     )
# return items

#def update_user(self, id: int, payload: UserUpdate): # -> User:
# for item in self.user_data:
        #     if item["id"] == id:
        #         item['email'] = payload.email
        #
        #         return User(
        #             id=item["id"],
        #             email=item["email"]
        #         )
        # return User(
        #     id=item["id"],
        #     email=item["email"])

#def register_user(self, payload: UserCreate):# -> User or str:
# for user in self.user_data:
        #     if user["email"] == payload.email:
        #         raise ValueError("You are already registered")
        # return user_data.append(user) #payload.dict() ??maybe self
        # Add the new user to the JSON file
        # else:
        #     self.user_data.append(User(
        #         id=new_user["id"],
        #         email=new_user["email"],
        #         password=new_user["password"]).dict())
        #     return User(
        #         id=new_user["id"],
        #         email=new_user["email"],
        #         password=new_user["password"])#.dict()
        # self.user_data.append(

# works properly
# def update_user(self, id: int, payload: UserUpdate):  # -> User:
#     if auth_user := self._auth(payload.auth):  # сразу записываем в переменную ауф значение из полученное в ифе
#         if auth_user.id != id:
#             raise ValueError("Id is uncorrected")
#
#         with open("D:\PycharmProjects\MyMultitasker\services\data.json", "r") as f:
#             data = json.load(f)
#
#         for item in data["all_users"]:
#             if item["id"] == id:
#                 item['email'] = payload.email
#
#             with open("D:\PycharmProjects\MyMultitasker\services\data.json", "w") as f:
#                 json.dump(data, f)
#
#                 return {"message": "User email updated successfully"}  # data["all_users"]
#
#     raise HTTPException(status_code=400, detail="User is not found")

#Ctrl+Alt+Shift+L