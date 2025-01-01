from fastapi import FastAPI, Response , status , HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi.params import Body 

app = FastAPI()

class Post(BaseModel):
    phone_number: str
    name: str
    last_name: str
    loyalty_card: Optional[bool] = False
    id = randrange(0, 10000000)


def find_post(id):
    for p in my_posts:
            if p ['id'] == id:
                return p 
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i 





my_posts = [{"phone_numbe":"123456790", "name":"CHuj", "last_name":"ChujCHUj","verified":"True", "loyalty_card":"False", "id": 1}, {"phone_numbe":"190", "name":"Cj", "last_name":"CjCHUj","verified":"True", "loyalty_card":"False" , "id":2}]

@app.get("/")
async def root():
    return {"message": "Hello, world"}

@app.get("/post/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")




@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} was not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)





@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id 
    my_posts[index] = post_dict
    return {"data" : post_dict}




