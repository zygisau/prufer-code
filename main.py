class vertex:
    def __init__(self):
        name = ""
        joinsWith = []
        branchCount = 0

tree = []

# reading from the file 
with open('tree3') as f:
    file = [[int(x) for x in line.split()] for line in f]

# appending to the class
index = 0
for element in file:
    tree.append(vertex())

    tree[index].name = element[0]
    element.pop(0)

    tree[index].joinsWith = element

    tree[index].branchCount = len(element)
    index += 1

# main
prufer = ""
while len(tree) > 2: # prüfer code is completed once there are only 2 vertices left

    # finding the smallest number vertex with only one branch
    minVertex = tree[0]
    index = 0
    while minVertex.branchCount != 1: # finding first element which could be needed vertex
        index += 1
        minVertex = tree[index]
    
    for index, element in enumerate(tree, start=1): # searching through every element
        if (element.branchCount == 1 and minVertex.name > element.name):
            minVertex = element
    
    # adding element to the code
    prufer += str(minVertex.joinsWith[0])

    # removing used branch
    for element in tree: # searching for a vertex that has vertex which needs to be deleted
        if element.name == minVertex.joinsWith[0]:
            element.branchCount -= 1
            element.joinsWith.remove(minVertex.name)
            break
    
    tree.remove(minVertex)

# printing results
print(prufer)