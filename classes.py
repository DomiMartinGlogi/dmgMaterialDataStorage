
    #TODO:
    #Store defined Materials, Parts, Tools and Jobs in separate files
    #Create Functions to work on the classes

# Material Class contains all necessary functions for the Material
class Material:
    def __init__(self,name,type,lotNr,amount,colour):
        self.name = name
        self.type = type
        self.lotNr = lotNr
        self.amount = amount
        self.colour = colour

    # PrintAllInfo is a debug function to print all Variables to console
    def printAllInfo(self,name,type,lotNr,amount,colour):
        print("Name is " + name)
        print("Type is " + type)
        print("LotNr is " + lotNr)
        print("Amount is " + amount)
        print("Colour is " + colour)

    pass

# Part class contains all necessary functions for Parts
class Part:
    def __init__(self,name,number,material1,material2,material3,material4,drawingNr):
        self.name = name
        self.number = number
        self.material1 = material1
        self.material2 = material2
        self.material3 = material3
        self.material4 = material4
        self.drawingNr = drawingNr
        self.toolNr = number

    # PrintAllInfo is a debug function to print all Variables to console
    def printAllInfo(self,name,number,material1,material2,material3,material4,drawingNr):
        print("Name is " + name)
        print("Type is " + type)
        print("Number is " + number)
        print("Material1 is " + material1)
        print("Material2 is " + material2)
        print("Material3 is " + material3)
        print("Material4 is " + material4)
        print("DrawingNr is " + drawingNr)

    pass

# Tool class contains all necessary functions for Tools
class Tool:
    def __init__(self,toolNr):
        self.toolNr = toolNr

    # PrintAllInfo is a debug function to print all Variables to console
    def printAllInfo(self, toolNr):
        print("ToolNR is" + toolNr)

    pass

# Job class contains all necessary functions for Jobs
class Job:
    def __init__(self,jobNr,part,material,tool,amount,customer):
        self.jobNr = jobNr
        self.part = part
        self.material = material
        self.tool = tool
        self.amount = amount
        self.customer = customer

    # PrintAllInfo is a debug function to print all Variables to console
    def printAllInfo(self, jobNr,part,material,tool,amount,customer):
        print("JobNr is " + jobNr)
        print("Part is " + part)
        print("Material is " + material)
        print("Tool is " + tool)
        print("Amount is " + amount)
        print("Customer is " + customer)
    pass
