import os
import string

with open(r"C:\Users\Admin\Desktop\pp2\dif-and-files\sometext.txt", "r", encoding="utf-8") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()