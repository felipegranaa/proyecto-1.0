import random 
elementos = "+-/*!&$#?=@abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lon = int(input("longitud de la contrasenas "))
pasworld = ""
for i in range(lon):
    pasworld += random.choice(elementos)

print (pasworld)