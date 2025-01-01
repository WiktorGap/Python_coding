from fastapi import FastAPI , Response , status , HTTPException , Depends
import psycopg2
import time
from pydantic import BaseModel
#from random import randrange  chce zrobic ze jak tworzymy przypisuje losowe id do naszych danych zebysmy potem mogeli na podstawie tego robic cos na tych danych 
from . import funcs
from .database import engine , SessionLocal
from funcs import variabilityBase
from sqlalchemy.orm import Session
from .schemas import User, GroupOfProducts ,Product
from . import table_models , schemas


#program ma błedy , nie dokonczylem ale mniej wiecej w ten sposb musi to tak wygladac tak samo jak reszta plików w nim zawartych , wystarczy takie cos pozniej wrzucuc na masyzne virtualna jak bedzie zrobione
#zmienilem nazawe main2 na funcs.py 
#w funcs pozmienilabym w troche nazwy obiektów i niektórych instancji bo ciezko mi sie implementuje szczegolnie przez new_base
#generalnie funkcje w nim wydaja mi sie spoko nie testowalem nic bo dlugo mi zeszlo na sklejeniu miej wiecej zeby miec zarys do czego dazyc 
#ale fajnie je mozna wykorzystac w tym głownym pliku ułatwia i skraca kod takze tam tez cos trzeba podziałać 


table_models.Base.metadata.create_all(bind=engine) #potrzebne do wygenerowania modelmów pydantic




app = FastAPI()
func_base = variabilityBase()
#potrzebne do stworzenia sesji naszej bazy 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#połaczenie z baza danych potrzebne
def make_conection():

    while True:

        try:
            conn = psycopg2.connect(host = 'localhost', database='fastapi', 
                                    user='postgres', 
                                    password='111111111', 
                                    )
            cursor = conn.cursor()
            print("Database connection was succesfull")
            break
        except Exception as error:
            print("Connection failed")
            print("Error: ", error)
            time.sleep(2)




def create_table():
    if make_conection():
        func_base.base_model()
    else:
        print("Conection was failed try smth else")
@app.get("/display", db = SessionLocal(get_db()) , status_code= status.HTTP_204_NO_CONTENT)
def display_table():
    if create_table():
        func_base.display_data() #nie wiem czemu nie czyta instancji 
    else:
        print("Connection error")


@app.delete("/delete/{id}", db = SessionLocal(get_db()) status_code=status.HTTP_204_NO_CONTENT)
def delete_data(id: int):
    func_base.del_product()

    if delete_data ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#generlanie wyglada na to ze do kazdej tabeli bedze potrzebna inna funkcja po nazwy danych sie różnią , zapewne w przypadku reszty tez
@app.put('/data/{id}' , db = SessionLocal(get_db())) #status_code=status.HTTP  nie wiem jaki status informuje o zakuralizowaniu
def update_table_users(id:int , data: User):
    func_base.update_post(data.id,data.login, data.address , data.phone_number , data.is_verified, str(id)) #id jest zmienanie z int na str żeby JSON mógł bez przeszkud skonwertowac nasze zapytanie przez ORM w API
    updated_user = variabilityBase.fetch_one_cur


    if updated_user  == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return{"updated_user"}



         

    