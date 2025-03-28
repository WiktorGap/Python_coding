from abc import ABC , abstractmethod
from datetime import datetime
import sqlite3
import time
#abstract class
class TextLines:

    @abstractmethod
    def getNumberOfLines(self):
        pass
    
    @abstractmethod
    def readLine(self,line_number):
        pass


    @abstractmethod
    def deleteLine(self,line_number):
        pass


    @abstractmethod
    def writeLine(self,text,line_number = None):
        pass
    #@abstractmethod
    """"
    def writeLine(self,text,line_number = None):
        if line_number is None:
            self.__writeLineAtEnd(text)
        else:
            self.__writeLineAtIdx(text,line_number)


    #BEGIN: Private Methods
    @abstractmethod
    def __writeLineAtEnd(self,text):
        pass
ow().strftimr('%Y%m%d%H$M%S')
    @abstractmethod
    def __writeLineAtIdx(self,text,line_number):
        pass
    """
    



class TextLinesInDB(TextLines):

    def __init__(self,db_name=None):
        if db_name is None:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            self.__db_name = f"data_{timestamp}.db"
        else:
            self.__db_name = db_name

        con = sqlite3.connect(self.__db_name)

        with open("db.sql") as script:
            con.executescript(script.read())

        con.commit()
        con.close()
        self.__con = None 
        self.__cur = None


    def getNumberOfLines(self):
        sql = "SELECT COUNT(*) AS count FROM LINES"

        con = self.__getCon()

        con.row_factory = sqlite3.Row #odwołanie sie nie za pomocą inedxów a zapomocą nazw kolumn
        cur = con.cursor()
        res = cur.execute(sql)
        row = res.fetchone()
        row = dict(row)
        #con.close()
        return row['count']
    

    def readLine(self,line_number):
        if(line_number <= self.getNumberOfLines()):
            
     
            sql = "SELECT * FROM lines WHERE id=(?)"

            con = sqlite3.connect(self.__db_name)
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            res = cur.execute(sql,(line_number,))
            row = res.fetchone()
            row = dict(row)
            #print(row)
            #con.close()
            return row['line']
        else:
            raise IndexError("list index our of range")
        
        #    if(line_number<len(self.__lines)):
        #    return self.__lines[line_number]
        
        

    def deleteLine(self, line_number):
        if(line_number>=0 and line_number<self.getNumberOfLines()):
            self.__writeLineAtIdx("",line_number)
        else:
            raise IndexError("list index our of range")


    def writeLine(self,text,line_number = None):
        if line_number is None:
            self.__writeLineAtEnd(text)
        else:
            self.__writeLineAtIdx(text,line_number)

    def __getCon(self):
        if self.__con is None:
            self.__con = sqlite3.connect(self.__db_name)
        return self.__con 

    def __writeLineAtEnd(self, text):
        if type(text) is not str:
            raise TypeError("Text must be a string type ")
        
        sql = "INSERT INTO lines(line) VALUES (?)"

        con = self.__getCon()
        cur = con.cursor()
        res = cur.execute(sql,(text,))
        con.commit()
        #con.close()


    #Conservative variant
    """"
    def __writeLineAtIdx(self,text,line_number):
        if type(text) is not str:
            raise TypeError("Text must be a string type ")
        elif(line_number>=0 and line_number<self.getNumberOfLines()):
            self.__lines[line_number]=text
        else:
            raise IndexError("list index our of range")
    """
    #Progressive varint
    def __writeLineAtIdx(self,text,line_number):
        if type(text) is not str:
            raise TypeError("Text must be a string type ")
        elif line_number>=0 and line_number<self.getNumberOfLines():
                sql = "UPDATE lines SET line =(?),modiffied=CURRENT_TIMESTAMP WHERE id =?"

                con = self.__getCon()
                cur = con.cursor()
                res = cur.execute(sql,(text,line_number))
                con.commit()
                #con.close()

        else:
            for _ in range(1,line_number-self.getNumberOfLines()):
                self.__writeLineAtEnd("")
            self.__writeLineAtEnd(text)

    def dump(self):
        sql = "SELECT * FROM lines "

        con = self.__getCon()
        cur = con.cursor()
        res = cur.execute(sql)
        rows = res.fetchall()
        for row in rows:
            print(dict(row))
        #print(row)
        #con.close()

    def closeDB(self):
        self.__con.close()
        self.__con = None




class IndentifiedTextLines:
    def __init__(self):
        self.__lines = TextLinesInDB()
        self.__ids={}

    def get_identifiers(self):
        return [key for key in self.__ids]

    def write_line(self,text,identifier):
        if identifier not in self.__ids:
            self.__ids[identifier] = []
        self.__lines.writeLine(text)
        line_number = self.__lines.getNumberOfLines() - 1
        self.__ids[identifier].append((line_number))
    

    def read_line(self,identifier):
        if identifier not in self.__ids:
            raise KeyError("Unknown identifier")
        
        result = []

        for idx in self.__ids[identifier]:
            line = self.__lines.readLine(idx)
            result.append(line)
        return result 


    def test(self):
        print(self.__ids)

    def deleteLine(self,identifier):
        if identifier not in self.__ids:
            raise KeyError("Unknown iderifier")
        
        for idx in self.__ids[identifier]:
            self.__lines.deleteLine(idx)
        
        del self.__ids[identifier]


    # def find_free_idx(self):
    #     number_of_lines = selfrom abc import ABC , abstractmethod

def test_IndentifiedTextLines():
    titl = IndentifiedTextLines()
    titl.write_line("foo 1","f1")
    titl.write_line("bar 1","b1")
    titl.write_line("foo 2","f1")
    titl.write_line("bar 2","b1")
    titl.write_line("foo 3","f1")
    print(titl.get_identifiers())
    lines = titl.read_line("f1")
    for l in lines:
        print(l)
    titl.deleteLine("f1")
    print(titl.get_identifiers())
    titl.dump()
    titl.find_free_idx()

    


def test_TextLinesInDB():
    tlid = TextLinesInDB("line_set.db")
    line_number = tlid.getNumberOfLines()
    print(line_number)
    tlid.writeLine("test text 1")
    tlid.writeLine("test text 2")
    tlid.writeLine("test text 3")
    line_number = tlid.getNumberOfLines()
    print(line_number)
    line = tlid.readLine(2)
    print(line)
    tlid.closeDB()
    #time.sleep(5)
    tlid.writeLine("mod 2",2)
    line = tlid.readLine(2)
    print(line)
    tlid.writeLine("line",7)
    line = tlid.readLine(7)
    print(line)
    tlid.deleteLine(2)
    line = tlid.readLine(2)
    print(f"line 2 : {line}")
    tlid.dump()


def main():
    test_TextLinesInDB()

if __name__ == "__main__":
    main()



def test_TextLinesInDB():
    tlid = TextLinesInDB("line_set.db")
    line_number = tlid.getNumberOfLines()
    print(line_number)
    tlid.writeLine("test text 1")
    tlid.writeLine("test text 2")
    tlid.writeLine("test text 3")
    line_number = tlid.getNumberOfLines()
    print(line_number)
    line = tlid.readLine(2)
    print(line)
    tlid.closeDB()
    #time.sleep(5)
    tlid.writeLine("mod 2",2)
    line = tlid.readLine(2)
    print(line)
    tlid.writeLine("line",7)
    line = tlid.readLine(7)
    print(line)
    tlid.deleteLine(2)
    line = tlid.readLine(2)
    print(f"line 2 : {line}")
    tlid.dump()

