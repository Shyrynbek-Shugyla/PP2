import re 


with open(r"D:\PP2\labs\lab5\8-9-10.txt", encoding="utf-8") as f:
    data = f.read()
    
print("Task 8")

print(re.findall(r"[A-Z][^A-Z]*", data))

#букыл матындерды келесы келесы улкен арыптерге дейын алады символдары коса: , . 