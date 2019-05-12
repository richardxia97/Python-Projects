from SimpleGraphics import*
rect(0,0,800,600)

CONST_MAX_SPACE = 50

def drawAndGate (x,y):
    setWidth(3)
    line(x+50,y,x,y)
    line(x,y,x,y+70)
    line(x,y+70,x+50,y+70)
    curve(x+50,y,x+100,y+35,x+50,y+70)
    
def drawCircle (boolValue):
    #Draw starting points and lines
    for x in range (0,5):
        setFill("white")
        setWidth(3)
        line(25,13+x*CONST_MAX_SPACE,125,13+x*CONST_MAX_SPACE)
        setWidth(1)
        ellipse(3,x*CONST_MAX_SPACE + 3,25,25)
        boolLetter = str(boolValue[x])[:1]
        text(16,13+x*CONST_MAX_SPACE,boolLetter)
        setFill("black")
        ellipse(80,x*CONST_MAX_SPACE + 9,10,10)
        
    #Draw first 2 AND gates
    drawAndGate(125,53)
    drawAndGate(125,153)
    
    #Draw second set of lines
    line(125,13,250,13)
    line(200,88,250,88)
    line(200,188,250,188)
    setWidth(1)
    ellipse(245,8,10,10)
    ellipse(245,83,10,10)
    ellipse(245,183,10,10)
    setWidth(3)
    line(250,8,250,8+CONST_MAX_SPACE/2)
    line(250,83,250,83+CONST_MAX_SPACE/2)
    line(250,183,250,183-CONST_MAX_SPACE/2)
    setWidth(1)
    ellipse(245,33,10,10)
    ellipse(245,108,10,10)
    ellipse(245,157,10,10)
    setWidth(3)
    line(250,36,300,36)
    line(250,111,300,111)
    line(250,161,300,161)
    drawAndGate(300,101)
    
    #Draw NOT Gate
    line(300,11,300,61)
    line(300,61,375,36)
    line(375,36,300,11)
    setFill("white")
    setWidth(1)
    ellipse(375,28,15,15)

    #Draw 3rd set of lines and AND gate
    setWidth(3)
    line (390,36,440,36)
    line (375,136,440,136)
    setFill("black")
    setWidth(1)
    ellipse(435,31,10,10)
    ellipse(435,131,10,10)
    setWidth(3)
    line(440,36,440,51)
    line(440,136,440,111)
    setWidth(1)
    ellipse(435,46,10,10)
    ellipse(435,106,10,10)
    setWidth(3)
    line(440,51,490,51)
    line(440,111,490,111)
    drawAndGate(490,46)

    #Draw final line and circle
    line(565,81,640,81)
    setWidth(1)
    ellipse(580,76,10,10)
    setFill("white")
    ellipse(627,68,25,25)
    text(640,81,str(evaluateMyCircuit(boolValue))[:1])
    
def evaluateMyCircuit(boolValue):
    z = ((boolValue[1] and boolValue[2]) and (boolValue[3] and boolValue[4])) and (not boolValue[0])
    #Student Number (101007519)
    return z
    

def main():
    boolValue = []
    for x in range (0,5):
        storeValue = input ("Enter either 't' for True or 'f'for False to store in " + chr(ord('A') + x) + ' ')
        while storeValue != 't' and storeValue != 'f':
            print ("Please enter a valid input")
            storeValue = input ("Enter either 't' for True or 'f' for False ")
        if storeValue == 't':
            boolValue.append(True)
        else:
            boolValue.append(False)
    print (evaluateMyCircuit(boolValue))
    print ("Student Number: 101007519")
    drawCircle(boolValue)
    
main()
