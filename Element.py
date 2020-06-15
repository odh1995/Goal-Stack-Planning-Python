def Element(n):
    global first
    count = 0
    check = 0
    list = []
    for i in n:
        count += 1
        if i == '(':
            first = n[count]
        elif i == ',':
            second = n[count]
            check = 1
    if check != 1:
        list.append(first)
    else:
        list.append(first)
        list.append(second)
    return list
