found_flag=0

class Node:
    def __init__(self,data):
        self.data=data
        self.leftNode=None
        self.rightNode=None

def insert_data(data_node,data_input):
    currentNode=data_node
    if(currentNode.data=='None'):
        currentNode.data=data_input
        currentNode.leftNode=Node('None')
        currentNode.rightNode=Node('None')
    else:
        if(data_input<currentNode.data):
            insert_data(currentNode.leftNode,data_input)
        elif (data_input>=currentNode.data):
            insert_data(currentNode.rightNode,data_input)

def search_tree(currentNode,search_key):
    if(currentNode.data!='None'):
        if currentNode.data==search_key:
            print "Found data: ", currentNode.data
            global found_flag
            found_flag=1
        search_tree(currentNode.leftNode,search_key)
        search_tree(currentNode.rightNode,search_key)
    return found_flag
    
def traverse_tree(currentNode):
    if currentNode.data!='None':
        traverse_tree(currentNode.leftNode)
        print "Node data: ",currentNode.data
        traverse_tree(currentNode.rightNode)

rootNode=Node('None')

flag=0
print "Enter \'None\' (without quotes) for end of input."
while(flag!=1):
    data_input=raw_input("Enter data: ")
    if data_input!='None':
        data_input=int(data_input)
        insert_data(rootNode,data_input)
    else:
        flag=1

print "InOrder traversal of generated BST:"
traverse_tree(rootNode)

search_key=int(raw_input("Enter the search key: "))

if search_tree(rootNode,search_key)==0:
    print "Element not found"





