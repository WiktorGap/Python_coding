from pydantic import BaseModel

class User(BaseModel):
    id :  str
    login : str
    address : str
    email : str
    phone_number : str
    is_verified : str
    class Config:
        from_attributes = True

class GroupOfProducts(BaseModel):
    id : int
    name_of_group : str
    description : str
    owner_id  : int
    class Config:
        from_attributes = True 


class Product(BaseModel):
    name  : str
    label : str
    price : int
    quantity : int
    description : str
    class Config:
        from_attributes = True
    

