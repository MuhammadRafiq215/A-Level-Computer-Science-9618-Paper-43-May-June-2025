Queue = [-1] * 50     # Declare Queue:ARRAY[0:49]
HeadPointer = -1      # DataType Integer
TailPointer = -1      # DataType Integer

# Part (b)
def Enqueue(Data):   # Data is of DataType Integer
    global Queue
    global HeadPointer
    global TailPointer
        
    
    if TailPointer < 49:
        TailPointer = TailPointer + 1
        Queue[TailPointer] = Data

        if HeadPointer == -1:
            HeadPointer = 0 
        return True
    else:
        return False


# part (c)
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer > -1 and HeadPointer <= TailPointer:
        Data = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        return Data
    else:
        return -1

# part(d)
# File is of Data Type Integer
# Line is of Data type Integer

def CreateQueue():
    try:
        File = open("QueueData.txt",'r')
        for Line in File:
            Item= Enqueue(int(Line))
            if Item == False:
                print("Queue full")
                break
        File.close()

    except Exception as e:
        print("Error:",e)


# part (e(i))
#.......................... Main Program............................
CreateQueue()
Total = 0   # Total is of DataType Integer
Item = 0 
while Item > -1:
    Item = Dequeue()
    if Item != -1:
        Total = Total + Item

print("The total is",Total)


