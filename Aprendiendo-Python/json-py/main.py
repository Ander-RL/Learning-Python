import json

data = """
{
  "name": "Chuck",
  "phone": {
    "type": "smart",
    "number": "+1 123 123 123 132"
  },
  "email": {
    "hide": "yes"
  }
}
"""
# Cargamos el string (loads = load string)
# jsonData = json.loads(data)

# Cargamos la info desde un archivo
file = open("data.json")
jsonData = json.load(file)

print(jsonData)
print(jsonData["name"])
print(jsonData["phone"]["type"])

print("***")

for element in jsonData: print(element)
