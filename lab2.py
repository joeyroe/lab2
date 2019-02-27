# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:07:31 2019
CS 2302 Data Structures
Professor: Fuentes
TAs: Anindita Nath, Maliheh Zargaran
Assignment: Lab2
02/26/2019
@author: Joey Roe
"""
import random
class node(object):
    def __init__(self, data, next = None):
        self.data = data                   #Makes the Node
        self.next = next
        
class linkedList(object):
    def __init__(self):
        self.head = None                  #Makes the linked list
        self.tail = None
        
    def append(self, num):
        if self.head == None:
            self.head = node(num)        #adds numbers to linked list
            self.tail = self.head
        else:
            self.tail.next = node(num)
            self.tail = self.tail.next
            
    def printList(self):
        temp = self.head
        while temp!= None:               #prints the list
            print(temp.data, end = ' ')
            temp = temp.next
        print()
                
     #gets the length of the list           
    def listLength(self):
        temp = self.head
        counter = 0
        while temp != None:
            counter += 1#adds one to represent nodes traveled
            temp = temp.next#moves through the list
        return counter
    
    #returns the number at a certain index
    def elementAt(self, index):
        if self.head == None:
            return
        if index >= self.listLength():#if index eneterd is out of range
            return None
        if index < 0: #if index entered is a negative
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.data

#fills the list with random numbers  
def listFiller(num):
    newList = linkedList()
    for i in range(num):
        newList.append(random.randrange(101))     
    return newList
 
    

def IsEmpty(theList):
    return theList.head == None
    

    
def bubbleSort(theList):
    change = False
    if theList.head == None:
        return theList
    while change != True:
        temp = theList.head
        change = True
        while temp.next != None: #goes through the whole list and compares values
            if temp.data > temp.next.data: #compares
                temp2 = temp.data #temporary place holder for temp.data
                #arrange items properly
                temp.data = temp.next.data
                temp.next.data = temp2
                change = False
            temp = temp.next
    return theList


def merge(list1, list2):
    temp1 = list1.head
    temp2 = list2.head
    newList = linkedList()
    while temp1 != None and temp2 != None:
        if temp1.data < temp2.data:
            newList.append(temp1.data)
            temp1 = temp1.next
        else:
            newList.append(temp2.data)
            temp2 = temp2.next
    #for when either the firs list or second list become empty
    while temp1 != None:
        newList.append(temp1.data)
        temp1 = temp1.next
    while temp2 != None:
        newList.append(temp2.data)
        temp2 = temp2.next
    return newList
        
    
def mergeSort(theList):
    if theList.listLength() > 1:
        temp = theList.head
        list1 = linkedList()
        list2 = linkedList()
        remaining = theList.listLength() - (theList.listLength() // 2)#for the second half of list
        for i in range(theList.listLength() // 2):  #fills the first list with the first half
            list1.append(temp.data)
            temp = temp.next
        for i in range(remaining):   #fills second list with second half
            list2.append(temp.data)
            temp = temp.next
        list1 = mergeSort(list1)
        list2 = mergeSort(list2)
        return merge(list1, list2)
    else:
        return theList
    
    
def listCombine(list1, list2):
    temp1 = list1.head
    temp2 = list2.head
    newList = linkedList()
    #go through list1 and put elements in new List
    while temp1 != None:
        newList.append(temp1.data)                #combines two lists together
        temp1 = temp1.next
    while temp2 != None:#put list2 elements in new list
        newList.append(temp2.data)
        temp2 = temp2.next
    return newList
        

def quickSort(theList):
    if theList.listLength() > 1:
        pivot = theList.head.data
        list1 = linkedList()
        list2 = linkedList()
        temp = theList.head.next
        while temp != None:
            if temp.data <= pivot: 
                list1.append(temp.data)
            else:
                list2.append(temp.data)     #compare to pivot to determine what goes where
            temp = temp.next
        list1 = quickSort(list1)
        list2 = quickSort(list2)
        list1.append(pivot)#add the pivot to the end of list1
        return listCombine(list1, list2)
    else:
        return theList
    
    
    
def Copy(theList):
    C = linkedList()
    if IsEmpty(theList):
        return C
    else:
        temp = L.head                #makes a copy of the list
        while temp is not None:
            C.append(temp.data)
            temp = temp.next
        return C  
    
    
    
def median(L):
    C = Copy(L)
    a = quickSort(C)                              #gets the middle of the list
    return a.elementAt(a.listLength()//2)


#def quickSort2(theList):
#    if theList.listLength() > 1:
#        list1 = linkedList()
#        list2 = linkedList()
#        temp = theList.head.next
#        pivot = theList.head.data
#        med = median(theList)
#        while temp != None:
#            if temp.data <= pivot:
#                list1.append(temp.data)
#            else:
#                list2.append(temp.data)
#        temp1 = list1.head
#        while temp1 != None:
#            if temp.data == med:
#                list1 = mergeSort(list1)
#                return list1
#            temp = temp.next
#        else:
#            list2 = mergeSort(list2)
#            return list2
#    else:
#        return theList

    
    
    
    
    
    
L = listFiller(4)
print('original list: ', end = ' ')
L.printList()
print()

print('bubbleSorted: ', end = ' ')
a = bubbleSort(L)
a.printList()
print()

print('mergeSorted: ', end = ' ')
b = mergeSort(L)
b.printList()
print()

print('quickSorted: ', end = ' ')
c = quickSort(L)
c.printList()
print()

print('Median: ', end = ' ')
d = median(L)
print(d)
print()
  

#print('modified quickSorted: ', end = ' ' )
#e = quickSort2(L)
#e.printList()  
