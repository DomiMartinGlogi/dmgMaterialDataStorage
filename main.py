#Created by DomiMartinGlogi
#E-Mail:

import json
from pathlib import Path

#Todo:
#Menu System
#Material Data and Storage places
    #Material Movements
    #Material Properties(LOT Number, Type, Colour)
    #Data for total Amounts, reserve Material for uses
#GUI

mainDatabase = { }

def menu():
    print("Menu:")
    print("1 : Save current Session")
    print("2 : Define new Material")
    print("3 : Search for Material")
    print("4 : Check Material Data")
    rawIn = input("Selection: ")
    intIn = int(rawIn)
    #Implement all Menu items here!
    if intIn == 1:
        save()
    elif intIn == 2:
        newMat()
    elif intIn == 3:
        searchMat()
    elif intIn == 4:
        checkMat()
    else:
        print("Invalid Input!")
        menu()

def save():
    Data = mainDatabase
    file = open("Material.json", "w")
    json.dump(Data, file, indent=1)
    file.flush()
    file.close()
    menu()

def searchMat():
    SearchKey = input("Search for: ")
    Result = dict(filter(lambda item: SearchKey in item[0], mainDatabase.items()))
    print("Results: " + str(Result))
    menu()

def checkMat():
    material = input("Name: ")
    if not material in mainDatabase:
        print("Material not in Database!")
        menu()
    file = mainDatabase[material]["File"]
    file = open(file , "r")
    subdict = json.load(file)
    print(subdict)
    menu()

def newMat():
    name = input("Name: ")
    matType = input("Material Type: ")
    lotNr = int(input("LotNr: "))
    amount = int(input("Amount in kg: "))
    colour = input("Colour: ")
    newFileName = "materials/" + name + ".json"
    mainDatabase[name] = {"File" : newFileName}
    newDB = {"Type" : matType , "LotNr" : lotNr , "Colour" : colour , "Amount" : amount}
    file = open(newFileName , "w")
    json.dump(newDB, file, indent=1)
    file.flush()
    file.close()
    menu()

file2load = Path("Material.json")
if file2load.exists() :
    with open("Material.json") as database:
        mainDatabase = json.load(database)
print("Welcome to dmgMaterialData&Storage!")
menu()