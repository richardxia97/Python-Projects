from SimpleGraphics import*

def userInput():
    while True:
        temp = False
        name = input("Enter the file name of the image:")
        try:
            file = loadImage(name)
        except:
            print ("Error: No such file named '"+name+"'")
            temp = True
        if not temp:
            return file

def conversion (img):
    imgWidth = getWidth(img)
    imgHeight = getHeight(img)
    storeAscii = [[] for _ in range(imgHeight)]
    asciiSymbols = [' ','.',',','~',':','=','?','I','7','#']
    while True:
        background = input("'1' to print on a black background, '2' to print on a white background")
        if background == '1':
            break
        if background == '2':
            asciiSymbols = asciiSymbols[::-1]
            break
        else:
            print("Error: Invalid input") 
            
    asciiValues = [int(x*255/10) for x in range(1,11)]
    for y in range (0, imgHeight):
        for x in range (0, imgWidth):
            r,g,b = getPixel(img,x,y)
            avg = int((r+g+b)/3)
            for each in range (0,11):
                if avg <= asciiValues[each]:
                    storeAscii[y].append(asciiSymbols[each])
                    break
    return storeAscii

def printAscii (storeAscii):
    for y in range(0,len(storeAscii)):
        for x in range(0,len(storeAscii[0])):
            print(storeAscii[y][x],end="")
        print('\n',end="")
def main():
    img = userInput()
    storeAscii = conversion(img)
    printAscii(storeAscii)
        
    
main()
            
