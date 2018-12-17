lista=[]
for k in range(10):
    lista.append(input("introduce valor en lista: "))

print("los elementos de la lista son: "+str(lista))
valor=int(input("introduce el valor a modificar de la lista por el indice:"))
nuevo=input("introduce el nuevo valor:")
lista[valor] = nuevo 
print("los elementos de la lista son:"+str(lista))
valor=int(input("introduce el índice en el que se insertará el nuevo valor:"))
nuevo=input("introduce el nuevo valor:")
lista.insert(valor,nuevo)
print("los elementos de la lista son: "+str(lista))
nuevo=input("introduce el valor a eliminar:")
lista.remove(nuevo)
print("los elementos de la lista son: "+str(lista))
