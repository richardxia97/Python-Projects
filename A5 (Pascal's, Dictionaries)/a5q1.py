#Asks user for input until user enters an integer
def getInput():
    while True:
        x = input("Enter the nth numnber")
        if x.isdigit():
            break
    return x
#Computes factorial of a number
def factorial(n):
    temp = 1
    for i in range(2,n+1):
        temp = temp*i
    return temp
#Computes combination of kth number given nth row
def combination(n,k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))
#Creates a list of numbers in triangle until user input is found
def createTriangle(n):
    row = 0
    nums = [1]
    while True:
        row += 1
        for i in range(row+1):
            nums.append(combination(row,i))
        if n in nums:
            return nums
        #Prints number cannot be found is number is not in first 400 rows
        if row > 400:
            print("Number cannot be found")
            return [0]
#Prints out triangle and spaces evenly by adding equal spacing in front and behind the string
def printTriangle(nums):
    temp = len(nums)
    numRows = 0
    counter = 0
    listStrings = []
    formatedStrings = []
    spacing = ""
    #Count number of rows in the triangle
    while temp != 0:
        numRows += 1
        temp -= numRows
    #Add numbers with spacing to listStrings
    for i in range(numRows):
        listStrings.append("")
        for j in range(i+1):
            listStrings[i] += (str(nums[counter]) + ' ')
            counter += 1
    formatedStrings.append(listStrings[len(listStrings)-1])
    #Add spacing to the front equal to the difference between the two lengths / 2
    for i in range(len(listStrings)-2,-1,-1):
        spacing += ' ' * int((len(listStrings[i+1]) - len(listStrings[i]))/2)
        formatedStrings.append(spacing + listStrings[i])
    #Reverse the list of formatedStrings
    formatedStrings = formatedStrings[::-1]
    for i in range(len(formatedStrings)):
        print(formatedStrings[i])
        
        
def main():
    findNum = int(getInput())
    nums = createTriangle(findNum)
    printTriangle (nums)

main()
