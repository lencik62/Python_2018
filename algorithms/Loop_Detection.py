'''
    
     You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.
     Your objective is to determine the length of the loop. 
     method:

     #1 : using hash and loop ran + loop - loop
     #2 : floyd's cycle finding algro.
        a :- using just pointers
        b :- Brent's The Tortoise and The Hare /  math vers

 '''
# #  1::
def loop_size1(node):
    hashTable = {}
    counter = 0
    while hash(node) not in hashTable:
#  has the node and store it under the py. hash func hash
        hashTable[hash(node)] = counter
        counter += 1
        node = node.next
    
    # one iter time the list ran + loop  ran -  loop ran 
    return counter-hashTable[hash(node)]

# # 2 a:
def loop_size2a(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count

def loop_size2b(node):
    t, h, i, lam = node, node.next, 0, 1
    while t != h:
        if lam == 2**i: i, lam, t = i + 1, 0, h
        h, lam = h.next, lam + 1
    return lam

    