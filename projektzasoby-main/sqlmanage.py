from connection_with_base import Connection

#w naszej bazie danych musimy uwzglednic kolumne id 
#potrzebna funkcja która bedzue czytac baze danych)
#funkcja fetch data
#update data
#funkcja do aktualizowania 

# pisze ta klase poniewaz bedzie mogli podpiac to wszystko pod API i zamiast sie meczyc mamy gotowy moduł odpowiedzialny za konkretne operacje


# musze jeszcze ogarnac jak stworzyc baze danych i modele (już cos mam ale raczej w dzis/piatek to wrzuca)

#WAŻNE nie za działa bo chciałbym zrobic tak zeby zmienna database była funkcja z innego pliku albo instancja jakies klasy 
#gdzie bedzie sprawdzac czy baza danych istnieje 
#jesli tak to dalej bedzoe mozliwe wykonywanie check_data jesli nie to wyswietli odpowiedni komunkiat
#widzialem ze cos podobnego pisales ale musze sie temu dokladniej przyjzec


def check_data(data, id , database):
        if data['id'] == id:    
            for data in database:
                return data
        else:
            print(f"Data with id {id} doesn't exists")





class Manage_data():
    def __init__(self, injection):
        injection = Connection.make_cursor()
        self.injection = injection
    def add_data(self):
        if not check_data():
            func = """INSERT INTO productsss (a,b,c,d) VALUES (%s, %s, %s, %s);""" #VALUES (%s, %s, %s, %s) to dobra praktyka te nasze s prametruzyje dane, chronimy sie dzieki temu przed atakiem SQLinjection
            exec = Connection.execute_sth(self.injection, func)
            return exec , print("Params was added to database succsefully")
    def delete_dataself(self, id):
         delete = f""" DELETE FROM productss (a,b,c,d) WHERE id = {id} """
         exec = Connection.execute_sth(self.injection, delete)
         return exec , print("Data was delete")


nb=Manage_data("k")
nb.add_data()




         
    



