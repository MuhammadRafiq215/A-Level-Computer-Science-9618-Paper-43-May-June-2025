# Part(a)
class Node:                            # Node is of type Integer
    def __init__(self,TheData):
        self.__TheData = TheData       # TheData of DataType Integer
        self.__NextNode = None         # self.__NextNode of DataType Integer

def GetData(self):
    return self.__TheData

def NextNode(self):
    return self.__NextNode


def SetNextNode(self,pNextNode):
    self.__NextNode = pNextNode



# part (b)
class LinkedList:       # LinkedList is of data type integer
    def __init__(self):
        self.__HeadNode= None     # self.__HeadNode is of data type integer

 
def InsertNode(self,TheData):
    TheNode= Node(TheData)
    TheNode.SetNextNode(self.__HeadNode)
    self.__HeadNode = TheNode



def Traverse(self):
    ReturnValue = ""
    CurrentNode= self.__HeadNode
    while (CurrentNode != -1):
        ReturnValue = ReturnValue + str(CurrentNode.GetData()) + " "
        CurrentNode = CurrentNode.GetNextNode()
    return ReturnValue






def RemoveNode(self,DataToRemove):
    if self.__HeadNode == None:
        return False
    elif self.__HeadNode.GetData() == DataToRemove:
        self.__HeadNode = self.__HeadNode.GetNextNode()
        return True
    Found = False
    CurrentNode = self.__HeadNode
    while not(Found) and CurrentNode!= None:
        if ((CurrentNode).GetNextNode()).GetData() == DataToRemove:
            CurrentNode.SetNextNode(CurrentNode.GetNextNode().GetNextNode())
            Found = True
        else:
            CurrentNode = CurrentNode.GetNextNode()



def RemoveNode(self,DataToRemove):
    if self.__HeadNode==None:
        return False

    
    if self.__HeadNode.GetData()== DataToRemove:
        self.__HeadNode = self.__HeadNode.GetNextNode()
        return True
    CurrentNode = self.__HeadNode
    while CurrentNode.GetNextNode()!= -1:
        NextOne = CurrentNode.GetNextNode()
        if NextOne.GetData()== DataToRemove:
            CurrentNode.SetNextNode(NextOne.GetNextNode())
            return True
        CurrentNode = NextOne
    return False
