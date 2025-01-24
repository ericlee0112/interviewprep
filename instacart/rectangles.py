'''
you are given operations, an array containing the following two types of operations:

[0,a,b] = create and save rectangle of size a x b
[1,a,b] = can a box of size axb fit inside each of the earlier saved rectanges. 

we can rotate the rectanges by 90 degrees so that a rectangle of a x b can be b x a

return a list of booleans, representing the answers to the second type of operation in the order they appear

[[0,3,3], [0,5,2], [1,3,2], [1,2,4]] = [true, false]


'''

def rectangleFit(operations):
    # rotate each rectangle so that width is no larger than its height, remember only min width and height of all saved rectangles
    minWidthSoFar = float('inf')
    minHeightSoFar = float('inf')

    output = []

    # adjust operations list
    for i in range(len(operations)):
        operation = operations[i]
        width = operation[1]
        height = operation[2]
        if width > height:
            operations[i][1] = height
            operations[i][2] = width

    for operation in operations:
        width = operation[1]
        height = operation[2]
        if operation[0] == 0:
            minWidthSoFar = min(minWidthSoFar, width)
            minHeightSoFar = min(minHeightSoFar, height)
        else:
            if (width <= minWidthSoFar and height <= minHeightSoFar):
                output.append(True)
            else:
                output.append(False)
    
    return output

operations = [[0,3,3], [0,5,2], [1,3,2], [1,2,4]] 
print(rectangleFit(operations))