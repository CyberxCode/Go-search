#! usr/bin/python
import os
class Search_File():
    def __File__(self,directory,name):
        self.directory_=directory
        var = ("find {} -name {}").format(self.directory_,name)
        os.system(var) 
    def __User__(self,directory,usr):
        self.directory_=directory
        var = ("find {} -user {}").format(self.directory_,usr)
        os.system(var)
    def __Type__(self,directory,type_):
        self.directory_=directory
        var = ("find {} -name \*{}").format(self.directory_,type_)
        os.system(var)
    def __Binary__(self,directory,day):
        self.directory_=directory
        var = ("find {} -type f -atime +{}").format(self.directory_,day)
        os.system(var)
    def __Days__(self,directory,day):
        self.directory_=directory
        var = ("find {} -type f -mtime -{}").format(self.directory_,day)
        os.system(var)
while True:
    Function = Search_File()
    print("""

         [*]=====================================[*]
         ||              Go Search                ||
         ||     Script Search within Linux        ||
         ||   system quickly and effectively      ||
         [*]=====================================[*]
         ||           By : CyberCode              ||
         [*]=====================================[*]
      
1) Find file or folder
2) Find files or folders belonging to user
3) Find files by extension (.jpg.png.MP3)
4) Find binary files By usage time (in days)
5) Find files created or modified in previous days
6) Exit
0) Help

==> Enter number of search process you want (e.g., 1 2 3 or 1-3)
==> ----------------------------------------------------------
 """)
    try:
        cmd=int(input("==> "))
        if cmd in range(0,7):
            break
    except ValueError:
        print("Error try again :/")
try:
    if cmd == 1:
        File=Search_File()
        val1 = input("Enter path of file you want to search: ")
        val2 = input("Enter file name: ")
        File.__File__(val1,val2)
    elif cmd == 2:
        User=Search_File()
        val1 = input("Enter path of file you want to search: ")
        val2 = input("Enter user name: ")
        User.__User__(val1,val2)
    elif cmd == 3:
        Type=Search_File()
        val1 = input("Enter path of file you want to search: ")
        val2 = input("Enter extension file ex..(.png): ")
        Type.__Type__(val1,val2)
    elif cmd == 4:
        Binary=Search_File()
        val1 = input("Enter path of file you want to search: ")
        val2 = input("Enter number of days ex..(365): ")
        Binary.__Binary__(val1,val2)
    elif cmd == 5:
        Days=Search_File()
        val1 = input("Enter path of file you want to search: ")
        val2 = input("Enter number of days ex..(365): ")
        Days.__Days__(val1,val2)
    elif cmd == 6:
        os.system("exit")
    elif cmd == 0:
        help_file=open('help.txt',"r")
        for line in help_file :
            print(line)
        help_file.close
        
            
except Exception :
    print("Failed program :/")
    

    
    
    
    

