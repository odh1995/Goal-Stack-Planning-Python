from Stack import Stack
from Element import Element
from conjuctivePredicatesCheck import*
from checkPreconditions import*
import time

# startState = "ON(C,B)^ONTABLE(B)^ONTABLE(A)^CLEAR(A)^CLEAR(C)".split("^")
# endState = "ON(A,B)^CLEAR(A)^ONTABLE(C)^ON(B,C)".split("^")

# startState = "ON(C,A)^ONTABLE(A)^ONTABLE(B)^CLEAR(B)^CLEAR(C)".split("^")
# endState = "ON(A,C)^CLEAR(A)^ONTABLE(B)^ON(C,B)".split("^")

# startState = "ON(A,B)^ON(B,C)^ON(C,D)^ONTABLE(D)^ONTABLE(E)^CLEAR(A)^CLEAR(E)".split("^")
# endState = "ON(A,B)^CLEAR(A)^ON(B,C)^ON(C,D)^ON(D,E)^ONTABLE(E)".split("^")

startState = "ON(A,B)^ON(B,C)^ONTABLE(C)^ONTABLE(D)^CLEAR(A)^CLEAR(D)^ONTABLE(E)^CLEAR(E)".split("^")
endState = "ON(D,C)^CLEAR(D)^ON(C,B)^ON(B,A)^ONTABLE(E)^ONTABLE(A)^CLEAR(E)".split("^")



def goalstack(startState, endState, file):

    startTime = time.time()
    goalstack = Stack()
    currentState = Stack()
    steps = Stack()
    Arm = Stack()
    goalstack.push(endState)

    for i in endState:
        goalstack.push(i)  # store goal into stack

    for i in startState:  # store initial state to currentstate
        currentState.push(i)

    k = 30

    while(not goalstack.isEmpty()):
    # for i in range(k):
        N = goalstack.peek()
        # print goalstack.toString()
        # print currentState.toString()
        # print steps.toString()
        # print Arm.toString()
        # print "\n"

        if N in currentState.__contains__():
            goalstack.pop()


    # -------------------------------------- #CHECK FOR CONJUCTIVE PREDICATES----------------------------------------------------

        elif type(N) == list:
            if len(set(N) & set(currentState.__contains__())) == len(N):
                goalstack.pop()
            else:             #CHECK FOR PREDICATES THAT IS IN THE CONJUCTIVE PREDICATE THAT DOES NOT EXIST IN THE CURRENT STATE
                tempList = []
                for i in N:
                    b = 0
                    for j in currentState.__contains__():
                        if i == j:
                            b += 1
                    if b == 0:
                        tempList.append(i)
    #--------------------------------------CHECK AND APPEND GOALSTACK FOR CONJUCTIVE PREDICATES THAT DOES NOT SATISFY

                for i in tempList:
                    #CHECK FOR ON
                    if len(Element(N)) == 2:
                        listAppend = ConjuctiveCheckOn(i, (Element(N)[0]), (Element(N)[1]))
                    else:
                        element = (Element(N)[0])

                        # CHECK HOLD
                        if hold(element) in i:
                            listAppend = checkPre1(element)
                            for j in listAppend:
                                goalstack.push(j)

                        # CHECK ARMEMPTY
                        elif armempty()in i:
                            if Arm.size() != 0:
                                listAppend = [putdown(Arm.peek()), [PutdownP(Arm.peek())], PutdownP(Arm.peek())]
                                for j in listAppend:
                                    goalstack.push(j)
                                print "hi"
                            else:
                                if len(set(N) & set(currentState.__contains__())) == len(N)-1:
                                    goalstack.pop()


                        # CHECK CLEAR
                        elif clear(element) in i:
                        # CHECK FOR THE TOP OF THE BLOCK
                            listAppend = checkClear(currentState.__contains__(), element)
                            for j in listAppend:
                                goalstack.push(j)

                        #CHECK ONTABLE
                        elif ontable(element)in i:
                            listAppend = checkOnTable(currentState.__contains__(), element)
                            for j in listAppend:
                                goalstack.push(j)




        else:
            # ON / STACK / UNSTACK 2 ELEMENTScheckPre1
            if len(Element(N)) == 2:
                a = Element(N)[0]
                b = Element(N)[1]


                if on(a, b) in N:   #CHECK ON
                    list1 = [stack(a, b), StackP(a, b)]
                    for i in StackP(a, b):
                        list1.append(i)
                    for i in list1:
                        goalstack.push(i)

        # ------------------------------ STACK CHECK--------------------------------------------
                elif N == stack(a, b):
                    # if len(set(StackP(a, b)) & set(current)) != len(StackP(a, b)):
                    #     return 0, StackP(a, b), current

                    StackUpdate(currentState.__contains__(), a, b)
                    for i in StackE(a, b):  # UPDATE THE CURRENT STATE IF REQUIREMENTS ARE MET
                        currentState.push(i)
                    Arm.pop()
                    steps.push(stack(a, b))

        #------------------------------ UNSTACK CHECK--------------------------------------------
                elif N == unstack(a, b):
                    # if len(set(UnstackP(a, b)) & set(current)) != len(UnstackP(a, b)):
                    #     return 0, UnstackP(a, b), 1

                    Unstackupdate(currentState.__contains__(), a, b)
                    for i in UnstackE(a, b):  # UPDATE THE CURRENT STATE IF REQUIREMENTS ARE MET
                        currentState.push(i)
                    Arm.push(a)
                    steps.push(unstack(a, b))

                if N != on(a, b):
                    goalstack.pop()





                # num, listAppend, currentList = checkPre2(steps, currentState.__contains__(), N, (Element(N)[0]), (Element(N)[1]))
                # # FOR ON
                # if num == 0:
                #     for i in listAppend:
                #         goalstack.push(i)
                # # FOR STACK / UNSTACK
                # elif num == 1:
                #
                #     # UPDATE CURRENT STATE
                #     del currentState.__contains__()[:]
                #     for i in currentList:
                #         currentState.push(i)
                #
                #     # UPDATE STEPS
                #     del steps.__contains__()[:]
                #     for i in listAppend:
                #         steps.push(i)
                #     if N != on((Element(N)[0]), (Element(N)[1])):
                #         goalstack.pop()


    #------------------------------------------------------------------------ IF ONLY ONE ELEMENT : HOLD / CLEAR/ ONTABLE/ PICKUP/ PUTDOWN------------------------------------------------------------------
            else:
                element = (Element(N)[0])

                # CHECK HOLD
                if hold(element) in N:
                    # CHECK PRECONDITION
                    if element not in Arm.__contains__():
                        listAppend = checkPre1(element)
                        for i in listAppend:
                            goalstack.push(i)
                    # else:
                    #     goalstack.pop()


                # CHECK ARMEMPTY
                elif armempty()in N:
                    if Arm.size() != 0:
                        listAppend = [putdown(Arm.__contains__()[0]), PutdownP(Arm.__contains__()[0])]
                        for i in listAppend:
                            goalstack.push(i)
                    else:
                        goalstack.pop()


                # CHECK PICKUP
                elif pickup(element) in N:
                    # # IF THERE ISNT ANY PREDICATES OF PICKUP IN CURRENTSTATE
                    # if len(set(PickupP(element)) & set(currentState)) != len(PickupP(element)):
                    #     listAppend = PickupP(element)
                    #     for i in listAppend:
                    #         goalstack.push(i)

                    # DELETE SELECTED PREDICATE
                    PickupUpdate(currentState.__contains__(), element)
                    currentState.push(PickupE(element))
                    steps.push(pickup(element))
                    Arm.push(element)
                    goalstack.pop()

                # CHECK PUTDOWN
                elif putdown(element) in N:
                    # # IF THERE ISNT ANY PREDICATES OF PUTDOWN IN CURRENTSTATE
                    # if len(set(PutdownP(element)) & set(currentState)) != len(PutdownP(element)):
                    #     listAppend = PutdownP(element)
                    #     for i in listAppend:
                    #         goalstack.push(i)

                    # DELETE SELECTED PREDICATE
                    Arm.pop()
                    PutdownUpdate(currentState.__contains__(), element)
                    for i in PutdownE(element):
                        currentState.push(i)
                    steps.push(putdown(element))
                    goalstack.pop()

                # CHECK CLEAR
                elif clear(element) in N:
                    # CHECK FOR THE TOP OF THE BLOCK
                    listAppend = checkClear(currentState.__contains__(), element)
                    for i in listAppend:
                        goalstack.push(i)

                elif ontable(element) in N:
                    # CHECK FOR THE TOP OF THE BLOCK
                    listAppend = checkOnTable(currentState.__contains__(), element)
                    for i in listAppend:
                        goalstack.push(i)


    file.write("Goal Stack Planning\n")
    file.write("Path found for " + str(startState) + " to " + str(endState) + "\n")
    file.write("Number of steps required is : " + str(steps.size()))
    file.write("Steps required are: " + steps.toString() + "\n")
    file.write("Time taken = " + str(time.time() - startTime) + "s")

outfile = open("gsutput.txt", "w+")
goalstack(startState, endState, outfile)
outfile.close()
