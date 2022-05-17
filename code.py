from random import randint, seed

# The basic unit for building a list
class Node:
    def __init__(self, h=0, e=None):
        self.e = e
        self.next = [None] * h


# class start
class Skip_List:

    # constructer
    def __init__(self):
        self.h = Node()
        self.len = 0
        self.maxh = 0

    # flip coine
    def flip_coine(self):
        h = 1
        while randint(1, 2) != 1:
            h += 1
        return h

        # update

    def update(self, e):
        update = [None] * self.maxh
        x = self.h
        for l in reversed(range(self.maxh)):
            while x.next[l] != None and x.next[l].e < e:
                x = x.next[l]
            update[l] = x
        return update

    # insert
    def insert(self, e):

        node = Node(self.flip_coine(), e)

        self.maxh = max(self.maxh, len(node.next))
        while len(self.h.next) < len(node.next):
            self.h.next.append(None)
        # use update function
        update = self.update(e)
        # use search function
        if self.search(e, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

        # search function

    def search(self, e, update=None):
        if update == None:
            update = self.update(e)
        if len(update) > 0:
            t = update[0].next[0]
            if t != None and t.e == e:
                return t
        return None

        # delet

    def delet(self, e):
        # use update
        update = self.update(e)
        # use search
        x = self.search(e, update)
        if x != None:
            for l in reversed(range(len(x.next))):
                update[l].next[l] = x.next[l]
                if self.h.next[l] == None:
                    self.maxh -= 1
            self.len -= 1
    #print function
    #def printL(self):
           
    # get min
    def min(self):
        t = Node(-1)
        if self.h != None:
            nex = self.h.next

            # Make next point to temp
            self.h.next = t

            # Get to the next node in the list
            self.h = nex
            print(self.h.e)
   
   #get max 
  # def max(self):


# out clas
num_ele, num_op = input().split()
ne=int(num_ele)
np =int(num_op)
n = Skip_List()
while np:
    in_list = list(l for l in input().strip("[").strip(":").strip("]"))
    nl=int(in_list[2])
    if in_list[0] == 'i':
        if ne != 0:
            n.insert(int(nl))
            ne -= 1
            np -= 1
    if in_list[0] == 'd':
        n.delet(int(nl))
        np -= 1
    if in_list[0] == 's':
        n.search(int(nl))
        if n.search(int(nl)) :
            print("yes")
        else:
            print("no")
        np -= 1
