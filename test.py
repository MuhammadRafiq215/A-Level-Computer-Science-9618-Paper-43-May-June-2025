Queue = [-1] * 50     # Queue : ARRAY[0:49] OF INTEGER
HeadPointer = -1      # INTEGER
TailPointer = -1      # INTEGER

def Enqueue(Data):    # Data : INTEGER
    global Queue, HeadPointer, TailPointer
    if TailPointer < 49:
        TailPointer = TailPointer + 1
        Queue[TailPointer] = Data
        if HeadPointer == -1:
            HeadPointer = 0
        return True
    else:
        return False

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer > -1 and HeadPointer <= TailPointer:
        Data = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        return Data
    else:
        return -1

def CreateQueue():
    try:
        File = open("QueueData.txt", "r")
        for Line in File:
            Item = Enqueue(int(Line))
            if Item == False:
                print("Queue full")
                break
        File.close()
    except:
        print("The file doesn't exist or the values can't be inserted!")

# ---------------- Main program ----------------
CreateQueue()
Total = 0
Item = 0
while Item > -1:
    Item = Dequeue()
    if Item != -1:
        Total = Total + Item
print("The total is", Total)

