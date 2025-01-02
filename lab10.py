import sys
import io
import time 


buffer = io.StringIO()

file_path = '/home/u335867/tesktowy.txt'

def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            print("File was read succesfully")
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found ")
        return 0
    

def read_file_to_buffer(content,buffer):
    if content:
        for i in range(101):
            buffer.write(content)
            val = (buffer.getvalue())
            print("Progress: {i}% ", end="\r")
            time.sleep(.1)

##def type_argv():
##    if(sys.argv[])

if __name__ == "__main__":
    try:
        if len(sys.argv)>1:
            file_path = sys.argv[1]
    except ValueError as exp :
        print("Error: ", exp)

    file_read = read_file(file_path)
    if file_read:
        read_file_to_buffer(file_read,buffer)

    buffer.seek(0)
    print("Buffer content: \n")
    print(buffer.read())