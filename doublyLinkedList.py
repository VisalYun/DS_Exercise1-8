class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


class listElement():
    ssn = 0
    name = ""
    depth = ""
    design = ""
    sal = 0
    phoneNum = 0


def createObject():
    ssn, name, depth, design, sal, phone = input("Enter SSN, Name, Dept, Designation, Sal, and Phone Number: ").split()
    element = listElement()
    element.ssn = ssn
    element.name = name
    element.depth = depth
    element.design = design
    element.sal = sal
    element.phoneNum = phone
    return element


def queueImplement():
    isTrue2 = True
    while isTrue2:
        print("\n+++++ Queue Menu +++++ \n1:Push operation at end \n2:Pop operation at beginning \n3:Display "
              "\n4:Exit")
        inp2 = int(input("Enter choice: "))
        if inp2 == 1:
            element = createObject()
            list.insertAtEnd(element)
        elif inp2 == 2:
            list.deleteAtStart()
        elif inp2 == 3:
            list.listPrint()
        elif inp2 == 4:
            isTrue2 = False
        else:
            print("Invalid input...")


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insertAtStart(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insertAtEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def deleteAtStart(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def deleteAtEnd(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def getCount(self):
        if self.start_node is None:
            print("List has no element")
            return 0
        else:
            count = 0
            n = self.start_node
            while n is not None:
                count += 1
                n = n.nref
            return count

    def listPrint(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item.ssn, n.item.name, n.item.depth, n.item.design, n.item.sal, n.item.phoneNum)
                n = n.nref


isTrue = True
list = DoublyLinkedList()
while isTrue:
    print("\n ===== Main Menu ===== \n1:Create DLL of Employee Nodes \n2:Display Status and Size \n3:Insert Beginning "
          "\n4:Delete Beginning \n5:Insert End \n6:Delete End \n7:Queue Demo using SLL \n8:Exit")
    inp = int(input("Enter choice: "))
    if inp == 1:
        studentNum = int(input("Enter number of employee: "))
        while studentNum > 0:
            element = createObject()
            list.insertAtEnd(element)
            studentNum -= 1
    elif inp == 2:
        list.listPrint()
        print("Total list elements: ", list.getCount())
    elif inp == 3:
        studentNum = int(input("Enter number of employee: "))
        while studentNum > 0:
            element = createObject()
            list.insertAtStart(element)
            studentNum -= 1
    elif inp == 4:
        list.deleteAtStart()
    elif inp == 5:
        studentNum = int(input("Enter number of employee: "))
        while studentNum > 0:
            element = createObject()
            list.insertAtEnd(element)
            studentNum -= 1
    elif inp == 6:
        list.deleteAtEnd()
    elif inp == 7:
        queueImplement()
    elif inp == 8:
        isTrue = False
    else:
        print("Wrong Input...")
