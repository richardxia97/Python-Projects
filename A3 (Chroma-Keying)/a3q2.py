from SimpleGraphics import*

#Asks user for coordinate until input is valid and appears on-screen 
def getCoordinate (string,limit):
    x = input(string)
    while x.isdigit() == False:
        print ("Please enter a valid integer")
        x = input(string)
    while int(x) >= limit or int(x) < 0:
            print ("That image will not appear on screen. Please enter a value that is less than",limit)
            x = input(string)
    return int(x)

#Asks user for file name until valid file is found
def getFile(imageType):
    while True:
        var = False
        fileName = input ("Please enter the file name for the " + imageType)
        try:
            loadFile = loadImage(fileName)
        except: 
            print ("Error: File not found")
            var = True
        if not var:
            return fileName


def main():
    #Load images and determine image coordinates
    hallwayImage = loadImage (getFile("background."))
    monsterImage = loadImage (getFile("monster."))
    monsterWidth = getWidth(monsterImage)
    monsterHeight = getHeight(monsterImage)
    bgWidth = getWidth(hallwayImage)
    bgHeight = getHeight(hallwayImage)
    centeredImageX = getCoordinate("Enter the x-coordinate of the image (centered)",800 + monsterWidth/2) - int(monsterWidth/2)
    centeredImageY = getCoordinate("Enter the y-coordinage of the image (centered)",600 + monsterHeight/2) - int(monsterHeight/2)
    imageX = centeredImageX - int(monsterWidth/2)
    imageY = centeredImageY - int(monsterHeight/2)

    #Iterate through each pixel in the image
    for x in range(0, getWidth(monsterImage)):
        for y in range(0, getHeight(monsterImage)):
            r, g, b = getPixel(monsterImage,x,y)
            #Check if pixel goes off screen
            if centeredImageX + x < bgWidth and centeredImageY + y < bgHeight and centeredImageX + x > 0 and centeredImageY + y > 0:
                r2,g2,b2 = getPixel(hallwayImage,centeredImageX+x,centeredImageY+y)
                #Check for green, if so copy the background pixel
                if g > 80 and r < 50 and b < 50:
                    putPixel(hallwayImage,centeredImageX + x,centeredImageY + y,r2,g2,b2)
                #If not green average the pixel of the background and monster and place it in the background image
                else: 
                    putPixel(hallwayImage,centeredImageX + x,centeredImageY + y,(r+r2)/2,(g+g2)/2,(b+b2)/2) 
    drawImage(hallwayImage,0,0)
main()
