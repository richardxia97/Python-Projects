import sys

def userInput():
    while True:
        temp = False
        name = input("Enter the name of the file.")
        try:
            file = open(name)
        except:
            print("Error: No such file named '"+name+"'")
            temp = True
        if not temp:
            return name

def horizontalFlip (storeAscii):
    newAscii = [[] for x in range(len(storeAscii))]
    for y in range(len(storeAscii)):
        for x in range(len(storeAscii[0])-1,0,-1):
            newAscii[y].append(storeAscii[y][x])
    return newAscii

def verticalFlip (storeAscii):
    newAscii = [[] for y in range(len(storeAscii))]
    for y in range(len(storeAscii),0,-1):
        for x in range(len(storeAscii[0])):
            newAscii[len(storeAscii)-y].append(storeAscii[y-1][x])
    return newAscii
            

def printAscii (storeAscii):
    for y in range(len(storeAscii)):
        for x in range(len(storeAscii[0])):
            print(storeAscii[y][x],end="")
        print ('\n',end="")

def rotate (storeAscii):
    newAscii = [[] for y in range(len(storeAscii[0]))]
    for y in range(len(storeAscii[0])):
        for x in range(len(storeAscii)):
            newAscii[y].append(storeAscii[len(storeAscii)-1-x][y])
    return newAscii

def negative(storeAscii,code):
    newAscii = [[] for y in range(len(storeAscii))]
    for y in range(len(storeAscii)):
        for x in range(len(storeAscii[0])):
            newAscii[y].append(code[(len(code)-1)-code.index(storeAscii[y][x])])
    return newAscii

def save(storeAscii,f,name,code):
    f = open(name,'w')
    f.write(code+'\n')
    for y in range(len(storeAscii)):
        for x in range(len(storeAscii[0])):
            f.write(storeAscii[y][x])
        f.write('\n')
    return f

def main():
    fileName = userInput() 
    f = open(fileName,'r+')
    code = f.readline().rstrip()
    storeAscii=[[] for x in range(sum(1 for line in open(fileName))-1)]
    n = 0
    for line in f:
        for c in line:
            if c != '\n':
                storeAscii[n].append(c)
        n += 1
    printAscii(storeAscii)
    while True:
        operation = input("1 = Flip image Horizontally\n2 = Flip image Vertically\n3 = Rotate Image\n4 = Invert Image\n5 = Save Image\n")
        if operation == '1':
            storeAscii = horizontalFlip (storeAscii)
            printAscii(storeAscii)
        elif operation == '2':
            storeAscii = verticalFlip (storeAscii)
            printAscii(storeAscii)
        elif operation == '3':
            storeAscii = rotate(storeAscii)
            printAscii(storeAscii)
        elif operation == '4':
            storeAscii = negative(storeAscii,code)
            printAscii(storeAscii)
        elif operation == '5':
            f = save(storeAscii,f,fileName,code)
            f.close()
            sys.exit()
        else:
            print ("Invalid!")
        
            
    
        
    
main()
            
