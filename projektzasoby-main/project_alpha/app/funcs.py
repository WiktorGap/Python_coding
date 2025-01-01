import psycopg2
class variabilityBase:
    def __init__(self):
        self.newbase = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",  password="thinkpad", port=5432)#create new base object using module connection_with_base
    def fetch_one_cur(self):
        cur = self.newbase.cursor()
        return cur.fetchone()

    def base_model(self,col1,col2,col3,col4):
        if not col1.isdigit():
            return "ID MUST BE AN INTEGER"
        cur = self.newbase.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS productsss({col1} VARCHAR, {col2} VARCHAR, {col3} VARCHAR, {col4} VARCHAR);""")
        self.newbase.commit()
        cur.close()

    def update_post(self,val1 : int,val2: str,val3: str, val4 : int, val5: bool):
        cur = self.newbase.cursor()
        cur.execute("""UPDATE users SET id = %s, login= %s , address = %s , email  = %s , phone_number = %s , is_verified = %s  WHERE id = %s RETURNING * """, 
                    ({val1},{val2},{val3}, {val4}, {val5})
        updated_post = cur.fetchone()
        cur.commit()
        
    def add_product(self, features: set,table_name):
        cur = self.newbase.cursor()

        cur.execute(f"""INSERT INTO productsss (name,b,c,d) VALUES {features};""")
        self.newbase.commit()
        cur.close()
    def del_product(self, name_product, table_name):
        cur = self.newbase.cursor()
        cur.execute("""DELETE from productsss WHERE name ="dupa" """)
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
        # Tez nie wiem czy na koncu zawsze musi byc cur.close() newbase.close() niby pisza ze musi byc pewnie dla bezpieczenstwa ale nie wiem




smt=variabilityBase()
print(smt)
smt.base_model("name","b","c","d")
smt.add_product(("dupfddsa","dddsd","dsds","ffd"),"products")

smt.display_data()