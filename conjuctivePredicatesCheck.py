from checkPreconditions import*

def ConjuctiveCheckOn(n, a, b):
    if on(a, b) in n:
        list1 = [stack(a, b), StackP(a, b)]
        for i in StackP(a, b):
            list1.append(i)
        return list1