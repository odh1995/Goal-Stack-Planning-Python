
#--------------------------------------------PICK-------------------------------------------------------------------------------------------------
def PickupP(x):
    predicates = ("ONTABLE(" + x + ")" + "^CLEAR(" + x + ")" + "^HANDEMPTY").split("^")
    return predicates

def PickupE(x):
    effect = ("HOLDING(" + x + ")")
    return effect
#--------------------------------------------PUT-------------------------------------------------------------------------------------------------
def PutdownP(x):
    predicates = "HOLDING(" + x + ")"
    return predicates

def PutdownE(x):
    effect = ("ONTABLE(" + x + ")" + "^CLEAR(" + x + ")" + "^HANDEMPTY").split("^")
    return effect
#--------------------------------------------STACK-------------------------------------------------------------------------------------------------
def StackP(x,y):
    predicates = ("HOLDING(" + x + ")" + "^CLEAR(" + y + ")").split("^")
    return predicates

def StackE(x,y):
    effect = ("ON(" + x + "," + y + ")" + "^CLEAR(" + x + ")" + "^HANDEMPTY").split("^")
    return effect
#--------------------------------------------UNSTACK-------------------------------------------------------------------------------------------------
def UnstackP(x,y):
    predicates = ("CLEAR(" + x + ")" + "^ON(" + x + "," + y + ")" + "^HANDEMPTY").split("^")
    return predicates

def UnstackE(x,y):
    effect = ("HOLDING(" + x + ")" + "^CLEAR(" + y + ")").split("^")
    return effect

#--------------------------------------------NOTHOLDING-------------------------------------------------------------------------------------------------
def NotHolding(x):
    out = ("PICKUP(" + x + ")" + "^" + PickupP(x)).split("^")
    return out

