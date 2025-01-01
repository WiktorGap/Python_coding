import psycopg2
from Schema import User, GroupOfProducts, Product
class variabilityBase:
    def __init__(self):
        self.newbase = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",  password="thinkpad", port=5432)#create new base object using module connection_with_base
    def create_table(self, name):
        cur=self.newbase.cursor()
        cur.execute("""CREATE TABLE users (id int, login VARCHAR, address VARCHAR, email VARCHAR, phone_number VARCHAR, is_verified VARCHAR);""")
        self.newbase.commit()
        cur.close()
    def add_product(self, user: User):
        cur = self.newbase.cursor()
        cur.execute(f"""INSERT INTO users (id, login, address, email, phone_number, is_verified) VALUES (%s, %s, %s, %s, %s, %s);""", (user.id, user.login, user.address, user.email, user.phone_number, user.is_verified))
        self.newbase.commit()
        cur.close()
        
    def del_product(self, name_product, table_name):
        cur = self.newbase.cursor()
        cur.execute("""DELETE from productsss WHERE name ="d" """)
        self.newbase.commit()
        cur.close()
        
    def display_data(self): #funkcja ktora pyta ile uzytkownik chce wyswietlic wierszy z tabeli, zabezpieczenie przed wprowadzeniem np stringa zamiast inta
        try:
            amount=int(input("How much rows do you want to display? (integer amount)"))
        except ValueError:
            print("Unfortunatly, I don't think it's a number")
        cur = self.newbase.cursor()
        cur.execute("""SELECT * from productsss""")
        rows=cur.fetchmany(size = amount)
        if len(rows) == 0: # ta linijka moze poinformowac uzytkownika ze nie ma tak duzo wierszy w tabeli, przyrownalem dlugosc rows do 0 bo jak sie da za duza liczba w fetchmany to zwraca pusta liste
            return "oh no, Database doesn't have that many records"
        print(rows)
        self.newbase.commit()
        cur.close()
        
smt=variabilityBase()
data={"id":"1", "login":"adminn", "address":"czekoladowa", "email":"cogmailcom", "phone_number":"dsad", "is_verified":"True"}


new_user=User(id="1243", login="example", address="czekoladowa", email="cos.com", phone_number="123456789", is_verified="True")
smt.add_product(new_user)



        


