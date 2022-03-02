from pydantic import BaseModel, Field


class User(BaseModel):
    login: str
    age: int = Field(alias="user_age", default=20)


user = {
    "login": "asdas"
}


u = User(**user)
print(u.dict(by_alias=True))
