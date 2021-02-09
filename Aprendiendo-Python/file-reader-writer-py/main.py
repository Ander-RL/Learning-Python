file = open("file-reader-writer-py/MyFile.txt")

lines = file.readlines()

# Nueva lista en la que guardar los cambios
nLines = list()

# Recorre la lista y reemplaza \n (nueva linea) por "" vacio
for line in lines:
    if "\n" in line:
        nLines.append(line.replace("\n", ""))

# Recorre la lista y elimina las posiciones con espacios vacios
for line in nLines:
    if line == "": nLines.remove(line)

for line in nLines: print(line)
print("\n==================================\n")

# Se crea lista vacia
wordList = list()

for line in nLines:
    wordList += line.split()

print(wordList)
print("\n==================================\n")

# Se crea diccionario vacio
di = dict()
# Letra a letra la añade al diccionario y
# cuenta cuantas veces aparece
for word in wordList:
    if word in di:
        di[word] = di[word] + 1
    else:
        di[word] = 1

print(di)
print("\n==================================\n")

maxWords = list()
valueList = list()
uniqueWords = dict()
maxVal = 0
# Extrae el valor más alto del diccionario y
# añade las claves únicas y su valor al 
# diccionario 'uniqueWords'
# Añade valores únicos a lista
for element in di:
    if di[element] > maxVal: maxVal = di[element]
    if di[element] not in uniqueWords: uniqueWords[element] = di[element]
    if di[element] not in valueList: valueList.append(di[element])

# Añade a la lista las claves con valor igual a maxVal
for element in di:
    if di[element] == maxVal: maxWords.append(element)


print("\nPalabras únicas:\n", uniqueWords)
print("\n==================================\n")
print("\nVeces que se repite cada palabra:\n", valueList)
print("\n==================================\n")
print("\nPalabra(s) más recurrente(s):\n", maxWords)
print("\nAparece(n)", maxVal,"veces.")
print("\n==================================\n")

# The 'with' statement clarifies code that previously 
# would use 'try...finally' blocks to ensure that 
# clean-up code is executed.
#with open("file-reader-writer-py/MyFile.txt", "a") as F: # 'a' Appends text at the end
#   F.writelines("\n\n*** Appended Lines ***")

#with open("file-reader-writer-py/MyFile.txt", "w") as F:
#    F.write("New text") # Deletes everything and writes new text
