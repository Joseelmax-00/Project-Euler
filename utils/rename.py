import os


for file in os.listdir():
    if "problema" in file:
        numero = file.replace("problema","").replace(".py", "")
        while len(numero) < 3:
            numero = "0" + numero
        os.rename(file, "problema" + numero + ".py")
    
    if "vars" in file:
        numero = file.replace("vars" , "").replace(".txt", "")
        while len(numero) < 3:
            numero = "0" + numero
        os.rename(file, "vars" + numero + ".txt")