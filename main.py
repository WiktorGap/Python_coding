from abc import ABC , abstractmethod

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

    @abstractmethod
    def __writeLineAtIdx(self,text,line_number):
        pass
    """
    



class TextLinesInMemory(TextLines):

    def __init__(self):
        self.__lines = []



    def getNumberOfLines(self):
        return len(self.__lines)
    

    def readLine(self,line_number):
        if(line_number<self.getNumberOfLines()):
            return self.__lines[line_number]
        else:
            raise IndexError("list index our of range")
        
        #    if(line_number<len(self.__lines)):
        #    return self.__lines[line_number]
        
        

    def deleteLine(self, line_number):
        if(line_number>=0 and line_number<self.getNumberOfLines()):
            self.__lines[line_number]=""
        else:
            raise IndexError("list index our of range")


    def writeLine(self,text,line_number = None):
        if line_number is None:
            self.__writeLineAtEnd(text)
        else:
            self.__writeLineAtIdx(text,line_number)


    def __writeLineAtEnd(self, text):
        if type(text) is not str:
            raise TypeError("Text must be a string type ")
        self.__lines.append(text)


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
            self.__lines[line_number]=text
        else:
            for _ in range(line_number-self.getNumberOfLines()):
                self.__writeLineAtEnd("")
            self.__writeLineAtEnd(text)

    def dump(self):
        print(self.__lines)




class IndentifiedTextLines:
    def __init__(self):
        self.__lines = TextLinesInMemory()
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


    def find_free_idx(self):
        number_of_lines = self.__lines.getNumberOfLines()
        print(number_of_lines)
        seq = [n for n in range(number_of_lines)]
        print(seq)
        for key in self.__ids:
            print(f"Identifier: {key}")
            for idx in self.__ids[key]:
                print(idx)
                seq.remove(idx)

        print(seq)
        if len(seq)>0:
            print(f"Use index {seq[0]}")
        else:
            print(f"Use without index(append)")

    def dump(self):
        self.__lines.dump()

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

    


def test_TextLinesInMemory():
    tlim = TextLinesInMemory()
    line_number = tlim.getNumberOfLines()
    print(line_number)
    tlim.writeLine("test text")
    line_number = tlim.getNumberOfLines()
    print(line_number)
    tlim.writeLine("foo bar",5)
    line_number = tlim.getNumberOfLines()
    print(line_number)
    tlim.writeLine("baz bar",2)
    line_number = tlim.getNumberOfLines()
    print(line_number)
    line = line_number = tlim.readLine(2)
    print(line)
    tlim.deleteLine(2)
    line_number = tlim.getNumberOfLines()
    print(line_number)
    line = tlim.readLine(2)
    print(line)

    try:
        line = tlim.readLine(20)
        print(line)
    except IndexError:
        print("Bad index")






def main():
    #test_TextLinesInMemory()
    test_IndentifiedTextLines()

if __name__ == "__main__":
    main()
