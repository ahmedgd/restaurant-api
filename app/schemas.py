from pydantic import BaseModel

#  User class
class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }


# MenuItem class

class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    image_url: str | None = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemRead(MenuItemBase):
    id: int

    model_config = {
        "from_attributes": True
    }
