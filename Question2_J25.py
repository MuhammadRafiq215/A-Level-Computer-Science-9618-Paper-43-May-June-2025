# Part (a)
DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54,1]   # Array of Data Type Integer

# Part(b)
# Array is a list of Data Type Integer
def Insertionsort(Array):
    for i in range(1,len(Array)):
        Key = Array[i]
        j= i -1
        while j>= 0 and Array[j] > Key:
            Array[j+1] = Array[j]
            j = j -1

        Array[j + 1] = Key
    return Array


# Part(C)
def OutputArray(OutArray):
    OutArray= OutArray.split(" ")
    print(OutArray)

# part (d(i))
UnSorted =OutputArray(DataArray)
Sorted= Insertionsort(UnSorted)
OutputArray(Sorted)


# part(e)
def Search(ItemToFind,DataArray):
    Max = len(DataArray)
    Min = 0
    Index = (Max + Min)//2
    if ItemToFind == DataArray[Index]:
        return Index
    elif ItemToFind > DataArray[Index]:
        Min = Index + 1
    else:
        Max = Index - 1
    if Max == Min:
        return -1

# Main program
Search(0,Sorted)
Search(345,Sorted)
Search(67,Sorted)
Search(2,Sorted)


    
