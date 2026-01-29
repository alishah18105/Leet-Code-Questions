#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

def getRow(rowNum):
    triangle = []
    for i in range (0,rowNum,1):
        newList = []
        for j in range(0,i+1,1):
            if j == 0 or i == j:
                newList.append(1)
            else:
                value = triangle[i-1][j-1] + triangle[i-1][j] 
                newList.append(value)
        triangle.append(newList)
    return triangle[rowNum-1]
print(getRow(3))