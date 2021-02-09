import xml.etree.ElementTree as ET # as es para establecer un alias

datos = '''
<person>
    <name>Ander</name>
    <phone type="smart">+3466666666</phone>
    <email hide="no">email@email.com</email>
</person>
'''
# Se usa try para comprobar que si hay errores en el XML
try:
    tree = ET.fromstring(datos)
    print("### Reading String XML ###")
    print("Nombre:", tree.find("name").text)
    print("Email:", tree.find("email").text, "\nAtributo:", tree.find("email").attrib)
except Exception as e:
    print(e)

# Si se lee un archivo xml
try:
    newTree = ET.parse(".\\xml-py\\data.xml")
    root = newTree.getroot()

    print("\n### Reading from XML file ###")
    #print("Nombre:", root.find("person").find("name").text) # Dos formas de extraer info del nodo deseado
    print("Nombre:", root.find("person/name").text)
    print("Email:", root.find("person").find("email").text, "\nAtributo:", root.find("person/email").attrib)

    lista = list()

    for person in root:
        lista.append(person)

    print(len(lista))
    for item in lista:
        print(" \n***********\n")
        print(item.find("name").text)
        print(item.find("phone").text)
        print(item.find("email").text)

except Exception as e:
    print(e)

