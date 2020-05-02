'''
Created on Feb 29, 2020

@author: ITAUser
'''
#readnwrite mod mane
from _io import StringIO

#basic concepts
#open file open()

file1="filename.txt","mode"

#mode r: read, w:write a:append r+:special case read and write

#read- read(), readline() -stores value as a string
#write- write()

#create a new file
    file1=open("hello.txt", "a")
    file1.close
    
#write to the file
    string="jello my name is leo"
    file1.write(String)

#write multiple lines
    line = ["dogs"  , "are", "cool"]
    file1.writeLine(line)  
                
#read file
    file1.open("hello.txt", "r")
    text=file1.read()
    file1.close
    
    print(text)