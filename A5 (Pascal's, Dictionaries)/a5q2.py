#Asks user for board pieces, asks again if any characters are invalid
def getInput(dictionary):
    board = []
    for i in range(8,0,-1):
        valid = True
        while True:
            row = input("Please type 8 characters for the " + str(i) + "th row of the chessboard: ")
            #Checks if any character entered is not in the dictionary
            for each in row:
                if each.lower() not in dictionary or len(row) != 8:
                    valid = False
            #If character is in dictionary append, else ask for input again
            if valid == True:
                board.append(row)
                break
            else:
                print("Please enter a valid input")
                break
    return board
#Calculates score using dictionary 
def checkBoard (board,allPieces):
    whiteValue = 0
    blackValue = 0
    #Iterate through each piece in the board, add to black if lower, 
    for row in board:
        for each in row:
            if each.isupper():
                blackValue += allPieces[each.lower()]
            else:
                whiteValue += allPieces[each]
    print ("White has a score of",whiteValue,"and Black has a score of " + str(blackValue) + ", so ", end ="")
    #Prints winner with higher value
    if whiteValue > blackValue:
        print("White is winning.")
    elif blackValue > whiteValue:
        print("Black is winning.")
    else:
        print("this game is a tie.")

def main():
    allPieces = {'k':0, 'q':10, 'b':3, 'n':3, 'r':5, 'p':1, '-':0}
    board = getInput(allPieces)
    checkBoard(board,allPieces)
main()
