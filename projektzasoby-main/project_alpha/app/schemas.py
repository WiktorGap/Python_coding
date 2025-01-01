from pydantic import BaseModel

class User(BaseModel):
    id :  int
    login : str
    address : str
    email : str
    phone_number : str
    is_verified : bool
    class Config:
        orm_mode = True 

class GroupOfProducts(BaseModel):
    id : int
    name_of_group : str
    description : str
    owner_id  : int
    class Config:
        orm_mode = True 


class Product(BaseModel):
    name  : str
    label : str
    price : int
    quantity : int
    description : str
    class Config:
        orm_mode = True
    

