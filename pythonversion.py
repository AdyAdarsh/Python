import os

path = "C:/Users/Hp/OneDrive/Desktop/OS.txt"  


def file_exists(): 
    print(os.access(path, os.F_OK))


def file_read():
    print(os.access(path, os.R_OK))


def file_write():  
    print(os.access(path, os.W_OK))


def path_execution():  
    print(os.access(path, os.X_OK))


# Gives boolean value as Output
file_write()
file_read()
file_exists()
path_execution()
