#Created by DomiMartinGlogi
#E-Mail:


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
    rawIn = input("Selection: ")
    intIn = int(rawIn)
    #Implement all Menu items here!
    if intIn == 1:
        save()
    elif intIn == 2:
        newMat()
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


def newMat():
    name = input("Name: ")
    matType = input("Material Type: ")
    lotNr = int(input("LotNr: "))
    amount = int(input("Amount in kg: "))
    mainDatabase[name] = {"Type" : matType , "LotNr" : lotNr , "Amount" : amount}
    print(mainDatabase[name])
    menu()

with open("Material.json") as database:
    mainDatabase = json.load(database)
print("Welcome to dmgMaterialData&Storage!")
menu()