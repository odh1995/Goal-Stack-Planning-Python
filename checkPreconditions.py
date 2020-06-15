from Operators import*

commas = ","
close = ")"
def on(a,b):
    return "ON(" + a + commas + b + close
def ontable(a):
    return "ONTABLE(" + a + close
def clear(a):
    return "CLEAR("+ a + close
def stack(a,b):
    return "STACK(" + a + commas + b + close
def unstack(a,b):
    return "UNSTACK(" + a + commas + b + close
def armempty():
    return "HANDEMPTY"
def pickup(a):
    return "PICKUP(" + a + close
def putdown(a):
    return "PUTDOWN(" + a + close
def hold(a):
    return "HOLDING(" + a + close

# REMOVE PREDICATES IN CURRENT STATES FOR UNSTACK
def Unstackupdate(current,a,b):
    UUtemp = []
    for i in range(len(current)):
        if current[i] == armempty():
            UUtemp.append(armempty())
        elif current[i] == on(a, b):
            UUtemp.append(on(a, b))
        elif current[i] == clear(a):
            UUtemp.append(clear(a))

    for i in UUtemp:
        current.remove(i)

def StackUpdate(current,a,b):   #REMOVE PREDICATES IN C
    SUtemp = []
    for i in range(len(current)):
        if current[i] == hold(a):
            SUtemp.append(hold(a))
        elif current[i] == clear(b):
            SUtemp.append(clear(b))

    for i in SUtemp:
        current.remove(i)

def PickupUpdate(current, a):
    PUtemp = []
    for i in range(len(current)):

        if current[i] == armempty():
            PUtemp.append(armempty())
        elif current[i] == clear(a):
            PUtemp.append(clear(a))
        elif current[i] == ontable(a):
            PUtemp.append(ontable(a))

    for i in PUtemp:
        current.remove(i)

def PutdownUpdate(current,a):
    PDtemp = []
    for i in range(len(current)):
        if current[i] == hold(a):
            PDtemp.append(hold(a))

    for i in PDtemp:
        current.remove(i)


# -----------------------------------------------------------------------------------------------------------------------------------
# return ([if 0 = does not meet requirement, if 1 = meet requirement,], LIST, [if 0 = non-action , if 1 = action])
# def checkPre2(steps, current, n, a, b):   #CHECK ON
#     updated = []
#     if on(a, b) in n:
#         list1 = [stack(a, b), StackP(a, b)]
#         for i in StackP(a, b):
#             list1.append(i)
#         return 0, list1, 0
#
#     elif stack(a, b) in n: #STACK CHECK
#         # if len(set(StackP(a, b)) & set(current)) != len(StackP(a, b)):
#         #     return 0, StackP(a, b), current
#
#         updated = StackUpdate(current, a, b)
#         for i in StackE(a, b):#UPDATE THE CURRENT STATE IF REQUIREMENTS ARE MET
#             updated.append(i)
#         steps.push(stack(a, b))
#         return 1, steps.__contains__(), current
#
#     elif unstack(a, b) in n:#UNSTACK CHECK
#         # if len(set(UnstackP(a, b)) & set(current)) != len(UnstackP(a, b)):
#         #     return 0, UnstackP(a, b), 1
#
#         updated = Unstackupdate(current, a, b)
#         for i in UnstackE(a, b):#UPDATE THE CURRENT STATE IF REQUIREMENTS ARE MET
#             updated.append(i)
#         steps.push(unstack(a, b))
#         return 1, steps.__contains__(), updated

# -----------------------------------------------------------------------------------------------------------------------------------

def checkPre1(a):         #CHECK WHEN THERE IS ONLY ONE ARGUMENT INPUT #HOLD / CLEAR / ONTABLE / PICKUP / PUTDOWN
    list1 = [pickup(a), PickupP(a)]
    for i in PickupP(a):
        list1.append(i)
    return list1



def checkClear(current,element):
    # global topvalue
    for i in current:
        if i[0] == 'O' and i[1] == 'N' and i[2] == '(' and i[5] == element and i[6] == ')':
            topvalue = i[3] #on(topvalue, element)
    list1 = [unstack(topvalue, element), UnstackP(topvalue, element)]
    for i in UnstackP(topvalue, element):
        list1.append(i)
    return list1

def checkOnTable(current, element):
    global bottomvalue
    for i in current:
        if i[0] == 'O' and i[1] == 'N' and i[2] == '(' and i[3] == element and i[6] == ')':
            bottomvalue = i[5]  # on(element, bottomvalue)
    list1 = [putdown(element), PutdownP(element), unstack(element, bottomvalue), UnstackP(element, bottomvalue)]
    for i in UnstackP(element, bottomvalue):
        list1.append(i)
    return list1



