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

# Function menu() is literally just a menu, sadly using if, elif and else statements
def menu():
    print("Menu:")
    print("1 : Save current Session")
    print("2 : Define new Material")
    print("3 : Search for Material")
    print("4 : Check Material Data")
    print("5 : Reserve Material")
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
    elif intIn == 5:
        reserveMat()
    else:
        print("Invalid Input!")
        menu()

# Function save() saves the mainDatabase dict to Material.json
def save():
    Data = mainDatabase
    file = open("Material.json", "w")
    json.dump(Data, file, indent = 1)
    file.flush()
    file.close()
    menu()

# Function searchMat() looks for a given substring within mainDatabase dict and prints out all appropriate results.
def searchMat():
    SearchKey = input("Search for: ")
    Result = dict(filter(lambda item: SearchKey in item[0], mainDatabase.items()))
    print("Results: " + str(Result))
    menu()

# Function checkMat() looks up a material and prints all the lotNr dicts availables.
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

# Function newMat() sets up new Materials, both totally new types and already existing types with new LotNrs, saves them
# in the appropriate dictionary file
def newMat():
    name = input("Name: ")
    matType = input("Material Type: ")
    lotNr = int(input("LotNr: "))
    amount = int(input("Amount in kg: "))
    colour = input("Colour: ")
    if not name in mainDatabase:
        newFileName = "materials/" + name + ".json"
        mainDatabase[name] = {"File": newFileName}
        matDB = {}
        matDB[lotNr] = {"Type": matType, "Colour": colour, "AmountAvailable": amount, "AmountReserved": "0", "TotalAmount": amount}
        file = open(newFileName, "w")
        json.dump(matDB, file, indent = 1)
        file.flush()
        file.close()
    else:
        file = mainDatabase[name]["File"]
        with open(file) as tempDB:
            matDB = json.load(tempDB)
        matDB[lotNr] = {"Type": matType, "Colour": colour, "AmountAvailable": amount, "AmountReserved": "0", "TotalAmount": amount}
        file = open(file, "w")
        json.dump(matDB, file, indent = 1)
        file.flush()
        file.close()
    menu()

# Function reserveMat() is used to check available Materials and reserve an amount from the smallest reasonably possible
# Amount available and puts out the LotNr and the Material amount reserved, available and total.
def reserveMat():
    material = input("Material: ")
    if not material in mainDatabase:
        print("Material not in Database!")
    else:
        file = mainDatabase[material]["File"]
        with open(file) as tempDB:
            matDB = json.load(tempDB)
    menu()

# The code below loads all data available from the Material.json, if it exists, else it doesn't do that and starts
# menu() directly
file2load = Path("Material.json")
if file2load.exists() :
    with open("Material.json") as database:
        mainDatabase = json.load(database)
print("Welcome to dmgMaterialData&Storage!")
menu()